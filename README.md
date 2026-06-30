# EV Adoption Likelihood Prediction using XGBoost | CI/CD Project

## Overview

This project predicts the likelihood of Electric Vehicle (EV) adoption using machine learning. It implements a complete machine learning workflow including data cleaning, preprocessing, model training, prediction, and project organization suitable for CI/CD deployment.

The model is built using the XGBoost classifier with a Scikit-learn pipeline for preprocessing.

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
* CI/CD Ready Project Structure

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib

---

## Dataset

The project uses the **Global EV Adoption Behavior 2026** dataset containing demographic, financial, behavioral, and environmental factors influencing electric vehicle adoption.

Target Variable:

* **ev_adoption_likelihood**

  * High
  * Medium
  * Low

---

## Machine Learning Pipeline

1. Load Dataset
2. Clean Data
3. Handle Missing Values
4. Encode Categorical Variables
5. Scale Numerical Features
6. Split Train/Test Data
7. Train XGBoost Classifier
8. Evaluate Model
9. Save Model
10. Predict New Data

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Nandhini0226/EV-Adoption-Likelihood-Prediction-Classification-CI_CD.git
```

Move into the project directory:

```bash
cd EV-Adoption-Likelihood-Prediction-Classification-CI_CD
```

Install the required packages:

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

## Future Enhancements

* Flask Web Application
* Streamlit Dashboard
* Docker Containerization
* GitHub Actions CI/CD
* Jenkins Pipeline
* Cloud Deployment
* Model Monitoring

---

## Author

**Nandhini**

GitHub:
https://github.com/Nandhini0226

---

## License

This project is created for learning, portfolio development, and demonstration purposes.
