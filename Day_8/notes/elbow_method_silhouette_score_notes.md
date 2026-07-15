# Elbow Method & Silhouette Score Notes

## Day 8 – Elbow Method & Silhouette Score

## Introduction

In K-Means Clustering, choosing the correct number of clusters (**K**) is very important. If the value of **K** is too small or too large, the clustering result may not represent the data correctly. Two common techniques used to determine the optimal number of clusters are the **Elbow Method** and the **Silhouette Score**.

---

## Why Choose the Correct Value of K?

The value of **K** determines how many clusters the dataset will be divided into.

- Too few clusters may combine different groups.
- Too many clusters may split similar data into unnecessary groups.
- Choosing the correct value of **K** improves clustering accuracy and quality.

---

## What is WCSS?

**WCSS (Within-Cluster Sum of Squares)** measures the total squared distance between each data point and the centroid of its cluster.

A lower WCSS value indicates that the data points are closer to their centroids, resulting in more compact clusters.

### Formula

```
WCSS = Σ (Distance between Data Point and Centroid)²
```

---

## What is the Elbow Method?

The **Elbow Method** is a technique used to find the optimal number of clusters in K-Means Clustering.

It works by calculating the WCSS for different values of **K** and plotting the results on a graph.

The point where the decrease in WCSS starts slowing down resembles an **elbow**. This point is considered the best value for **K**.

---

## Steps of the Elbow Method

1. Select a range of values for **K** (for example, 1 to 10).
2. Train a K-Means model for each value of **K**.
3. Calculate the WCSS for each model.
4. Plot a graph of **K** versus WCSS.
5. Identify the elbow point.
6. Choose the corresponding value of **K**.

---

## Python Example – Elbow Method

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Age": [22, 25, 47, 52, 46, 56],
    "Income": [20000, 25000, 70000, 75000, 72000, 78000]
})

wcss = []

for k in range(1, 6):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(data)
    wcss.append(model.inertia_)

plt.plot(range(1, 6), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()
```

---

## What is the Silhouette Score?

The **Silhouette Score** measures how well a data point fits within its own cluster compared to other clusters.

It evaluates the quality of clustering by considering both:

- Cohesion (how close data points are within the same cluster)
- Separation (how far clusters are from each other)

---

## Silhouette Score Range

| Score | Meaning |
|--------|---------|
| +1 | Excellent clustering |
| 0 | Overlapping clusters |
| -1 | Incorrect clustering |

A higher Silhouette Score indicates better clustering performance.

---

## Python Example – Silhouette Score

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

data = pd.DataFrame({
    "Age": [22, 25, 47, 52, 46, 56],
    "Income": [20000, 25000, 70000, 75000, 72000, 78000]
})

model = KMeans(n_clusters=2, random_state=42, n_init=10)

labels = model.fit_predict(data)

score = silhouette_score(data, labels)

print("Silhouette Score:", score)
```

---

## Advantages of the Elbow Method

- Simple to understand.
- Helps determine the optimal number of clusters.
- Easy to implement.
- Widely used with K-Means.

---

## Limitations of the Elbow Method

- The elbow point is not always clearly visible.
- Different users may interpret the graph differently.
- Less effective for complex datasets.

---

## Advantages of the Silhouette Score

- Measures clustering quality.
- Considers both cohesion and separation.
- Helps compare different clustering models.
- Easy to interpret.

---

## Limitations of the Silhouette Score

- Can be computationally expensive for large datasets.
- Performance depends on the distance metric used.
- May not perform well for clusters with irregular shapes.

---

## Real-World Applications

The Elbow Method and Silhouette Score are used in:

- Customer Segmentation
- Market Analysis
- Image Segmentation
- Fraud Detection
- Medical Research
- Recommendation Systems
- Social Network Analysis
- Geographic Data Clustering

---

## Key Learnings

Today I learned:

- Why selecting the correct value of **K** is important.
- What WCSS is and how it is calculated.
- How the Elbow Method identifies the optimal number of clusters.
- What the Silhouette Score measures.
- The range and interpretation of the Silhouette Score.
- Advantages and limitations of both evaluation techniques.
- Python implementation using Scikit-learn.

---

## Conclusion

The Elbow Method and Silhouette Score are important techniques for evaluating K-Means Clustering models. The Elbow Method helps determine the optimal number of clusters using WCSS, while the Silhouette Score measures the quality of clustering by evaluating cohesion and separation. Using both techniques together helps build more accurate and reliable clustering models for real-world Machine Learning applications.