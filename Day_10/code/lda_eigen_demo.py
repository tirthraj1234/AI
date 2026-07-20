from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_lda.shape)

print("Explained Variance Ratio:")
print(lda.explained_variance_ratio_)