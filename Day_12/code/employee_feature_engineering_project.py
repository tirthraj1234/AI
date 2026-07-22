import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

print("=" * 70)
print("EMPLOYEE FEATURE ENGINEERING PROJECT")
print("=" * 70)

# ==========================================================
# Step 1 : Create Sample Employee Dataset
# ==========================================================

data = {
    "Age": [25, 30, 35, 40, 45, 28, 32, 38],
    "Experience": [2, 5, 8, 12, 18, 3, 7, 10],
    "Education": [
        "Bachelor",
        "Master",
        "Bachelor",
        "PhD",
        "Master",
        "Bachelor",
        "Master",
        "PhD"
    ],
    "Department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "HR",
        "Finance",
        "IT",
        "HR"
    ],
    "Gender": [
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female"
    ],
    "Salary": [
        35000,
        50000,
        65000,
        85000,
        110000,
        42000,
        60000,
        90000
    ]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset\n")
print(df)

# ==========================================================
# Step 2 : Data Cleaning
# ==========================================================

print("\n" + "=" * 70)
print("Step 2 : Data Cleaning")
print("=" * 70)

df = df.drop_duplicates()
df = df.fillna(method="ffill")

print("Missing Values\n")
print(df.isnull().sum())

# ==========================================================
# Step 3 : Feature Creation
# ==========================================================

print("\n" + "=" * 70)
print("Step 3 : Feature Creation")
print("=" * 70)

# Experience Level
df["Experience_Level"] = pd.cut(
    df["Experience"],
    bins=[0, 3, 7, 50],
    labels=["Junior", "Mid", "Senior"]
)

# Salary Category
df["Salary_Category"] = pd.cut(
    df["Salary"],
    bins=[0, 50000, 80000, 200000],
    labels=["Low", "Medium", "High"]
)

# Experience Score
df["Experience_Score"] = df["Experience"] * 10

print(df)

# ==========================================================
# Step 4 : Feature Transformation
# ==========================================================

print("\n" + "=" * 70)
print("Step 4 : Feature Transformation")
print("=" * 70)

df["Log_Salary"] = np.log1p(df["Salary"])

print(df[["Salary", "Log_Salary"]])

# ==========================================================
# Step 5 : Feature Encoding
# ==========================================================

print("\n" + "=" * 70)
print("Step 5 : Feature Encoding")
print("=" * 70)

encoder = LabelEncoder()

columns = [
    "Education",
    "Department",
    "Gender",
    "Experience_Level",
    "Salary_Category"
]

for column in columns:
    df[column] = encoder.fit_transform(df[column])

print(df)

# ==========================================================
# Step 6 : Feature Selection
# ==========================================================

print("\n" + "=" * 70)
print("Step 6 : Feature Selection")
print("=" * 70)

X = df.drop("Salary", axis=1)
y = df["Salary_Category"]

selector = SelectKBest(score_func=f_classif, k=5)

X_new = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]

print("Selected Features\n")

for feature in selected_features:
    print(feature)

# ==========================================================
# Step 7 : Final Dataset
# ==========================================================

print("\n" + "=" * 70)
print("Step 7 : Final Dataset")
print("=" * 70)

final_dataset = df[selected_features.tolist() + ["Salary_Category"]]

print(final_dataset)

# ==========================================================
# Project Completed
# ==========================================================

print("\n" + "=" * 70)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 70)

print("""
Employee Feature Engineering Pipeline Completed

Pipeline Covered

1. Dataset Loading
2. Data Cleaning
3. Feature Creation
4. Feature Transformation
5. Feature Encoding
6. Feature Selection
7. Final Dataset Preparation

Dataset is now ready for Machine Learning Model Training.
""")