import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.ensemble import RandomForestClassifier

# ==========================================================
# Load Dataset
# ==========================================================

iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print("=" * 60)
print("Original Dataset")
print("=" * 60)
print(X.head())

# ==========================================================
# 1. Correlation Matrix
# ==========================================================

print("\n" + "=" * 60)
print("1. Correlation Matrix")
print("=" * 60)

correlation = X.corr()
print(correlation)

# ==========================================================
# 2. Filter Method (SelectKBest)
# ==========================================================

print("\n" + "=" * 60)
print("2. Filter Method - SelectKBest")
print("=" * 60)

selector = SelectKBest(score_func=f_classif, k=2)

X_selected = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]

print("Selected Features:")
for feature in selected_features:
    print(feature)

# ==========================================================
# 3. Wrapper Method (Recursive Feature Elimination)
# ==========================================================

print("\n" + "=" * 60)
print("3. Wrapper Method - Recursive Feature Elimination")
print("=" * 60)

model = RandomForestClassifier(random_state=42)

rfe = RFE(
    estimator=model,
    n_features_to_select=2
)

rfe.fit(X, y)

print("Selected Features:")
for feature, selected in zip(X.columns, rfe.support_):
    if selected:
        print(feature)

# ==========================================================
# 4. Embedded Method (Random Forest Feature Importance)
# ==========================================================

print("\n" + "=" * 60)
print("4. Embedded Method - Feature Importance")
print("=" * 60)

model.fit(X, y)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

# ==========================================================
# Summary
# ==========================================================

print("\n" + "=" * 60)
print("Feature Selection Review Completed Successfully!")
print("=" * 60)

print("""
Techniques Demonstrated:

1. Correlation Matrix
2. Filter Method (SelectKBest)
3. Wrapper Method (RFE)
4. Embedded Method (Random Forest Feature Importance)
""")