from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the features from the request
    features = request.get_json()

    # Make a prediction
    prediction = model.predict(features)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


