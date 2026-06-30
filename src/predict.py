import pandas as pd
import joblib

# Load trained model and label encoder
model = joblib.load("models/ev_adoption_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

# Sample input
sample_data = {
    "annual_income": [850000],
    "charging_station_accessibility": [8],
    "technology_affinity_score": [9],
    "environmental_awareness_score": [8],
    "range_anxiety_score": [3],
    "ev_knowledge_score": [9],
    "battery_replacement_concern": [4],
    "government_incentive_awareness": [8],
    "nearest_charging_station_km": [2],
    "previous_ev_experience": ["Yes"],
    "city_type": ["Urban"],
    "home_charging_available": ["Yes"]
}

# Convert to DataFrame
input_df = pd.DataFrame(sample_data)

# Predict
prediction = model.predict(input_df)

# Convert numeric prediction back to original label
prediction_label = label_encoder.inverse_transform(prediction)

print("Predicted EV Adoption Likelihood:", prediction_label[0])