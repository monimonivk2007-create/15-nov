Here is your final **VS Code-ready Software Project Specification Sheet (SRS)** for building the complete FINTRUST AI application. This version uses a consistent **White + Blue theme**, Python backend, Machine Learning, and a professional fintech dashboard.

# **FINTRUST AI – Project Specification Sheet**

FULL-STACK AI PROJECT

# **FINTRUST AI**

**Real-Time Financial Fraud & Mule Account Detection Engine**

*Detect suspicious transactions. Identify financial risks. Analyze account networks.*

[SaaS Fraud Detection Dashboard by Yuliya Lebedeva on Dribbble](https://images.openai.com/static-rsc-4/em2ojPP79l0JnVg-qMA97c4-mMzedHe6E0FC-1vSyY0VTOayrz3Om5MhofVciju8jkSpUhvnjA7khJdiYVRREWITmWbsN8yBGqz2Oc4ODl4AjU8fHErqblHR8J6eU7N_I3zgCu1GWSUWS6IYP45YHQdI2lYsSTQWs-HJuNTGHkY?purpose=inline)

[dribbble.com](https://dribbble.com/shots/27001312-SaaS-Fraud-Detection-Dashboard?utm_source=chatgpt.com)

Development IDE

**Visual Studio Code**

Application

**Web Platform**

Backend

**Python + FastAPI**

Machine Learning

**Scikit-learn**

## **1. Project Overview**

FINTRUST AI is an AI-powered financial security platform that detects suspicious digital transactions, identifies potentially fraudulent activities, and discovers possible mule accounts using Machine Learning and account relationship analysis.

The application processes simulated financial transactions, analyzes transaction behavior, calculates risk scores, and generates automated fraud alerts.

It also uses graph-based network analysis to identify suspicious relationships between multiple accounts.

The platform must be a fully functional application, not just a static dashboard.

## **2. Project Objectives**

- Monitor simulated financial transactions in real time.
- Detect suspicious and potentially fraudulent transactions.
- Identify abnormal transaction patterns.
- Predict fraud probability using Machine Learning.
- Detect potential mule accounts.
- Analyze connected suspicious accounts.
- Generate transaction risk scores.
- Provide interactive fraud monitoring dashboards.

## **3. Technology Stack**

| Layer             | Technology              |
| ----------------- | ----------------------- |
| Language          | Python                  |
| Backend           | FastAPI                 |
| Frontend          | HTML5, CSS3, JavaScript |
| UI Framework      | Bootstrap 5             |
| Database          | SQLite                  |
| ORM               | SQLAlchemy              |
| Data Processing   | Pandas, NumPy           |
| Classification    | Random Forest           |
| Anomaly Detection | Isolation Forest        |
| Network Analysis  | NetworkX                |
| Charts            | Chart.js                |
| Model Storage     | Joblib                  |
| API Testing       | Swagger UI              |
| Development       | VS Code                 |

## **4. Functional Modules**

### **Module 1 – Transaction Monitoring**

- Generate simulated transactions.
- Monitor incoming and outgoing transactions.
- Store transaction records in SQLite.
- Display transaction IDs, sender, receiver, amount, date, and status.
- Automatically refresh the monitoring dashboard.

### **Module 2 – AI Fraud Detection**

Implement Random Forest classification to classify transactions into:

1. Legitimate Transaction
2. Suspicious Transaction
3. Potentially Fraudulent Transaction

Analyze transaction amount, frequency, account activity, transaction timing, and unusual behavior.

Display fraud probability from 0–100%.

### **Module 3 – Mule Account Detection**

Identify possible mule account patterns using:

- Multiple incoming transfers.
- Unusual outgoing transfers.
- High transaction volume.
- Unusual account activity.
- Suspicious account relationships.

Use NetworkX to visualize account connections.

### **Module 4 – Risk Scoring Engine**

| Score  | Classification |
| ------ | -------------- |
| 0–30   | Low Risk       |
| 31–60  | Medium Risk    |
| 61–80  | High Risk      |
| 81–100 | Critical Risk  |

Risk scores must be calculated using documented model outputs and risk indicators.

### **Module 5 – Fraud Alerts**

Generate automated alerts containing:

- Alert ID.
- Transaction ID.
- Account ID.
- Transaction amount.
- Fraud probability.
- Risk level.
- Detection reason.
- Timestamp.

Include risk-level filtering.

### **Module 6 – Transaction History**

- Search transaction ID.
- Search account ID.
- Filter transactions by risk.
- Sort by date and amount.
- View transaction details.
- Display model predictions.

## **5. Dashboard UI Specification**

Required Theme: White + Blue

[From Idea to Interactive: Vibe-Coding a Fraud Detection Dashboard with AI](https://images.openai.com/static-rsc-4/oz-z1kW03V-1FFhXYSX4n3GBS6eN8wdchh9-Y_eAQAbvTwOp9CnKopn-2yG640c9VyQPvnUjGeDbyzwqAfkU5obJaJ9fiYlSvYzISk3pyAgvFe-DvVgR1_eiXaQHWo-VeC5P1ZU6Knejm3nQHvFLLxegMeydRLvimL8D_ituDCo?purpose=inline)

[Adaptive Fraud Detection AI Platform for MP Police | Built with Blink](https://images.openai.com/static-rsc-4/xt8OP47njAFJOq8kcSqBeaH-6VnYMsspwTYJlfGJkTFg6rtRPeI655JDxM9gxNFv9UWEaG-r9SSYmqNe-Wzs2hbYnpzJJ7KepPQoBP23bwk0pVJxvNZYcCDYm1rmH49nMu1UKW5mJzndYa6OuaevAlElXUQXyU-f7QGt4cmnqkU?purpose=inline)

[Sensfrx - AI-powered fraud detection for ecommerce | AppSumo](https://images.openai.com/static-rsc-4/GR-xOptlMpOIlQQjYAOwu1Ps4Y4uCcJn0Lq0ZfPlWOI99FF6r8_ibgc4d4wIN0vbD-ZnW8mmz91ENwu2FuyiTmlzvcXGsBCA79XJax6N1mJaDdFmOSNeg_e69eX_lH55zws6s8OwDJmlkWJAfrc4vmcL8D3lrguVm-357TYOiT4?purpose=inline)

15

### **Color Palette**

| Element        | Color     |
| -------------- | --------- |
| Background     | `#FFFFFF` |
| Primary Blue   | `#2563EB` |
| Light Blue     | `#DBEAFE` |
| Dark Text      | `#0F172A` |
| Secondary Text | `#64748B` |
| Border         | `#E2E8F0` |
| Success        | `#16A34A` |
| Warning        | `#F59E0B` |
| Critical       | `#DC2626` |

### **Dashboard Summary Cards**

1. Total Transactions
2. Legitimate Transactions
3. Suspicious Transactions
4. Potentially Fraudulent Transactions
5. Potential Mule Accounts
6. Total Flagged Amount

### **Dashboard Charts**

1. Transaction Volume Over Time
2. Fraud vs Legitimate Transactions
3. Risk Distribution
4. Top Suspicious Accounts
5. Fraud Detection Trends

### **Navigation Sidebar**

- Dashboard
- Live Transactions
- Fraud Detection
- Mule Account Analysis
- Fraud Alerts
- Transaction History
- Model Performance
- Settings

## **6. Machine Learning Specification**

**Random Forest Classifier**

Classifies simulated transactions into three categories.

**Isolation Forest**

Identifies unusual transaction patterns and anomalies.

**Feature Engineering**

- Transaction amount.
- Transaction frequency.
- Time difference.
- Sender transaction count.
- Receiver transaction count.
- Incoming amount.
- Outgoing amount.
- Unique counterparties.
- Account activity.

**Model Evaluation**

- Accuracy.
- Precision.
- Recall.
- F1-score.
- Confusion matrix.

Save trained models using Joblib. Use realistic synthetic patterns and a reproducible train/test split. Clearly identify all model performance as experimental synthetic-data performance.

## **7. Backend API Specification**

| Method | Endpoint                         | Description           |
| ------ | -------------------------------- | --------------------- |
| GET    | `/transactions`                  | Retrieve transactions |
| POST   | `/transactions`                  | Add transaction       |
| GET    | `/transactions/{transaction_id}` | Transaction details   |
| GET    | `/fraud-alerts`                  | Retrieve alerts       |
| GET    | `/dashboard/summary`             | Dashboard statistics  |
| GET    | `/accounts`                      | Retrieve accounts     |
| GET    | `/accounts/{account_id}`         | Account details       |
| GET    | `/accounts/{account_id}/network` | Account network       |
| POST   | `/predict-fraud`                 | Predict transaction   |
| GET    | `/model/performance`             | Model metrics         |

## **8. Database Specification**

Use SQLite and SQLAlchemy.

Create four primary tables:

- `transactions`
- `accounts`
- `fraud_alerts`
- `model_logs`

Store transaction history, account information, risk classifications, alert details, and model prediction records.

## **9. VS Code Project Folder Structure**

Create the following structure:

```
fraud_detection_engine/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── transactions.py
│   │   ├── fraud.py
│   │   ├── accounts.py
│   │   └── dashboard.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── fraud_detector.py
│       ├── risk_scoring.py
│       └── mule_detector.py
│
├── ml/
│   ├── __init__.py
│   ├── train_model.py
│   ├── feature_engineering.py
│   ├── evaluate_model.py
│   └── saved_model/
│
├── frontend/
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── transactions.html
│   │   ├── fraud.html
│   │   ├── mule_accounts.html
│   │   ├── alerts.html
│   │   └── performance.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   ├── dashboard.js
│       │   ├── transactions.js
│       │   └── charts.js
│       └── images/
│
├── data/
│   ├── generate_data.py
│   └── transactions.csv
│
├── tests/
│   ├── test_api.py
│   ├── test_fraud.py
│   └── test_mule.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## **10. Security Requirements**

- Use simulated transaction data only.
- Validate API inputs using Pydantic.
- Use environment variables.
- Implement exception handling.
- Use secure database operations.
- Avoid hardcoded credentials.
- Keep backend and frontend code modular.
- Include unit tests.
- Clearly label suspected fraud as an algorithmic assessment, not confirmed criminal activity.

## **11. Development Workflow**

1. **Phase 1:** Create the project structure in VS Code.
2. **Phase 2:** Set up Python virtual environment and dependencies.
3. **Phase 3:** Generate the simulated transaction dataset.
4. **Phase 4:** Develop and train ML models.
5. **Phase 5:** Implement mule account analysis using NetworkX.
6. **Phase 6:** Develop FastAPI backend and SQLite database.
7. **Phase 7:** Build the white-and-blue dashboard.
8. **Phase 8:** Integrate all modules and APIs.
9. **Phase 9:** Run tests, fix errors, and document the project.

## **12. VS Code Execution Commands**

**Create virtual environment:**

```
python -m venv venv
```

**Activate on Windows:**

```
venv\Scripts\activate
```

**Install dependencies:**

```
pip install -r requirements.txt
```

**Train ML model:**

```
python -m ml.train_model
```

**Run application:**

```
uvicorn backend.main:app --reload
```

**Open application:**

`http://127.0.0.1:8000`

**API documentation:**

`http://127.0.0.1:8000/docs`

## **13. Final Project Acceptance Checklist**

- Project runs in VS Code.
- Synthetic dataset is generated.
- Random Forest model trains successfully.
- Isolation Forest detects anomalies.
- Fraud predictions work.
- Risk scores are calculated.
- Mule accounts are identified.
- Network visualization works.
- Fraud alerts are stored.
- Transaction history works.
- Dashboard charts display database data.
- All API endpoints work.
- White-and-blue theme is consistent.
- Unit tests pass.
- README includes setup instructions.

# **14. Master Prompt for VS Code AI Coding Assistant**

Copy this complete instruction into your AI coding assistant inside VS Code.

# MASTER PROJECT DEVELOPMENT PROMPT – FINTRUST AI

Act as a Senior Python Developer, Machine Learning Engineer, Full-Stack Developer, and Financial Security Architect.

Your task is to build a complete, production-style academic prototype named FINTRUST AI – Real-Time Financial Fraud & Mule Account Detection Engine.

TECHNOLOGY:

- Python
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Isolation Forest
- SQLite
- SQLAlchemy
- NetworkX
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Chart.js
- Joblib

DESIGN:\
Use a consistent WHITE AND BLUE THEME throughout the application.\
Use white backgrounds, blue primary buttons, light-blue highlights, clean tables, rounded cards, modern typography, and a professional fintech dashboard.

CORE IMPLEMENTATION:

1. Generate realistic synthetic financial transaction datasets.
2. Build a complete feature engineering pipeline.
3. Train a Random Forest classification model.
4. Implement Isolation Forest anomaly detection.
5. Evaluate models using accuracy, precision, recall, F1-score, and confusion matrix.
6. Implement fraud risk scoring from 0 to 100.
7. Develop mule account detection using transaction relationships.
8. Visualize account networks using NetworkX.
9. Develop all required FastAPI endpoints.
10. Create SQLite database models and persistent storage.
11. Build a responsive dashboard with six summary cards and five analytics charts.
12. Implement live transaction simulation and automated fraud alerts.
13. Implement searchable transaction history.
14. Display model performance metrics.
15. Connect every frontend component to actual backend data.

DEVELOPMENT RULES:

- Inspect the existing VS Code workspace before making changes.
- Preserve useful existing files.
- Create missing files and folders.
- Follow the specified project architecture.
- Write complete, modular, maintainable code.
- Never use hardcoded or random fraud predictions.
- Do not create dashboard statistics that are disconnected from the database.
- Handle API validation and errors properly.
- Add tests for all important features.
- Use simulated transactions only.
- Clearly label synthetic data and experimental model performance.
- Do not claim a prediction proves actual fraud.

EXECUTION:\
Work through all development phases in order.\
Do not stop after creating the folders.\
Do not stop after creating the frontend.\
Integrate the database, ML models, backend, and frontend.\
Run the application, test APIs, fix errors, and update README.md.

FINAL DELIVERABLE:\
A complete, functional FINTRUST AI application that can be executed locally using VS Code, with a professional white-and-blue fintech dashboard and working fraud detection and mule account analysis features.

At the end, provide:

- Completed features.
- Project file structure.
- Installation commands.
- Execution commands.
- Test results.
- Any incomplete features or limitations.

**Important:** Use this specification as the main development reference. Give the coding assistant one phase at a time if it has limited context, and verify each phase before moving forward.