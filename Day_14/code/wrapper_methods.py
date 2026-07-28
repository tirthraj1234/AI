import pandas as pd

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE, SequentialFeatureSelector

# WRAPPER METHODS FOR FEATURE SELECTION

print("=" * 70)
print("WRAPPER METHODS FOR FEATURE SELECTION")
print("=" * 70)

# Step 1 : Load Dataset

iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

print("\nDataset Loaded Successfully")
print("Number of Samples :", X.shape[0])
print("Number of Features:", X.shape[1])

print("\nOriginal Features")
print(X.columns.tolist())

# Step 2 : Create Model

model = LogisticRegression(max_iter=5000)

# Step 3 : Recursive Feature Elimination (RFE)

print("\n" + "=" * 70)
print("RECURSIVE FEATURE ELIMINATION (RFE)")
print("=" * 70)

rfe = RFE(
    estimator=model,
    n_features_to_select=2
)

rfe.fit(X, y)

print("\nSelected Features:")

selected_rfe = X.columns[rfe.support_]

for feature in selected_rfe:
    print(feature)

print("\nFeature Ranking")

ranking = pd.DataFrame({
    "Feature": X.columns,
    "Rank": rfe.ranking_
})

print(ranking)


# Step 4 : Forward Selection

print("\n" + "=" * 70)
print("FORWARD SELECTION")
print("=" * 70)

forward_selector = SequentialFeatureSelector(
    estimator=model,
    n_features_to_select=2,
    direction="forward",
    cv=5
)

forward_selector.fit(X, y)

forward_features = X.columns[forward_selector.get_support()]

print("\nSelected Features")

for feature in forward_features:
    print(feature)

# Step 5 : Backward Selection

print("\n" + "=" * 70)
print("BACKWARD SELECTION")
print("=" * 70)

backward_selector = SequentialFeatureSelector(
    estimator=model,
    n_features_to_select=2,
    direction="backward",
    cv=5
)

backward_selector.fit(X, y)

backward_features = X.columns[backward_selector.get_support()]

print("\nSelected Features")

for feature in backward_features:
    print(feature)

# Step 6 : Comparison

print("\n" + "=" * 70)
print("FEATURE SELECTION COMPARISON")
print("=" * 70)

comparison = pd.DataFrame({
    "Method": [
        "Recursive Feature Elimination",
        "Forward Selection",
        "Backward Selection"
    ],
    "Selected Features": [
        ", ".join(selected_rfe),
        ", ".join(forward_features),
        ", ".join(backward_features)
    ]
})

print(comparison)

