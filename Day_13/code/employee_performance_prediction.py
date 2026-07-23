import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
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

# ======================================================
# EMPLOYEE PERFORMANCE PREDICTION
# ======================================================

print("=" * 70)
print("EMPLOYEE PERFORMANCE PREDICTION")
print("=" * 70)

# Load Dataset
data = pd.read_csv("../dataset/employee_performance.csv")

print("\nDataset Loaded Successfully")
print(data.head())

# Encode Categorical Columns
encoder = LabelEncoder()

categorical_columns = [
    "Education_Level",
    "Department",
    "Overtime",
    "Performance"
]

for column in categorical_columns:
    data[column] = encoder.fit_transform(data[column])

# Features and Target
X = data.drop(["Employee_ID", "Performance"], axis=1)
y = data["Performance"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train Model
model = LogisticRegression(max_iter=5000)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

tn, fp, fn, tp = cm.ravel()
specificity = tn / (tn + fp)

# ROC-AUC
fpr, tpr, threshold = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)

# Cross Validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

# Results
print("\nAccuracy :", accuracy)
print("Precision :", precision)
print("Recall :", recall)
print("F1 Score :", f1)
print("Specificity :", specificity)
print("ROC AUC :", auc)

print("\nConfusion Matrix")
print(cm)

print("\nClassification Report")
print(report)

print("\nCross Validation Scores")
print(scores)

print("\nAverage Accuracy :", np.mean(scores))

# ROC Curve
plt.figure(figsize=(8,6))

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {auc:.2f}",
    linewidth=2
)

plt.plot([0,1],[0,1],"r--")

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.grid()

plt.show()

print("="*70)
print("PROJECT COMPLETED SUCCESSFULLY")
print("="*70)