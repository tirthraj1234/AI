import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

# ==========================================================
# FEATURE ENGINEERING IMPLEMENTATION
# ==========================================================

print("=" * 70)
print("FEATURE ENGINEERING IMPLEMENTATION")
print("=" * 70)

# ==========================================================
# Step 1: Create Sample Dataset
# ==========================================================

data = {
    "Age": [25, 30, 35, 40, 45],
    "Height": [1.70, 1.65, 1.80, 1.75, 1.68],
    "Weight": [65, 55, 80, 75, 68],
    "Quantity": [2, 5, 3, 4, 6],
    "Unit_Price": [100, 50, 120, 150, 80],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Purchased": [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset\n")
print(df)

# ==========================================================
# Step 2: Feature Creation
# ==========================================================

print("\n" + "=" * 70)
print("Step 2 : Feature Creation")
print("=" * 70)

# BMI Feature
df["BMI"] = df["Weight"] / (df["Height"] ** 2)

# Total Price Feature
df["Total_Price"] = df["Quantity"] * df["Unit_Price"]

print(df)

# ==========================================================
# Step 3: Feature Transformation
# ==========================================================

print("\n" + "=" * 70)
print("Step 3 : Feature Transformation")
print("=" * 70)

# Log Transformation
df["Log_Total_Price"] = np.log1p(df["Total_Price"])

print(df[["Total_Price", "Log_Total_Price"]])

# ==========================================================
# Step 4: Feature Encoding
# ==========================================================

print("\n" + "=" * 70)
print("Step 4 : Feature Encoding")
print("=" * 70)

encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])

print(df)

# ==========================================================
# Step 5: Feature Selection
# ==========================================================

print("\n" + "=" * 70)
print("Step 5 : Feature Selection")
print("=" * 70)

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

selector = SelectKBest(score_func=f_classif, k=5)

X_selected = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]

print("Selected Features:\n")

for feature in selected_features:
    print(feature)

# ==========================================================
# Step 6: Final Dataset
# ==========================================================

print("\n" + "=" * 70)
print("Step 6 : Final Dataset")
print("=" * 70)

final_dataset = df[selected_features.tolist() + ["Purchased"]]

print(final_dataset)

# ==========================================================
# Program Completed
# ==========================================================

print("\n" + "=" * 70)
print("Feature Engineering Pipeline Completed Successfully!")
print("=" * 70)

print("""
Pipeline Steps Performed

1. Dataset Loading
2. Feature Creation
3. Feature Transformation
4. Feature Encoding
5. Feature Selection
6. Final Dataset Preparation

The dataset is now ready for Machine Learning model training.
""")