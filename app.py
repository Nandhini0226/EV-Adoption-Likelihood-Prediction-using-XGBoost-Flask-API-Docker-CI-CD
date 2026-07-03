from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained pipeline and label encoder
model = joblib.load("models/ev_adoption_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "EV Adoption Likelihood Prediction API is running!"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Convert JSON to DataFrame
        df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(df)

        # Convert numeric prediction back to label
        prediction_label = label_encoder.inverse_transform(prediction)

        return jsonify({
            "prediction": prediction_label[0]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)