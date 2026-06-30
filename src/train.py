import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

from data_cleaning import clean_data
from data_preprocessing import (
    get_preprocessor,
    numerical_features,
    categorical_features
)
print("Program started")
# Load dataset
df = pd.read_csv("data/global_ev_adoption_behavior_2026.csv")
print("Data Loaded successfully!")

# Clean data
df = clean_data(df)
print("Data cleaned successfully!")
print(df)


print("Preparing data for training...")


X = df[numerical_features + categorical_features]
y = df["ev_adoption_likelihood"] 



# Encode target
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Save encoder
joblib.dump(label_encoder, "models/label_encoder.pkl")

# Create pipeline
model = Pipeline([
    ("preprocessor", get_preprocessor()),
    ("classifier", XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    ))
])

# Train model
model.fit(X, y)

print("Model trained successfully!")

# Save model
joblib.dump(model, "models/ev_adoption_model.pkl")

print("Model saved successfully!")