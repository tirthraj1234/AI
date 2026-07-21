from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# PCA Model
pca = PCA(
    n_components=2,
    svd_solver="auto",
    whiten=False,
    random_state=42
)

# LDA Model
lda = LinearDiscriminantAnalysis(
    n_components=2,
    solver="svd",
    tol=1e-4
)

print("PCA Hyperparameters")
print(pca)

print("\nLDA Hyperparameters")
print(lda)