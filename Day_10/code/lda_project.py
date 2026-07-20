from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Standardize Features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)

X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# Train Logistic Regression
model = LogisticRegression(random_state=42)

model.fit(X_train_lda, y_train)

# Prediction
y_pred = model.predict(X_test_lda)

# Evaluation
print("=" * 50)
print("Accuracy Score")
print("=" * 50)
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print("=" * 50)
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print("=" * 50)
print(classification_report(y_test, y_pred))

# Visualization
plt.figure(figsize=(8,6))

colors = ['red', 'green', 'blue']
labels = iris.target_names

for i, color in enumerate(colors):
    plt.scatter(
        X_train_lda[y_train == i, 0],
        X_train_lda[y_train == i, 1],
        color=color,
        label=labels[i]
    )

plt.title("LDA - Iris Flower Classification")
plt.xlabel("Linear Discriminant 1")
plt.ylabel("Linear Discriminant 2")
plt.legend()
plt.grid(True)

plt.savefig("../images/lda_scatter_plot.png")

plt.show()