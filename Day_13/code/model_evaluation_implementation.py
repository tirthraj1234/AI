import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    roc_auc_score
)

# ==========================================================
# COMPLETE MODEL EVALUATION IMPLEMENTATION
# ==========================================================

print("=" * 70)
print("COMPLETE MODEL EVALUATION IMPLEMENTATION")
print("=" * 70)

# ==========================================================
# Step 1 : Load Dataset
# ==========================================================

dataset = load_breast_cancer()

X = dataset.data
y = dataset.target

print("\nDataset Loaded Successfully")
print("Dataset Name       : Breast Cancer Dataset")
print("Number of Samples  :", X.shape[0])
print("Number of Features :", X.shape[1])

# ==========================================================
# Step 2 : Train-Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nDataset Split Completed")
print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================================
# Step 3 : Train Model
# ==========================================================

model = LogisticRegression(max_iter=5000)

model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# ==========================================================
# Step 4 : Prediction
# ==========================================================

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

print("Prediction Completed")

# ==========================================================
# Step 5 : Classification Metrics
# ==========================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

report = classification_report(y_test, y_pred)

tn, fp, fn, tp = cm.ravel()

specificity = tn / (tn + fp)

# ==========================================================
# Step 6 : ROC Curve and AUC Score
# ==========================================================

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

auc = roc_auc_score(y_test, y_prob)

# ==========================================================
# Step 7 : Cross Validation
# ==========================================================

cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

cv_accuracy = np.mean(cv_scores)

# ==========================================================
# Step 8 : Display Evaluation Metrics
# ==========================================================

print("\n" + "=" * 70)
print("CLASSIFICATION METRICS")
print("=" * 70)

print(f"Accuracy      : {accuracy:.4f}")
print(f"Precision     : {precision:.4f}")
print(f"Recall        : {recall:.4f}")
print(f"F1 Score      : {f1:.4f}")
print(f"Specificity   : {specificity:.4f}")
print(f"AUC Score     : {auc:.4f}")

# ==========================================================
# Step 9 : Confusion Matrix
# ==========================================================

print("\n" + "=" * 70)
print("CONFUSION MATRIX")
print("=" * 70)

print(cm)

print("\nTrue Positive  :", tp)
print("True Negative  :", tn)
print("False Positive :", fp)
print("False Negative :", fn)

# ==========================================================
# Step 10 : Classification Report
# ==========================================================

print("\n" + "=" * 70)
print("CLASSIFICATION REPORT")
print("=" * 70)

print(report)

# ==========================================================
# Step 11 : Cross Validation Result
# ==========================================================

print("\n" + "=" * 70)
print("CROSS VALIDATION")
print("=" * 70)

print("Cross Validation Scores :")

for i, score in enumerate(cv_scores, start=1):
    print(f"Fold {i} : {score:.4f}")

print(f"\nAverage Accuracy : {cv_accuracy:.4f}")

# ==========================================================
# Step 12 : Plot ROC Curve
# ==========================================================

plt.figure(figsize=(8,6))

plt.plot(
    fpr,
    tpr,
    color="blue",
    linewidth=2,
    label=f"ROC Curve (AUC = {auc:.4f})"
)

plt.plot(
    [0,1],
    [0,1],
    linestyle="--",
    color="red",
    label="Random Classifier"
)

plt.title("Receiver Operating Characteristic (ROC) Curve")

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.legend()

plt.grid(True)

plt.show()

# ==========================================================
# Step 13 : Final Performance Summary
# ==========================================================

print("\n" + "=" * 70)
print("FINAL MODEL PERFORMANCE SUMMARY")
print("=" * 70)

print(f"""
Dataset                 : Breast Cancer Dataset

Algorithm               : Logistic Regression

Training Samples        : {len(X_train)}

Testing Samples         : {len(X_test)}

Accuracy                : {accuracy:.4f}

Precision               : {precision:.4f}

Recall                  : {recall:.4f}

F1 Score                : {f1:.4f}

Specificity             : {specificity:.4f}

ROC AUC Score           : {auc:.4f}

Cross Validation Score  : {cv_accuracy:.4f}
""")

# ==========================================================
# Step 14 : Interpretation
# ==========================================================

print("=" * 70)
print("MODEL INTERPRETATION")
print("=" * 70)

print("""
This evaluation pipeline demonstrates a complete workflow
for evaluating a Machine Learning classification model.

The model was evaluated using:

✔ Accuracy

✔ Precision

✔ Recall

✔ F1 Score

✔ Specificity

✔ Confusion Matrix

✔ Classification Report

✔ ROC Curve

✔ AUC Score

✔ 5-Fold Cross Validation

Using multiple evaluation metrics provides a more reliable
understanding of the model's performance than relying on
Accuracy alone.
""")

# ==========================================================
# Program Completed
# ==========================================================

print("=" * 70)
print("COMPLETE MODEL EVALUATION IMPLEMENTATION COMPLETED")
print("=" * 70)