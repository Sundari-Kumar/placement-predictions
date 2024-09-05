from flask import render_template, request
from app import app
from app.model import predict

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    # Extract features from request form
    features = [float(request.form['feature1']), float(request.form['feature2'])]  # Adjust as needed
    prediction = predict(features)
    return render_template('results.html', prediction=prediction)
