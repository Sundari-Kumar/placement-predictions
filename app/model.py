import joblib
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Prepare SMOTE instance
smote = SMOTE(random_state=42)

def predict(features):
    features = pd.DataFrame([features], columns=['feature1', 'feature2'])  # Adjust as needed
    features = scaler.transform(features)
    prediction = model.predict(features)
    return 'Class 1' if prediction[0] == 1 else 'Class 0'
