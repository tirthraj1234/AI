# import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# load dataset
df = pd.read_csv("Day_8/dataset/mall_customers.csv")

print(df.head())

# select feature
X = df[["Age", "AnnualIncome"]]

# elbow method - find optimal number of cluster
wcss = []

for k in range(1, 6):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    model.fit(X)
    wcss.append(model.inertia_)

plt.plot(range(1, 6), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# train final model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(X)

# display result
print(df)

print("\nCentroids:")
print(model.cluster_centers_)

# visualize customer segment
plt.figure(figsize=(8,6))

plt.scatter(
    df["Age"],
    df["AnnualIncome"],
    c=df["Cluster"],
    s=80
)

plt.scatter(
    model.cluster_centers_[:,0],
    model.cluster_centers_[:,1],
    marker="X",
    s=250,
    label="Centroids"
)

plt.title("Customer Segmentation")
plt.xlabel("Age")
plt.ylabel("Annual Income")
plt.legend()

plt.show()