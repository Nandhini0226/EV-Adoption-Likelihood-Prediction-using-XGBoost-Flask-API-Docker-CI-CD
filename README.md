# 🚗 EV Adoption Likelihood Prediction using XGBoost | Flask API | Docker | CI/CD

## 📌 Overview

This project predicts the likelihood of **Electric Vehicle (EV) adoption** using Machine Learning. It demonstrates an end-to-end ML workflow covering data preprocessing, feature engineering, model training, prediction, API deployment, and containerization.

The solution is built using the **XGBoost Classifier** integrated with a **Scikit-learn Pipeline** and deployed as a **Flask REST API**. The application is containerized using **Docker**, making it portable, reproducible, and deployment-ready. The project follows a CI/CD-ready structure and is designed for production-oriented ML deployment.

---

# 🚀 Features

* Data Cleaning
* Missing Value Handling
* Outlier Treatment
* Feature Engineering
* One-Hot Encoding
* Feature Scaling
* XGBoost Classification
* Scikit-learn Pipeline
* Model Serialization using Joblib
* Flask REST API
* JSON-based Prediction Endpoint
* Docker Containerization
* Docker Hub Ready
* CI/CD Ready Project Structure
* Production-ready Folder Organization

---

# 🏗️ Project Structure

```text
EV-Adoption-Likelihood-Prediction-Classification-CI_CD/
│
├── .github/
│   └── workflows/
│
├── data/
│   └── global_ev_adoption_behavior_2026.csv
│
├── models/
│   ├── ev_adoption_model.pkl
│   └── label_encoder.pkl
│
├── src/
│   ├── data_cleaning.py
│   ├── data_preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🧠 Machine Learning Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Train-Test Split
      │
      ▼
XGBoost Classifier
      │
      ▼
Model Evaluation
      │
      ▼
Save Model (.pkl)
      │
      ▼
Flask REST API
      │
      ▼
Docker Container
      │
      ▼
Deployment
```

---

# 📊 Dataset

The project uses the **Global EV Adoption Behavior 2026** dataset containing demographic, financial, technological, behavioral, and environmental factors influencing EV adoption.

## Target Variable

```
ev_adoption_likelihood
```

Possible Classes

* High
* Medium
* Low

---

# 🛠 Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Docker
* Git
* GitHub

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Nandhini0226/continuous-integration-and-deployment.git
```

## Navigate into Project

```bash
cd continuous-integration-and-deployment
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

```bash
python src/train.py
```

This generates:

```
models/
    ev_adoption_model.pkl
    label_encoder.pkl
```

---

# 🔮 Run Prediction

```bash
python src/predict.py
```

The prediction script loads the saved model and predicts EV Adoption Likelihood for new data.

---

# 🌐 Flask REST API

Start the API

```bash
python app.py
```

Application runs on

```
http://127.0.0.1:5000
```

---

# 📡 API Endpoints

## Home Endpoint

### GET /

Returns

```json
{
  "message": "EV Adoption Likelihood Prediction API is running!"
}
```

---

## Prediction Endpoint

### POST /predict

Example Request

```json
{
  "annual_income":60000,
  "charging_station_accessibility":8,
  "technology_affinity_score":7,
  "environmental_awareness_score":9,
  "range_anxiety_score":4,
  "ev_knowledge_score":8,
  "battery_replacement_concern":3,
  "government_incentive_awareness":7,
  "nearest_charging_station_km":2.5,
  "previous_ev_experience":"Yes",
  "city_type":"Urban",
  "home_charging_available":"Yes"
}
```

Example Response

```json
{
    "prediction":"High"
}
```

---

# 🐳 Docker Containerization

## Build Docker Image

```bash
docker build -t ev-adoption-app .
```

---

## Verify Docker Image

```bash
docker images
```

---

## Run Docker Container

```bash
docker run -p 5000:5000 ev-adoption-app
```

The API will be available at

```
http://localhost:5000
```

---

## Docker Hub

Push the Docker image

```bash
docker login

docker tag ev-adoption-app nandhini0426/ev-adoption-app:latest

docker push nandhini0426/ev-adoption-app:latest
```

Pull the image

```bash
docker pull nandhini0426/ev-adoption-app:latest
```

Run directly from Docker Hub

```bash
docker run -p 5000:5000 nandhini0426/ev-adoption-app:latest
```

---

# 🧪 API Testing

The API can be tested using

* Postman
* Thunder Client
* cURL
* Python Requests

---

# 📁 Model Files

After training

```
models/
│
├── ev_adoption_model.pkl
└── label_encoder.pkl
```

---

# 🔄 CI/CD

This project follows a CI/CD-ready structure.

Current Implementation

* Flask API
* Docker Containerization
* Docker Image Build
* Docker Hub Integration

Planned Enhancements

* GitHub Actions
* Jenkins Pipeline
* Automated Testing
* Cloud Deployment
* Model Monitoring

---

# 🚀 Future Enhancements

* GitHub Actions CI/CD
* Jenkins CI/CD
* Docker Compose
* Kubernetes Deployment
* AWS Deployment
* Azure Deployment
* Streamlit Dashboard
* Model Monitoring
* Automated Retraining
* MLflow Integration

---

# 💼 Skills Demonstrated

* Machine Learning
* Feature Engineering
* Data Preprocessing
* XGBoost
* Scikit-learn Pipelines
* Flask API Development
* REST API Design
* Model Serialization
* Docker
* Docker Hub
* Git & GitHub
* CI/CD Concepts

---

# 👩‍💻 Author

**Nandhini**

GitHub: https://github.com/Nandhini0226

---

# 📄 License

This project is developed for learning, portfolio development, and demonstration purposes.
