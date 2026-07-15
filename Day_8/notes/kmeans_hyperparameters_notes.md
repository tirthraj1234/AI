# K-Means Hyperparameters Notes

## Day 8 – K-Means Hyperparameters

## What are Hyperparameters?

Hyperparameters are configuration values that are set before training a Machine Learning model. They control how the K-Means algorithm works and influence the quality and performance of clustering.

Unlike model parameters, hyperparameters are not learned from the training data.

---

## Why are Hyperparameters Important?

Hyperparameters help to:

- Improve clustering performance.
- Increase model stability.
- Control the training process.
- Produce better cluster quality.
- Ensure consistent and reproducible results.

---

## 1. n_clusters

The `n_clusters` hyperparameter specifies the number of clusters that the K-Means algorithm should create.

### Example

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
```

### Advantages

- Controls the number of groups.
- Easy to configure.
- Works well when the correct value of K is known.

---

## 2. init

The `init` hyperparameter determines how the initial centroids are selected.

### Common Values

- `"k-means++"` (default) – Selects centroids intelligently for faster and more stable convergence.
- `"random"` – Selects centroids randomly.

### Example

```python
model = KMeans(
    n_clusters=3,
    init="k-means++"
)
```

### Advantages

- Faster convergence.
- Better clustering quality.
- Reduces the chance of poor initial centroids.

---

## 3. n_init

The `n_init` hyperparameter specifies how many times K-Means runs with different initial centroid positions. The best result is selected.

### Default Value

```python
10
```

### Example

```python
model = KMeans(
    n_clusters=3,
    n_init=10
)
```

### Advantages

- Produces more reliable results.
- Reduces the effect of poor initialization.
- Improves clustering quality.

---

## 4. max_iter

The `max_iter` hyperparameter specifies the maximum number of iterations allowed during a single run of the algorithm.

### Default Value

```python
300
```

### Example

```python
model = KMeans(
    n_clusters=3,
    max_iter=300
)
```

### Advantages

- Prevents infinite iterations.
- Controls training time.
- Ensures the algorithm stops after a fixed number of iterations.

---

## 5. random_state

The `random_state` hyperparameter controls the random initialization process and helps produce reproducible results.

### Example

```python
model = KMeans(
    n_clusters=3,
    random_state=42
)
```

### Advantages

- Produces consistent results.
- Useful for testing and debugging.
- Makes experiments reproducible.

---

## 6. algorithm

The `algorithm` hyperparameter specifies the implementation used by the K-Means algorithm.

### Common Value

- `"lloyd"` – Standard implementation used in Scikit-learn.

### Example

```python
model = KMeans(
    n_clusters=3,
    algorithm="lloyd"
)
```

---

## Best Practices

- Use the Elbow Method to select the optimal value of **K**.
- Use `init="k-means++"` for better centroid initialization.
- Keep `n_init` at a reasonable value to improve stability.
- Use `random_state` for reproducible experiments.
- Increase `max_iter` only if the model does not converge.

---

## Complete Python Example

```python
from sklearn.cluster import KMeans

model = KMeans(
    n_clusters=3,
    init="k-means++",
    n_init=10,
    max_iter=300,
    random_state=42,
    algorithm="lloyd"
)

print(model)
```

---

## Advantages

- Improves clustering performance.
- Produces more stable clusters.
- Helps achieve faster convergence.
- Makes experiments reproducible.
- Reduces poor centroid initialization.

---

## Limitations

- Incorrect hyperparameter values can reduce clustering quality.
- Selecting the best number of clusters requires experimentation.
- Large values of `n_init` may increase computation time.

---

## Real-World Applications

K-Means hyperparameters are important in:

- Customer Segmentation
- Market Analysis
- Product Recommendation
- Image Segmentation
- Medical Data Analysis
- Fraud Detection
- Sales Analysis
- Geographic Data Clustering

---

## Key Learnings

Today I learned:

- What hyperparameters are.
- The purpose of `n_clusters`.
- How `init` selects centroids.
- The role of `n_init`.
- Why `max_iter` is important.
- How `random_state` ensures reproducibility.
- The purpose of the `algorithm` parameter.
- Best practices for configuring K-Means.

---

## Conclusion

K-Means hyperparameters play an important role in determining the quality and efficiency of clustering. Parameters such as `n_clusters`, `init`, `n_init`, `max_iter`, `random_state`, and `algorithm` help control how the algorithm initializes, trains, and converges. Selecting appropriate hyperparameter values leads to more accurate, stable, and reliable clustering results in real-world Machine Learning applications.