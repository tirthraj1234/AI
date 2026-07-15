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