from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ==========================================================
# CLASSIFICATION EVALUATION METRICS
# ==========================================================

print("=" * 70)
print("CLASSIFICATION EVALUATION METRICS")
print("=" * 70)

# ==========================================================
# Step 1 : Load Dataset
# ==========================================================

dataset = load_breast_cancer()

X = dataset.data
y = dataset.target

print("\nDataset Loaded Successfully")
print("Number of Samples :", X.shape[0])
print("Number of Features:", X.shape[1])

# ==========================================================
# Step 2 : Split Dataset
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# ==========================================================
# Step 3 : Train Logistic Regression Model
# ==========================================================

model = LogisticRegression(max_iter=5000)

model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# ==========================================================
# Step 4 : Make Predictions
# ==========================================================

y_pred = model.predict(X_test)

print("\nPredictions Generated Successfully")

# ==========================================================
# Step 5 : Calculate Evaluation Metrics
# ==========================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

report = classification_report(y_test, y_pred)

# ==========================================================
# Step 6 : Calculate Specificity
# ==========================================================

tn, fp, fn, tp = cm.ravel()

specificity = tn / (tn + fp)

# ==========================================================
# Step 7 : Display Results
# ==========================================================

print("\n" + "=" * 70)
print("Classification Evaluation Metrics")
print("=" * 70)

print(f"Accuracy    : {accuracy:.4f}")
print(f"Precision   : {precision:.4f}")
print(f"Recall      : {recall:.4f}")
print(f"F1-Score    : {f1:.4f}")
print(f"Specificity : {specificity:.4f}")

# ==========================================================
# Step 8 : Confusion Matrix
# ==========================================================

print("\n" + "=" * 70)
print("Confusion Matrix")
print("=" * 70)

print(cm)

print("\nValues:")

print(f"True Positives (TP) : {tp}")
print(f"True Negatives (TN) : {tn}")
print(f"False Positives(FP) : {fp}")
print(f"False Negatives(FN) : {fn}")

# ==========================================================
# Step 9 : Classification Report
# ==========================================================

print("\n" + "=" * 70)
print("Classification Report")
print("=" * 70)

print(report)

# ==========================================================
# Step 10 : Interpretation
# ==========================================================

print("=" * 70)
print("Interpretation")
print("=" * 70)

print("""
Accuracy    -> Overall percentage of correct predictions.

Precision   -> Out of all predicted positive cases,
               how many were actually positive.

Recall      -> Out of all actual positive cases,
               how many were correctly identified.

F1-Score    -> Harmonic mean of Precision and Recall.

Specificity -> Ability to correctly identify negative cases.

Confusion Matrix -> Shows TP, TN, FP and FN.

Classification Report -> Displays Precision,
Recall, F1-Score and Support for each class.
""")

# ==========================================================
# Program Completed
# ==========================================================

print("=" * 70)
print("Classification Metrics Evaluation Completed Successfully!")
print("=" * 70)