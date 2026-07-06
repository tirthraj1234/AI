import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np

# Read Dataset
df = pd.read_csv("Day_1/dataset/salary_data.csv")

print(df)

# Features (Input)
X = df[["Experience"]]

# Target (Output)
y = df["Salary"]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Salary
prediction = model.predict([[12]])

print("Predicted Salary for 12 Years Experience:", prediction[0])

# Draw Graph
plt.scatter(X, y, color="blue", label="Actual Data")

plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.legend()

plt.grid(True)

plt.show()

y_pred = model.predict(X)

mae = mean_absolute_error(y, y_pred)
print("Mean Absolute Error (MAE):", mae)

mse = mean_squared_error(y, y_pred)
print("Mean Squared Error (MSE):", mse)

rmse = np.sqrt(mse)
print("Root Mean Squared Error (RMSE):", rmse)

r2 = r2_score(y, y_pred)
print("R² Score:", r2)

