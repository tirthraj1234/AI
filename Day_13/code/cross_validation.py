from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    KFold,
    StratifiedKFold,
    LeaveOneOut
)
from sklearn.metrics import accuracy_score
import numpy as np

# ==========================================================
# CROSS VALIDATION
# ==========================================================

print("=" * 70)
print("CROSS VALIDATION TECHNIQUES")
print("=" * 70)

# ==========================================================
# Step 1 : Load Dataset
# ==========================================================

dataset = load_iris()

X = dataset.data
y = dataset.target

print("\nDataset Loaded Successfully")
print("Number of Samples :", X.shape[0])
print("Number of Features:", X.shape[1])

# ==========================================================
# Step 2 : Create Model
# ==========================================================

model = LogisticRegression(max_iter=500)

# ==========================================================
# Step 3 : Hold-Out Validation
# ==========================================================

print("\n" + "=" * 70)
print("Hold-Out Validation")
print("=" * 70)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

holdout_accuracy = accuracy_score(y_test, y_pred)

print(f"Hold-Out Accuracy : {holdout_accuracy:.4f}")

# ==========================================================
# Step 4 : K-Fold Cross Validation
# ==========================================================

print("\n" + "=" * 70)
print("5-Fold Cross Validation")
print("=" * 70)

kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

kfold_scores = cross_val_score(
    model,
    X,
    y,
    cv=kfold,
    scoring="accuracy"
)

print("Fold Scores :", kfold_scores)
print("Average Accuracy :", round(np.mean(kfold_scores), 4))

# ==========================================================
# Step 5 : Stratified K-Fold
# ==========================================================

print("\n" + "=" * 70)
print("Stratified 5-Fold Cross Validation")
print("=" * 70)

stratified = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

stratified_scores = cross_val_score(
    model,
    X,
    y,
    cv=stratified,
    scoring="accuracy"
)

print("Fold Scores :", stratified_scores)
print("Average Accuracy :", round(np.mean(stratified_scores), 4))

# ==========================================================
# Step 6 : Leave-One-Out Cross Validation
# ==========================================================

print("\n" + "=" * 70)
print("Leave-One-Out Cross Validation")
print("=" * 70)

loo = LeaveOneOut()

loo_scores = cross_val_score(
    model,
    X,
    y,
    cv=loo,
    scoring="accuracy"
)

print("Total Iterations :", len(loo_scores))
print("Average Accuracy :", round(np.mean(loo_scores), 4))

# ==========================================================
# Step 7 : Comparison
# ==========================================================

print("\n" + "=" * 70)
print("Comparison of Validation Techniques")
print("=" * 70)

print(f"Hold-Out Accuracy        : {holdout_accuracy:.4f}")
print(f"K-Fold Accuracy          : {np.mean(kfold_scores):.4f}")
print(f"Stratified K-Fold        : {np.mean(stratified_scores):.4f}")
print(f"LOOCV Accuracy           : {np.mean(loo_scores):.4f}")

# ==========================================================
# Step 8 : Interpretation
# ==========================================================

print("\n" + "=" * 70)
print("Interpretation")
print("=" * 70)

print("""
Hold-Out Validation
- Fast and simple.
- Uses one train-test split.

K-Fold Cross Validation
- Splits data into K equal folds.
- Every sample is used for both training and testing.

Stratified K-Fold
- Maintains class distribution in every fold.
- Best for classification problems.

Leave-One-Out Cross Validation (LOOCV)
- Uses one sample for testing at a time.
- Gives highly reliable evaluation.
- Computationally expensive.
""")

# ==========================================================
# Program Completed
# ==========================================================

print("=" * 70)
print("Cross Validation Completed Successfully!")
print("=" * 70)