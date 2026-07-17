from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Reconstruct data
X_reconstructed = pca.inverse_transform(X_pca)

# Calculate reconstruction error
error = np.mean((X_scaled - X_reconstructed) ** 2)

print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nCumulative Explained Variance:")
print(np.sum(pca.explained_variance_ratio_))

print("\nReconstruction Error:")
print(error)