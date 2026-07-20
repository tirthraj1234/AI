from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create LDA model
lda = LinearDiscriminantAnalysis(
    n_components=2,
    solver="svd"
)

# Transform data
X_lda = lda.fit_transform(X, y)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_lda.shape)