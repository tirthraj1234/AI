import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Age": [22, 25, 47, 52, 46, 56, 23, 27, 50, 60],
    "Income": [20000, 25000, 70000, 75000, 72000, 78000, 22000, 27000, 71000, 80000]
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