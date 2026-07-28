import pandas as pd

from sklearn.datasets import load_iris
from sklearn.feature_selection import (
    VarianceThreshold,
    SelectKBest,
    chi2,
    f_classif,
    mutual_info_classif
)

# FILTER METHODS FOR FEATURE SELECTION

print("=" * 70)
print("FILTER METHODS FOR FEATURE SELECTION")
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

# Step 2 : Variance Threshold

print("\n" + "=" * 70)
print("VARIANCE THRESHOLD")
print("=" * 70)

variance_selector = VarianceThreshold(threshold=0.2)

X_variance = variance_selector.fit_transform(X)

selected_variance = X.columns[variance_selector.get_support()]

print("\nSelected Features")

for feature in selected_variance:
    print(feature)

print("\nNumber of Selected Features :", len(selected_variance))

# Step 3 : Correlation Matrix

print("\n" + "=" * 70)
print("CORRELATION MATRIX")
print("=" * 70)

correlation_matrix = X.corr()

print(correlation_matrix)

print("\nHighly Correlated Features (Threshold = 0.80)")

threshold = 0.80

for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        correlation = correlation_matrix.iloc[i, j]

        if abs(correlation) > threshold:
            print(
                f"{correlation_matrix.columns[i]}  <-->  "
                f"{correlation_matrix.columns[j]} : "
                f"{correlation:.2f}"
            )

# Step 4 : Chi-Square Test

print("\n" + "=" * 70)
print("CHI-SQUARE TEST")
print("=" * 70)

chi_selector = SelectKBest(score_func=chi2, k=2)

chi_selector.fit(X, y)

chi_scores = chi_selector.scores_

chi_result = pd.DataFrame({
    "Feature": X.columns,
    "Chi-Square Score": chi_scores
})

chi_result = chi_result.sort_values(
    by="Chi-Square Score",
    ascending=False
)

print(chi_result)

# Step 5 : ANOVA F-Test

print("\n" + "=" * 70)
print("ANOVA F-TEST")
print("=" * 70)

anova_selector = SelectKBest(score_func=f_classif, k=2)

anova_selector.fit(X, y)

anova_scores = anova_selector.scores_

anova_result = pd.DataFrame({
    "Feature": X.columns,
    "F-Score": anova_scores
})

anova_result = anova_result.sort_values(
    by="F-Score",
    ascending=False
)

print(anova_result)

# Step 6 : Mutual Information

print("\n" + "=" * 70)
print("MUTUAL INFORMATION")
print("=" * 70)

mi_scores = mutual_info_classif(
    X,
    y,
    random_state=42
)

mi_result = pd.DataFrame({
    "Feature": X.columns,
    "Mutual Information": mi_scores
})

mi_result = mi_result.sort_values(
    by="Mutual Information",
    ascending=False
)

print(mi_result)

# Step 7 : Comparison

print("\n" + "=" * 70)
print("FEATURE SELECTION COMPARISON")
print("=" * 70)

comparison = pd.DataFrame({
    "Feature": X.columns,
    "Chi-Square": chi_scores,
    "ANOVA F": anova_scores,
    "Mutual Information": mi_scores
})

print(comparison)

# Step 8 : Best Features

print("\n" + "=" * 70)
print("TOP FEATURES")
print("=" * 70)

print("\nTop Features using Chi-Square")

print(
    chi_result.head(2).to_string(index=False)
)

print("\nTop Features using ANOVA")

print(
    anova_result.head(2).to_string(index=False)
)

print("\nTop Features using Mutual Information")

print(
    mi_result.head(2).to_string(index=False)
)

# Program Completed

print("\n" + "=" * 70)
print("FILTER METHODS IMPLEMENTATION COMPLETED SUCCESSFULLY")
print("=" * 70)