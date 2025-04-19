import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load the simulated data
df = pd.read_csv('data/simulated_cost_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Feature Engineering
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['dayofweek'] = df['date'].dt.dayofweek

# Lag features
df['cost_lag1'] = df['cost'].shift(1)
df['cost_lag7'] = df['cost'].shift(7)

# Remove rows with NaN values from lagging
df = df.dropna()

# Define features and target
X = df[['day', 'month', 'dayofweek', 'cost_lag1', 'cost_lag7']]
y = df['cost']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions
preds = model.predict(X_test)

# Calculate and print RMSE
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE:", rmse)

# Save model
joblib.dump(model, 'models/cost_predictor.joblib')
