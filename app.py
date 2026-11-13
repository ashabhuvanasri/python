import os
from flask import Flask, render_template, session, request
from config import Config
from database.db import close_db, init_db
from modules.auth.decorators import generate_csrf_token

def create_app(config_class=Config):
    """Application factory for the Accident Service Prediction System."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure necessary folders exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['PROCESSED_DATA_DIR'], exist_ok=True)
    os.makedirs(os.path.dirname(app.config['DATABASE_PATH']), exist_ok=True)
    os.makedirs(os.path.dirname(app.config['MODEL_PATH']), exist_ok=True)

    # Database teardown registration
    app.teardown_appcontext(close_db)

    # Context processors for all Jinja2 templates
    @app.context_processor
    def inject_global_template_vars():
        return {
            'csrf_token': generate_csrf_token,
            'current_user': {
                'id': session.get('user_id'),
                'username': session.get('username'),
                'full_name': session.get('full_name'),
                'role': session.get('role'),
                'email': session.get('email')
            } if 'user_id' in session else None,
            'official_emergency_number': app.config['OFFICIAL_EMERGENCY_NUMBER'],
            'disclaimer_text': app.config['DISCLAIMER_TEXT'],
            'active_path': request.path
        }

    # Register Blueprints
    from modules.public.routes import public_bp
    from modules.auth.routes import auth_bp
    from modules.dashboard.routes import dashboard_bp
    from modules.accidents.routes import accidents_bp
    from modules.prediction.routes import prediction_bp
    from modules.hotspots.routes import hotspots_bp
    from modules.emergency.routes import emergency_bp
    from modules.admin.routes import admin_bp
    from modules.reports.routes import reports_bp
    from modules.ontology.routes import ontology_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(accidents_bp)
    app.register_blueprint(prediction_bp)
    app.register_blueprint(hotspots_bp)
    app.register_blueprint(emergency_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(ontology_bp)

    # Security and Cache Headers
    @app.after_request
    def set_cache_control_headers(response):
        """Prevent caching of authenticated session pages to secure browser history navigation."""
        if 'user_id' in session or request.path.startswith('/auth/'):
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
        return response

    # Error Handlers
    @app.errorhandler(400)
    def bad_request_error(e):
        return render_template('errors/400.html', error=e), 400

    @app.errorhandler(403)
    def forbidden_error(e):
        return render_template('errors/403.html', error=e), 403

    @app.errorhandler(404)
    def not_found_error(e):
        return render_template('errors/404.html', error=e), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html', error=e), 500

    # Ensure DB is created if not exists
    if not os.path.exists(app.config['DATABASE_PATH']):
        with app.app_context():
            from database.seed_data import seed_database
            print("[App Startup]: Initializing and seeding database...")
            seed_database(app.config['DATABASE_PATH'], app.config['SCHEMA_PATH'])

    return app

app = create_app()

if __name__ == '__main__':
    print("[Accident Safety System]: Running on http://127.0.0.1:5000 ...")
    app.run(host='127.0.0.1', port=5000, debug=True)
