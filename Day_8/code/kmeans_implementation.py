# import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# load dataset
df = pd.read_csv("Day_8/dataset/customer_data.csv")

print(df.head())

# select feature
X = df[["Age", "AnnualIncome"]]

# create K-means model
model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

# train the model
model.fit(X)

# assign cluster labels
df["Cluster"] = model.labels_

print(df)

# display centroids
print("Centroids:")
print(model.cluster_centers_)

# visualize the cluster
plt.figure(figsize=(8, 6))

plt.scatter(
    df["Age"],
    df["AnnualIncome"],
    c=df["Cluster"]
)

plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Age")
plt.ylabel("Annual Income")
plt.legend()

plt.show()

