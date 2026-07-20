from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load dataset 
iris = load_iris()
X = iris.data

# Apply PCA
pca = PCA()
pca.fit(X)

# Explained Variance Ratio
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Scree Plot
plt.plot(
    range(1, len(pca.explained_variance_ratio_) + 1),
    pca.explained_variance_ratio_,
    marker="o"
)

plt.title("Scree Plot")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")

plt.show()