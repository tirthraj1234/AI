from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

# Display shapes
print("=" * 50)
print("Original Dataset Shape :", X.shape)

print("\nPCA Transformed Shape :", X_pca.shape)

print("\nLDA Transformed Shape :", X_lda.shape)

# Display first five rows
print("\nFirst 5 PCA Components")
print(X_pca[:5])

print("\nFirst 5 LDA Components")
print(X_lda[:5])