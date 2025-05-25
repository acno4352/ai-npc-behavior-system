from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Ensure the model and encoder paths are correctly resolved
model_path = os.path.join(os.path.dirname(__file__), "npc_behavior_model.pkl")
interaction_encoder_path = os.path.join(os.path.dirname(__file__), "interaction_encoder.pkl")
response_encoder_path = os.path.join(os.path.dirname(__file__), "response_encoder.pkl")

# Load the trained model and encoders
model = joblib.load(model_path)
interaction_encoder = joblib.load(interaction_encoder_path)
response_encoder = joblib.load(response_encoder_path)

print("Available interaction types:", interaction_encoder.classes_)


@app.route('/predict_npc_response', methods=['POST'])
def predict_npc_response():
    data = request.json
    print("Received data:", data)  # Debugging Output

    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400

    if 'interaction_type' not in data:
        return jsonify({"error": "Missing 'interaction_type'"}), 400

    if data['interaction_type'] not in interaction_encoder.classes_:
        return jsonify({"error": f"Unknown interaction type: {data['interaction_type']}"}), 400

    player_id = data['player_id']
    npc_id = data['npc_id']
    interaction_type = interaction_encoder.transform([data['interaction_type']])[0]

    X_input = pd.DataFrame([[player_id, npc_id, interaction_type]], columns=['player_id', 'npc_id', 'interaction_type'])
    prediction = model.predict(X_input)
    print("Model prediction:", prediction)

    npc_response = response_encoder.inverse_transform(prediction)[0]

    return jsonify({"npc_response": npc_response})

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
