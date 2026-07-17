from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data

# Configure PCA
pca = PCA(
    n_components=2,
    svd_solver="auto",
    whiten=False
)

# Transform data
X_pca = pca.fit_transform(X)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)