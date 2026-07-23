import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split

# ==========================================================
# ROC CURVE AND AUC SCORE
# ==========================================================

print("=" * 70)
print("ROC CURVE AND AUC SCORE")
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
# Step 4 : Predict Probabilities
# ==========================================================

y_prob = model.predict_proba(X_test)[:, 1]

print("\nPrediction Probabilities Generated")

# ==========================================================
# Step 5 : Calculate ROC Curve
# ==========================================================

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# ==========================================================
# Step 6 : Calculate AUC Score
# ==========================================================

auc_score = roc_auc_score(y_test, y_prob)

print("\n" + "=" * 70)
print("ROC-AUC RESULT")
print("=" * 70)

print(f"AUC Score : {auc_score:.4f}")

# ==========================================================
# Step 7 : Plot ROC Curve
# ==========================================================

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"ROC Curve (AUC = {auc_score:.4f})",
    linewidth=2
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Classifier"
)

plt.title("Receiver Operating Characteristic (ROC) Curve")

plt.xlabel("False Positive Rate (FPR)")

plt.ylabel("True Positive Rate (TPR)")

plt.legend(loc="lower right")

plt.grid(True)

plt.show()

# ==========================================================
# Step 8 : Interpretation
# ==========================================================

print("\n" + "=" * 70)
print("Interpretation")
print("=" * 70)

print("""
ROC Curve:
Shows the relationship between
True Positive Rate (TPR)
and False Positive Rate (FPR).

AUC Score Interpretation

1.00  -> Perfect Classifier

0.90 - 0.99 -> Excellent Model

0.80 - 0.89 -> Good Model

0.70 - 0.79 -> Fair Model

0.60 - 0.69 -> Poor Model

0.50 -> Random Guessing
""")

# ==========================================================
# Program Completed
# ==========================================================

print("=" * 70)
print("ROC Curve and AUC Evaluation Completed Successfully!")
print("=" * 70)