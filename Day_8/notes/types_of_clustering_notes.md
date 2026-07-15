# Types of Clustering Notes

## Day 8 – Types of Clustering

## What are the Types of Clustering?

Clustering algorithms group similar data points based on their characteristics. Different clustering methods use different techniques to create clusters. Choosing the right clustering algorithm depends on the dataset, business problem, and desired results.

The five main types of clustering are:

1. Partition-based Clustering
2. Hierarchical Clustering
3. Density-based Clustering
4. Distribution-based Clustering
5. Model-based Clustering

---

## 1. Partition-based Clustering

Partition-based clustering divides the dataset into a fixed number of clusters. Each data point belongs to only one cluster.

### Popular Algorithm

- K-Means Clustering

### Suitable For

- Customer Segmentation
- Sales Analysis
- Market Research
- Product Recommendation

### Advantages

- Simple and easy to implement.
- Fast for large datasets.
- Efficient for well-separated clusters.

### Limitations

- Number of clusters (K) must be specified in advance.
- Sensitive to outliers.
- Works best with spherical clusters.

---

## 2. Hierarchical Clustering

Hierarchical clustering creates a tree-like structure called a **dendrogram** that represents relationships between data points.

### Types

- Agglomerative (Bottom-Up)
- Divisive (Top-Down)

### Suitable For

- Biological Data Analysis
- Document Clustering
- Small and Medium-sized Datasets

### Advantages

- No need to specify the number of clusters initially.
- Easy to visualize using a dendrogram.
- Suitable for discovering hierarchical relationships.

### Limitations

- Slower than K-Means for large datasets.
- Difficult to modify clusters after creation.

---

## 3. Density-based Clustering

Density-based clustering groups data points based on dense regions and identifies low-density points as noise or outliers.

### Popular Algorithm

- DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

### Suitable For

- Fraud Detection
- Anomaly Detection
- Geographic Data
- Spatial Analysis

### Advantages

- Detects clusters of different shapes.
- Handles noise and outliers effectively.
- No need to specify the number of clusters.

### Limitations

- Sensitive to parameter selection.
- Performance may decrease with varying data densities.

---

## 4. Distribution-based Clustering

Distribution-based clustering assumes that the data follows a probability distribution, such as a Gaussian distribution.

### Popular Algorithm

- Gaussian Mixture Model (GMM)

### Suitable For

- Financial Analysis
- Medical Research
- Statistical Data Analysis

### Advantages

- Provides probabilistic cluster assignments.
- Works well with overlapping clusters.

### Limitations

- Assumes a specific probability distribution.
- More complex than K-Means.

---

## 5. Model-based Clustering

Model-based clustering assumes that the data is generated from a mixture of statistical models and assigns data points to the most likely model.

### Suitable For

- Pattern Recognition
- Scientific Research
- Complex Data Analysis

### Advantages

- Flexible and accurate.
- Can model complex cluster structures.
- Suitable for advanced applications.

### Limitations

- Computationally expensive.
- Requires statistical assumptions.

---

## Comparison of Clustering Types

| Clustering Type | Popular Algorithm | Best For |
|-----------------|-------------------|----------|
| Partition-based | K-Means | Customer Segmentation |
| Hierarchical | Agglomerative Clustering | Small Datasets |
| Density-based | DBSCAN | Outlier Detection |
| Distribution-based | Gaussian Mixture Model | Statistical Analysis |
| Model-based | Mixture Models | Complex Data Analysis |

---

## Python Examples

### K-Means

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
```

### Hierarchical Clustering

```python
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=3)
```

### DBSCAN

```python
from sklearn.cluster import DBSCAN

model = DBSCAN(eps=0.5, min_samples=5)
```

---

## Real-World Applications

Different clustering techniques are used in:

- Customer Segmentation
- Recommendation Systems
- Fraud Detection
- Image Segmentation
- Medical Diagnosis
- Social Network Analysis
- Market Basket Analysis
- Geographic Data Analysis
- Document Classification

---

## Advantages of Clustering

- No labeled data required.
- Discovers hidden patterns.
- Helps in business decision-making.
- Supports data exploration.
- Useful for large datasets.

---

## Limitations of Clustering

- Selecting the right algorithm can be difficult.
- Results depend on dataset quality.
- Sensitive to noisy data and outliers.
- Some algorithms are computationally expensive.

---

## Key Learnings

Today I learned:

- The different types of clustering algorithms.
- The purpose of Partition-based Clustering.
- The working of Hierarchical Clustering.
- How DBSCAN detects clusters and outliers.
- The concept of Distribution-based Clustering.
- The purpose of Model-based Clustering.
- The strengths and limitations of each clustering technique.
- Basic implementation of clustering algorithms using Scikit-learn.

---

## Conclusion

Different clustering algorithms are designed for different types of datasets and applications. K-Means is suitable for simple and large datasets, Hierarchical Clustering is useful for understanding relationships between data points, DBSCAN is effective for detecting outliers, and Distribution-based and Model-based clustering are ideal for complex statistical datasets. Selecting the appropriate clustering algorithm helps improve analysis, pattern discovery, and decision-making in real-world Machine Learning applications.