# Accident Service Prediction System
### Diploma 3rd-Year Computer Science and Engineering Internship Project

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask 3.0+](https://img.shields.io/badge/Flask-3.1-black.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg)](https://scikit-learn.org/)
[![Leaflet.js](https://img.shields.io/badge/Leaflet-1.9.4-green.svg)](https://leafletjs.com/)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-pink.svg)](https://www.chartjs.org/)
[![W3C OWL 2](https://img.shields.io/badge/Ontology-W3C_OWL_2-purple.svg)](https://www.w3.org/OWL/)
[![Tests Passing](https://img.shields.io/badge/Tests-33%2F33_Passed-brightgreen.svg)]()

A complete, responsive, full-stack road safety management and emergency dispatch decision-support platform. The application combines **pre-trip road accident risk prediction (Machine Learning without target leakage)**, **geospatial accident hotspot clustering (Leaflet.js & OpenStreetMap)**, **emergency facility discovery & Haversine distance calculations**, **incident records management (CRUD)**, **dispatcher triage workflows**, **semantic knowledge modeling (W3C OWL 2 Ontology with RDFLib SPARQL querying)**, and a **centralized administrative panel**.

---

## 1. Key Features & Modules

1. **Accident Risk Prediction Engine (`modules/ml/` & `modules/prediction/`)**
   - Trained Scikit-Learn **Random Forest Classifier** with balanced class weighting.
   - **Target Leakage Prevention**: Features are strictly restricted to pre-crash parameters (road classification, weather conditions, lighting, visibility, traffic density, time of day, day of week).
   - Generates calibrated risk indices (0–100%), classified into **Low, Medium, and High** tiers.
   - Provides plain-English explanations identifying specific hazards (e.g. unlit expressway + heavy rain) and recommends proactive safety precautions.
   - Retains a persistent audit history of all user predictions.

2. **Accident Hotspot Geospatial Analysis (`modules/hotspots/`)**
   - Interactive Leaflet.js canvas with custom intensity circles and cluster popups.
   - Multi-tier classification: High Frequency ($\ge 5$ crashes), Medium Frequency (3–4 crashes), Low Frequency (1–2 crashes).
   - Filter by date range, area/sector, road type, and severity tier.
   - High-frequency accident corridors leaderboard table.

3. **Emergency Services Locator (`modules/emergency/`)**
   - Verified directory for **Trauma Hospitals**, **Paramedic Ambulances**, **Traffic Police Posts**, and **Fire & Rescue Stations**.
   - **Haversine Distance Calculator**: Sorts facilities by true spherical distance from user coordinates or detected GPS location.
   - Direct click-to-call dialing (`tel:...`) and OpenStreetMap directions links.
   - Prominent **National Emergency Hotline 112** safety notice.

4. **Emergency Assistance Request Workflow (`modules/emergency/`)**
   - Citizens log incident assistance requests with location and casualty notes.
   - **Operator Dispatch Queue**: Dispatchers triage requests through a verified progression:
     $$\text{Pending} \longrightarrow \text{Reviewed} \longrightarrow \text{Assigned} \longrightarrow \text{Dispatched} \longrightarrow \text{Completed / Cancelled}$$
   - Full chronological dispatch audit trail with dispatcher notes and citizen notification alerts.

5. **Accident Records Management (`modules/accidents/`)**
   - Full CRUD operations with server-side input validation.
   - Searching by keyword, filtering by severity and road classification, and multi-field sorting.
   - Real-time CSV data export.

6. **W3C OWL 2 Semantic Ontology (`ontology/`)**
   - Validated ontology (`accident_service.owl`) defining **28 classes**, **12 object properties**, **8 data properties**, and **13 named individuals**.
   - Built-in RDFLib / SPARQL query engine and interactive web graph inspector.

7. **Reports & Statistical Analytics (`modules/reports/`)**
   - Chart.js visualizations for monthly incident trends, severity doughnuts, weather correlation bars, road type distributions, and request status breakdowns.
   - Clear visual distinction between historical ground-truth data and model risk predictions.

8. **Role-Based Access Control & Security (`modules/auth/` & `modules/admin/`)**
   - Three distinct user roles: **Citizen**, **Emergency Operator**, **Administrator**.
   - Secure password hashing via `werkzeug.security` (Scrypt / PBKDF2).
   - Session protection, HTTP-only cookies, and CSRF token verification across all forms.
   - System-wide audit log for traceability and regulatory compliance.

---

## 2. Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3, Bootstrap Icons |
| **Interactive Maps** | Leaflet.js 1.9.4 with OpenStreetMap |
| **Visualizations** | Chart.js 4.4 |
| **Backend Framework** | Python 3.10+, Flask 3.1 (Application Factory & Blueprints) |
| **Database** | SQLite 3 (15 normalized schema tables with foreign keys & indexes) |
| **Machine Learning** | Scikit-learn, Pandas, NumPy, Joblib |
| **Semantic Web** | W3C OWL 2 Ontology XML, RDFLib (SPARQL 1.1) |
| **Testing** | PyTest 9.1 |

---

## 3. Preconfigured Demo Accounts

For evaluation, examination, or presentation purposes, the system is seeded with 3 active demonstration accounts:

| Role | Username | Password | Access Scope |
|---|---|---|---|
| **Administrator** | `admin` | `AdminPassword123!` | System settings, user role management, CSV import, audit logs, facilities CRUD |
| **Emergency Operator** | `operator1` | `OperatorPassword123!` | Operational dispatch queue, triage ticket updates, accident logging |
| **Citizen User** | `citizen1` | `CitizenPassword123!` | Route risk predictions, emergency locator, requesting assistance, personal history |

---

## 4. Installation & Quickstart Guide

### Step 1: Clone or Navigate to Project Directory
```powershell
cd c:\Users\Dell\Documents\intenship\project\project1
```

### Step 2: Set Up Python Virtual Environment (Optional but Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
> *Tip (Windows PowerShell): If script execution is disabled, allow it for the current user once:*
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
> *Or on standard Windows Command Prompt (cmd.exe):* `venv\Scripts\activate.bat`

### Step 3: Install Required Dependencies
```powershell
pip install -r requirements.txt
```

### Step 4: Seed Database & Train Machine Learning Model
The database is auto-seeded on first run, or you can trigger training and seeding manually:
```powershell
# 1. Generate clean pre-crash training dataset
python data/generate_data.py

# 2. Train and evaluate the Random Forest model
python modules/ml/train.py

# 3. Seed SQLite schema and initial demonstration records
python database/seed_data.py
```

### Step 5: Run Automated Tests
```powershell
python -m pytest tests/
```
*(All 33 unit and integration tests should pass in under 5 seconds).*

### Step 6: Start the Flask Application
```powershell
python app.py
```
Open your browser and navigate to:
**`http://127.0.0.1:5000/`**

---

## 5. Project Directory Structure

```
project1/
├── app.py                      # Central Flask application factory & error handlers
├── config.py                   # System configuration, paths, and security defaults
├── requirements.txt            # Python dependency specification
├── README.md                   # Installation, overview, and quickstart documentation
├── database/
│   ├── __init__.py             # Database module initializer
│   ├── db.py                   # Context-aware SQLite connector & query execution helpers
│   ├── schema.sql              # Normalized SQLite schema (15 tables, indexes, constraints)
│   └── seed_data.py            # Realistic demonstration data seeder
├── data/
│   ├── generate_data.py        # Pre-event historical road safety dataset generator
│   ├── raw/
│   │   └── historical_accidents_sample.csv # 1,200 verified pre-crash records
│   └── processed/
├── models/
│   ├── accident_risk_model.joblib # Persisted Scikit-learn Pipeline
│   └── evaluation_results.json    # Exact test evaluation metrics & confusion matrix
├── ontology/
│   ├── accident_service.owl    # W3C OWL 2 XML / RDF ontology
│   └── ontology_manager.py     # RDFLib graph loader, SPARQL query engine, taxonomy parser
├── modules/
│   ├── auth/                   # Authentication, registration, profile, decorators, CSRF
│   ├── dashboard/              # Live operational dashboard with dynamic statistics
│   ├── accidents/              # Accident records CRUD, pagination, filtering, CSV export
│   ├── prediction/             # ML inference, risk scoring, explanations, evaluation view
│   ├── hotspots/               # Leaflet hotspot mapping, cluster filters, GeoJSON API
│   ├── emergency/              # Services directory, Haversine sorting, request queue, timeline
│   ├── admin/                  # User management, facility registry, CSV dataset import, audit logs
│   ├── reports/                # Safety analytics, Chart.js trends, CSV summary export
│   ├── ontology/               # Web taxonomy viewer, SPARQL query console, OWL download
│   └── ml/                     # ML training pipeline, balanced Random Forest, predictor class
├── templates/
│   ├── base.html               # Professional dark navy, crimson, and white layout
│   ├── components/             # Flash messages, sidebar navigation
│   ├── public/                 # Home, About, Contact pages
│   ├── auth/                   # Sign in, Citizen registration, User profile
│   ├── dashboard/              # Dynamic operations dashboard
│   ├── accidents/              # Accident list, detail, creation, edit views
│   ├── prediction/             # Risk prediction interface, history, model evaluation
│   ├── hotspots/               # Interactive Leaflet hotspot map
│   ├── emergency/              # Services directory, request form, user requests, operator queue, timeline
│   ├── admin/                  # Admin dashboard, users, facilities, dataset CSV import, audit logs
│   ├── reports/                # Visual analytics and trend reports
│   ├── ontology/               # Interactive OWL 2 taxonomy and SPARQL query console
│   └── errors/                 # 400, 403, 404, 500 error pages
├── static/
│   ├── css/
│   │   └── style.css           # Core styling, cards, status badges, map containers
│   └── js/
│       ├── main.js             # General UI utilities, tooltips, confirmations
│       ├── hotspot_map.js      # Leaflet hotspot rendering and AJAX filters
│       └── emergency_map.js    # Geolocation, Haversine distance calculator, facility popups
├── tests/
│   ├── conftest.py             # Pytest fixtures and authenticated session helpers
│   ├── test_auth.py            # Authentication and role access tests
│   ├── test_accidents.py       # Accident records CRUD & CSV export tests
│   ├── test_prediction.py      # ML inference and evaluation tests
│   ├── test_emergency.py       # Locator, Haversine formula, and triage tests
│   ├── test_ontology.py        # OWL parsing and SPARQL query tests
│   └── test_db.py              # Schema integrity and seed record tests
└── docs/
    ├── architecture.md         # Detailed system design, data dictionary & algorithms
    └── project_report.md       # Diploma 3rd-Year CSE internship project report outline
```

---

## 6. Machine Learning Model Architecture

### Features (Pre-Trip Conditions Only)
1. `road_type`: Expressway, Major Highway, Arterial Highway, Urban Street, Rural Road
2. `weather_condition`: Clear, Rainy, Foggy, Cloudy, Stormy
3. `traffic_density`: Low, Moderate, Heavy, Congested
4. `visibility`: Good (> 8 km), Moderate (4–8 km), Low (< 4 km)
5. `lighting_condition`: Daylight, Dusk/Dawn, Darkness - Street Lights On, Darkness - No Lights
6. `time_of_day`: Morning, Afternoon, Evening, Night
7. `day_of_week`: Monday through Sunday

### Pipeline Architecture
- **Preprocessing**: `ColumnTransformer` with `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`.
- **Estimator**: `RandomForestClassifier(n_estimators=120, max_depth=10, class_weight='balanced', random_state=42)`.
- **Evaluation Split**: 80% Training ($n=960$), 20% Stratified Testing ($n=240$).
- **Empirical Test Performance**:
  - **Accuracy**: $81.67\%$
  - **Weighted Precision**: $81.96\%$
  - **Weighted Recall**: $81.67\%$
  - **Weighted F1-Score**: $81.51\%$

---

## 7. W3C OWL 2 Ontology Summary

- **File**: `ontology/accident_service.owl`
- **IRI**: `http://www.semanticweb.org/accident_service`
- **Total Axioms / Triples**: $185$
- **Main Classes ($28$)**: `Person`, `Citizen`, `Administrator`, `EmergencyOperator`, `Accident`, `AccidentType`, `SeverityLevel`, `Location`, `RoadSegment`, `AccidentHotspot`, `EnvironmentalCondition`, `WeatherCondition`, `TrafficCondition`, `Prediction`, `InputFeature`, `PredictionResult`, `RiskLevel`, `EmergencyService`, `Hospital`, `AmbulanceService`, `PoliceStation`, `FireAndRescueService`, `ServiceRequest`, `EmergencyResponse`, `Notification`, `Dataset`, `ModelEvaluation`, `AuditLog`.
- **Object Properties ($12$)**: `reportedBy`, `occurredAt`, `hasWeather`, `hasTrafficCondition`, `hasSeverity`, `predictsRiskAt`, `producesResult`, `recommendsService`, `locatedAt`, `requestsService`, `assignedTo`, `generatesNotification`.
- **Data Properties ($8$)**: `accidentDateTime`, `latitude`, `longitude`, `riskScore`, `riskLevel`, `serviceName`, `contactNumber`, `requestStatus`.

---

## 8. Academic & Educational Notice

> [!IMPORTANT]
> **Educational Demonstration**: This web application was created as an internship capstone project for a **Diploma 3rd-Year in Computer Science and Engineering**. It is not an officially commissioned emergency dispatch authority.
> In a genuine emergency in India, dial **112** (National Emergency Response Support System) or **108** (Ambulance).
