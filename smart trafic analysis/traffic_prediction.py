# Smart Traffic Analysis & Congestion Prediction
# Import Libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# Load Dataset
df = pd.read_csv('smart_traffic_management_dataset.csv')


# Convert Timestamp to Datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])


# Create Hour Column
df['hour'] = df['timestamp'].dt.hour


# Create Congestion Level Column
df['congestion_level'] = pd.cut(
    df['traffic_volume'],
    bins=[0, 300, 700, 1000],
    labels=['Low', 'Medium', 'High']
)


# Select Features and Target
X = df[['hour', 'temperature', 'humidity']]
y = df['traffic_volume']


# Split Dataset into Training and Testing Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create and Train Model
model = LinearRegression()
model.fit(X_train, y_train)


# Make Predictions
y_pred = model.predict(X_test)


# Evaluate Model
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))


# Predict Future Traffic Volume
prediction = model.predict([[18, 30, 70]])

print("Predicted Traffic Volume:", prediction[0])
# Save Model
import joblib

joblib.dump(model, 'traffic_model.pkl')

print("Model Saved Successfully")
import matplotlib.pyplot as plt

#prediction vs actual graph

plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Traffic Volume")
plt.ylabel("Predicted Traffic Volume")
plt.title("Actual vs Predicted Traffic Volume")
plt.show()

# Save Actual vs Predicted values

prediction_df = pd.DataFrame({
    'Actual_Traffic': y_test,
    'Predicted_Traffic': y_pred
})

prediction_df.to_csv('traffic_predictions.csv', index=False)

print("Prediction CSV Saved")