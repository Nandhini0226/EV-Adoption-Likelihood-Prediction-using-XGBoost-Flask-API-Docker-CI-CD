
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Selected numerical features
numerical_features = [
    'annual_income',
    'charging_station_accessibility',
    'technology_affinity_score',
    'environmental_awareness_score',
    'range_anxiety_score',
    'ev_knowledge_score',
    'battery_replacement_concern',
    'government_incentive_awareness',
    'nearest_charging_station_km'
]

# Selected categorical features
categorical_features = [
    'previous_ev_experience',
    'city_type',
    'home_charging_available'
]

def get_preprocessor():
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ]
    )

    return preprocessor