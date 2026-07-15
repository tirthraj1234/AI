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