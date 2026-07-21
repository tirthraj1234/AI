import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

colors = ['red', 'green', 'blue']
labels = iris.target_names

# PCA Scatter Plot
plt.figure(figsize=(8,6))

for i, color in enumerate(colors):
    plt.scatter(
        X_pca[y == i, 0],
        X_pca[y == i, 1],
        color=color,
        label=labels[i]
    )

plt.title("PCA Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)

plt.show()

# LDA Scatter Plot
plt.figure(figsize=(8,6))

for i, color in enumerate(colors):
    plt.scatter(
        X_lda[y == i, 0],
        X_lda[y == i, 1],
        color=color,
        label=labels[i]
    )

plt.title("LDA Visualization")
plt.xlabel("Linear Discriminant 1")
plt.ylabel("Linear Discriminant 2")
plt.legend()
plt.grid(True)
plt.show()