# K-Means Clustering Notes

## Day 8 – K-Means Clustering

## What is K-Means Clustering?

K-Means Clustering is one of the most popular **Unsupervised Machine Learning** algorithms. It groups similar data points into **K** clusters, where **K** is the number of clusters chosen before training the model.

The objective of K-Means is to minimize the distance between data points and the centroid of their assigned cluster.

---

## What is a Centroid?

A centroid is the center point of a cluster. It represents the average position of all the data points in that cluster.

During training, the centroid is updated repeatedly until the clusters become stable.

---

## How K-Means Works

The K-Means algorithm follows these steps:

1. Choose the number of clusters (**K**).
2. Randomly initialize **K** centroids.
3. Calculate the distance between each data point and every centroid.
4. Assign each data point to the nearest centroid.
5. Recalculate the centroid of each cluster.
6. Repeat steps 3–5 until the centroids no longer change significantly.

---

## Euclidean Distance

K-Means usually uses **Euclidean Distance** to measure the distance between a data point and a centroid.

### Formula

```
Distance = √((x₂ − x₁)² + (y₂ − y₁)²)
```

The data point is assigned to the cluster with the shortest distance.

---

## Python Example

```python
from sklearn.cluster import KMeans
import pandas as pd

data = pd.DataFrame({
    "Age": [22, 25, 47, 52, 46, 56],
    "Income": [20000, 25000, 70000, 75000, 72000, 78000]
})

model = KMeans(n_clusters=2, random_state=42)

model.fit(data)

print("Cluster Labels:")
print(model.labels_)

print("\nCentroids:")
print(model.cluster_centers_)
```

---

## Advantages

- Simple and easy to understand.
- Fast and efficient for large datasets.
- Easy to implement.
- Works well with well-separated clusters.
- Widely used in customer segmentation and market analysis.

---

## Limitations

- The number of clusters (**K**) must be selected before training.
- Sensitive to outliers.
- Initial centroid selection can affect the final result.
- Performs best with spherical and equally sized clusters.
- May not work well with complex cluster shapes.

---

## Real-World Applications

K-Means Clustering is used in:

- Customer Segmentation
- Market Basket Analysis
- Product Recommendation
- Image Segmentation
- Social Network Analysis
- Document Clustering
- Fraud Detection
- Medical Data Analysis
- Sales and Marketing Analysis

---

## Hyperparameters

Common hyperparameters used in K-Means include:

- **n_clusters** – Number of clusters to create.
- **random_state** – Ensures reproducible results.
- **max_iter** – Maximum number of iterations.
- **n_init** – Number of times the algorithm runs with different centroid initializations.

Example:

```python
model = KMeans(
    n_clusters=3,
    random_state=42,
    max_iter=300,
    n_init=10
)
```

---

## Advantages of K-Means

- Easy to understand and implement.
- Computationally efficient.
- Scales well for large datasets.
- Produces clear and interpretable clusters.
- Suitable for many business applications.

---

## Limitations of K-Means

- Choosing the correct value of **K** is difficult.
- Sensitive to noisy data and outliers.
- Different initial centroids can produce different results.
- Not suitable for clusters with irregular shapes.

---

## Key Learnings

Today I learned:

- What K-Means Clustering is.
- The purpose of centroids.
- How the K-Means algorithm works.
- How Euclidean Distance is used.
- Important K-Means hyperparameters.
- Advantages and limitations of K-Means.
- Real-world applications of K-Means.
- Basic implementation using Scikit-learn.

---

## Conclusion

K-Means Clustering is a simple, fast, and widely used unsupervised learning algorithm for grouping similar data points into clusters. It uses centroids and Euclidean Distance to assign data points to the nearest cluster. K-Means is widely applied in customer segmentation, recommendation systems, image segmentation, and business analytics. Choosing the correct number of clusters and handling outliers properly are important for achieving good clustering performance.