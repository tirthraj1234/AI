import pandas as pd

from sklearn.datasets import load_iris
from sklearn.linear_model import Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


# EMBEDDED METHODS FOR FEATURE SELECTION


print("=" * 70)
print("EMBEDDED METHODS FOR FEATURE SELECTION")
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

print("\nOriginal Features")
print(X.columns.tolist())


# Step 2 : Feature Scaling


scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# Step 3 : Lasso Regression


print("\n" + "=" * 70)
print("LASSO REGRESSION")
print("=" * 70)

lasso = Lasso(alpha=0.01)

lasso.fit(X_scaled, y)

lasso_result = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": lasso.coef_
})

print(lasso_result)

selected_lasso = lasso_result[
    lasso_result["Coefficient"] != 0
]

print("\nSelected Features (Lasso)")
print(selected_lasso)


# Step 4 : Ridge Regression


print("\n" + "=" * 70)
print("RIDGE REGRESSION")
print("=" * 70)

ridge = Ridge(alpha=1.0)

ridge.fit(X_scaled, y)

ridge_result = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": ridge.coef_
})

print(ridge_result)


# Step 5 : Elastic Net


print("\n" + "=" * 70)
print("ELASTIC NET")
print("=" * 70)

elastic = ElasticNet(
    alpha=0.01,
    l1_ratio=0.5,
    max_iter=5000
)

elastic.fit(X_scaled, y)

elastic_result = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": elastic.coef_
})

print(elastic_result)

selected_elastic = elastic_result[
    elastic_result["Coefficient"] != 0
]

print("\nSelected Features (Elastic Net)")
print(selected_elastic)


# Step 6 : Decision Tree Feature Importance


print("\n" + "=" * 70)
print("DECISION TREE FEATURE IMPORTANCE")
print("=" * 70)

tree = DecisionTreeClassifier(random_state=42)

tree.fit(X, y)

tree_result = pd.DataFrame({
    "Feature": X.columns,
    "Importance": tree.feature_importances_
})

tree_result = tree_result.sort_values(
    by="Importance",
    ascending=False
)

print(tree_result)


# Step 7 : Random Forest Feature Importance


print("\n" + "=" * 70)
print("RANDOM FOREST FEATURE IMPORTANCE")
print("=" * 70)

forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

forest.fit(X, y)

forest_result = pd.DataFrame({
    "Feature": X.columns,
    "Importance": forest.feature_importances_
})

forest_result = forest_result.sort_values(
    by="Importance",
    ascending=False
)

print(forest_result)


# Step 8 : Comparison


print("\n" + "=" * 70)
print("FEATURE IMPORTANCE COMPARISON")
print("=" * 70)

comparison = pd.DataFrame({
    "Feature": X.columns,
    "Lasso": lasso.coef_,
    "Ridge": ridge.coef_,
    "ElasticNet": elastic.coef_,
    "Decision Tree": tree.feature_importances_,
    "Random Forest": forest.feature_importances_
})

print(comparison)


# Step 9 : Top Features

print("\n" + "=" * 70)
print("TOP FEATURES (RANDOM FOREST)")
print("=" * 70)

print(
    forest_result.head(3).to_string(index=False)
)

