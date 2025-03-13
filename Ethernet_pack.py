import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
file_path = "J:\SIH\NIDS-master\NIDS-master\pck.csv"  # Update if needed
df = pd.read_csv(file_path)

# Handle missing values
df.fillna(0, inplace=True)

# Encode categorical columns
label_encoders = {}
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Split features and labels
X = df.drop(columns=['Label'])  # Assuming 'Label' is the target column
y = df['Label']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a RandomForest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Function to predict new data
def predict_intrusion(new_data):
    new_data_df = pd.DataFrame([new_data], columns=X.columns)
    new_data_scaled = scaler.transform(new_data_df)
    prediction = clf.predict(new_data_scaled)
    return label_encoders['Label'].inverse_transform(prediction)[0]

# Example usage:
# new_packet = {<feature_values_here>}
# print(predict_intrusion(new_packet))
