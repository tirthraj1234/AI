# import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# load dataset
df = pd.read_csv("Day_9/dataset/iris.csv")

print(df.head())

# standardize data
scaler = StandardScaler()

X_scaled = scaler.fit_transform(df)

# apply pca
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

# display shape
print("Original Shape:", df.shape)
print("Reduced Shape:", X_pca.shape)

# display explained variance ratio
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# visualize PCA output
plt.figure(figsize=(8,6))

plt.scatter(
    X_pca[:,0],
    X_pca[:,1]
)

plt.title("PCA - Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()

