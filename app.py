from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

# Load model and preprocessing objects
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('updated_label_encoder.pkl')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define prediction mapping
prediction_mapping = {
    0: "The loan is approved",
    1: "The loan is rejected"
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        input_data = request.get_json()
        input_df = pd.DataFrame([input_data])

        # Transform categorical values
        input_df['Source of Income'] = le.transform(input_df['Source of Income'])
        input_df['Purpose'] = le.transform(input_df['Purpose'])

        # Scale input
        input_scaled = scaler.transform(input_df)

        # Make prediction
        raw_prediction = model.predict(input_scaled)
        prediction_message = prediction_mapping.get(int(raw_prediction[0]), "Unknown")

        return jsonify(prediction_message)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

