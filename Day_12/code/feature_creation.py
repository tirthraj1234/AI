import pandas as pd

# Sample Dataset
data = {
    "Height_m": [1.70, 1.65, 1.80],
    "Weight_kg": [65, 55, 80],
    "Quantity": [2, 5, 3],
    "Unit_Price": [100, 50, 120]
}

df = pd.DataFrame(data)

# Create BMI Feature
df["BMI"] = df["Weight_kg"] / (df["Height_m"] ** 2)

# Create Total Price Feature
df["Total_Price"] = df["Quantity"] * df["Unit_Price"]

print(df)