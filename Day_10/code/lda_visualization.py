from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

# Plot
plt.figure(figsize=(8, 6))

colors = ["red", "green", "blue"]
labels = iris.target_names

for i, color in enumerate(colors):
    plt.scatter(
        X_lda[y == i, 0],
        X_lda[y == i, 1],
        color=color,
        label=labels[i]
    )

plt.title("LDA Visualization of Iris Dataset")
plt.xlabel("Linear Discriminant 1")
plt.ylabel("Linear Discriminant 2")
plt.legend()
plt.grid(True)
plt.show()