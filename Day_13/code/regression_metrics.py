import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================================================
# REGRESSION EVALUATION METRICS
# ==========================================================

print("=" * 70)
print("REGRESSION EVALUATION METRICS")
print("=" * 70)

# ==========================================================
# Step 1 : Load Dataset
# ==========================================================

dataset = load_diabetes()

X = dataset.data
y = dataset.target

print("\nDataset Loaded Successfully")
print("Number of Samples :", X.shape[0])
print("Number of Features:", X.shape[1])

# ==========================================================
# Step 2 : Split Dataset
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# ==========================================================
# Step 3 : Train Linear Regression Model
# ==========================================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# ==========================================================
# Step 4 : Predictions
# ==========================================================

y_pred = model.predict(X_test)

print("\nPredictions Generated Successfully")

# ==========================================================
# Step 5 : Evaluation Metrics
# ==========================================================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

# ==========================================================
# Step 6 : Adjusted R² Score
# ==========================================================

n = len(y_test)

p = X_test.shape[1]

adjusted_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))

# ==========================================================
# Step 7 : Display Results
# ==========================================================

print("\n" + "=" * 70)
print("Regression Evaluation Metrics")
print("=" * 70)

print(f"Mean Absolute Error (MAE)      : {mae:.2f}")

print(f"Mean Squared Error (MSE)       : {mse:.2f}")

print(f"Root Mean Squared Error (RMSE) : {rmse:.2f}")

print(f"R² Score                       : {r2:.4f}")

print(f"Adjusted R² Score              : {adjusted_r2:.4f}")

# ==========================================================
# Step 8 : Interpretation
# ==========================================================

print("\n" + "=" * 70)
print("Interpretation")
print("=" * 70)

print("""
MAE  -> Average prediction error.

MSE  -> Average squared prediction error.

RMSE -> Error measured in the same unit as the target variable.

R²   -> Percentage of variance explained by the model.

Adjusted R² -> R² adjusted for the number of features.
""")

# ==========================================================
# Program Completed
# ==========================================================

print("=" * 70)
print("Regression Metrics Evaluation Completed Successfully!")
print("=" * 70)