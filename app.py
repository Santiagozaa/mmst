from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/predict')
def predict():
    # Get the input values from the query string
    age = int(request.args.get('age'))
    sex = int(request.args.get('sex'))
    bmi = float(request.args.get('bmi'))
    children = int(request.args.get('children'))
    smoker = int(request.args.get('smoker'))
    region = int(request.args.get('region'))

    # Make a prediction using the model
    prediction = model.predict([[age, sex, bmi, children, smoker, region]])

    # Return the prediction as JSON
    return {'prediction': prediction[0]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

