from sklearn.cluster import KMeans
import pandas as pd

# Sample data
data = pd.DataFrame({
    "Age": [22, 25, 47, 52, 46, 56],
    "Income": [20000, 25000, 70000, 75000, 72000, 78000]
})

# Create K-Means model
model = KMeans(n_clusters=2, random_state=42)

# Train model
model.fit(data)

# Cluster labels
print("Cluster Labels:")
print(model.labels_)

# Centroids
print("\nCentroids:")
print(model.cluster_centers_)