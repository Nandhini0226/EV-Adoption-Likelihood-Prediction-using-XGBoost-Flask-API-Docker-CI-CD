# EV Adoption Likelihood Prediction using XGBoost | Flask API | CI/CD Project

## Overview

This project predicts the likelihood of Electric Vehicle (EV) adoption using Machine Learning. It implements an end-to-end machine learning workflow, including data cleaning, preprocessing, model training, prediction, and deployment through a Flask REST API. The project is organized using a CI/CD-ready structure, making it suitable for deployment and automation.

The model is built using the XGBoost Classifier integrated with a Scikit-learn Pipeline for efficient preprocessing and prediction.

---

## Project Structure

```text
EV-Adoption-Likelihood-Prediction-Classification-CI_CD/
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
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Features

* Data Cleaning
* Missing Value Handling
* Outlier Treatment
* Feature Preprocessing
* One-Hot Encoding
* Feature Scaling
* XGBoost Classification
* Model Serialization using Joblib
* Prediction Pipeline
* Flask REST API
* JSON-based Prediction Endpoint
* CI/CD Ready Project Structure

---

## Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib

---

## Dataset

The project uses the **Global EV Adoption Behavior 2026** dataset containing demographic, financial, behavioral, and environmental factors influencing electric vehicle adoption.

### Target Variable

**ev_adoption_likelihood**

Possible classes:

* High
* Medium
* Low

---

## Machine Learning Workflow

1. Load Dataset
2. Clean Data
3. Handle Missing Values
4. Encode Categorical Variables
5. Scale Numerical Features
6. Split Train/Test Data
7. Train XGBoost Classifier
8. Evaluate Model Performance
9. Save Trained Model
10. Predict EV Adoption Likelihood
11. Deploy Model using Flask REST API

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Nandhini0226/continuous-integration-and-deployment.git
```

### Navigate to the Project Folder

```bash
cd continuous-integration-and-deployment
```

### Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

```bash
python src/train.py
```

This generates:

* `models/ev_adoption_model.pkl`
* `models/label_encoder.pkl`

---

## Run Prediction

```bash
python src/predict.py
```

The script loads the saved model and predicts the EV adoption likelihood for new input data.

---

# Flask REST API

## Start the Flask Server

```bash
python app.py
```

The Flask server will start at:

```
http://127.0.0.1:5000/
```

---

## API Endpoints

### Home Endpoint

**GET /**

Returns a message indicating that the API is running.

Example response:

```json
{
    "message": "EV Adoption Likelihood Prediction API is running!"
}
```

---

### Prediction Endpoint

**POST /predict**

Example request body:

```json
{
    "annual_income": 60000,
    "charging_station_accessibility": 8,
    "technology_affinity_score": 7,
    "environmental_awareness_score": 9,
    "range_anxiety_score": 4,
    "ev_knowledge_score": 8,
    "battery_replacement_concern": 3,
    "government_incentive_awareness": 7,
    "nearest_charging_station_km": 2.5,
    "previous_ev_experience": "Yes",
    "city_type": "Urban",
    "home_charging_available": "Yes"
}
```

Example response:

```json
{
    "prediction": "High"
}
```

---

## Testing the API

The API can be tested using:

* Thunder Client
* Postman
* cURL
* Python `requests`

---

## Model Files

After training, the following files are created inside the `models` directory:

* `ev_adoption_model.pkl` – Trained XGBoost Pipeline
* `label_encoder.pkl` – Label Encoder for decoding predictions

---

## Future Enhancements

* Streamlit Dashboard
* Docker Containerization
* GitHub Actions CI/CD
* Jenkins Pipeline
* Cloud Deployment
* Model Monitoring
* Automated Model Retraining

---

## Author

**Nandhini**

GitHub: https://github.com/Nandhini0226

---

## License

This project is developed for learning, portfolio development, and demonstration purposes.
