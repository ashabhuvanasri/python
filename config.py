import os
import secrets

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Application configuration settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(32))
    DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'accident_system.db')
    SCHEMA_PATH = os.path.join(BASE_DIR, 'database', 'schema.sql')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'data', 'raw')
    PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')
    MODEL_PATH = os.path.join(BASE_DIR, 'models', 'accident_risk_model.joblib')
    ONTOLOGY_PATH = os.path.join(BASE_DIR, 'ontology', 'accident_service.owl')
    
    # Upload and security
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
    ALLOWED_EXTENSIONS = {'csv'}
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Emergency Information
    OFFICIAL_EMERGENCY_NUMBER = "112"
    DISCLAIMER_TEXT = (
        "Educational Demonstration: This portal is a Diploma Engineering internship project "
        "and NOT an official emergency dispatch service. In a real emergency, immediately dial 112."
    )
    
    # Pagination
    ITEMS_PER_PAGE = 15

class TestConfig(Config):
    TESTING = True
    DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'test_accident_system.db')
    WTF_CSRF_ENABLED = False
