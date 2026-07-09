import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = {
    "Experience": [2, 5, 7, 10, 3, 8],
    "Performance": [3, 5, 4, 5, 2, 5],
    "Age": [25, 30, 35, 40, 28, 38],
    "Promotion": [0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["Experience", "Performance", "Age"]]
y = df["Promotion"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(f"{feature}: {score:.3f}")