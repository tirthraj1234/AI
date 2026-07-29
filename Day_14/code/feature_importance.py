import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


# FEATURE IMPORTANCE USING RANDOM FOREST


print("=" * 70)
print("FEATURE IMPORTANCE & VISUALIZATION")
print("=" * 70)


# Step 1 : Load Dataset


iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

print("\nDataset Loaded Successfully")
print("Samples :", X.shape[0])
print("Features:", X.shape[1])


# Step 2 : Train Random Forest Model


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print("\nRandom Forest Model Trained Successfully.")


# Step 3 : Extract Feature Importance


importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance Scores")
print(feature_importance)


# Step 4 : Rank Features


feature_importance["Rank"] = range(
    1,
    len(feature_importance) + 1
)

print("\nRanked Features")
print(feature_importance)


# Step 5 : Display Top Features


print("\nTop 3 Important Features")

print(
    feature_importance.head(3).to_string(index=False)
)


# Step 6 : Plot Feature Importance


plt.figure(figsize=(8, 5))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.title("Feature Importance using Random Forest")

plt.xlabel("Features")

plt.ylabel("Importance Score")

plt.xticks(rotation=20)

plt.tight_layout()

plt.show()


# Step 7 : Horizontal Bar Chart


plt.figure(figsize=(8, 5))

plt.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.title("Feature Importance (Horizontal Bar Chart)")

plt.xlabel("Importance Score")

plt.ylabel("Features")

plt.tight_layout()

plt.show()
