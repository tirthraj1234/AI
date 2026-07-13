from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create KNN model
model = KNeighborsClassifier(
    n_neighbors=5,
    weights="uniform",
    algorithm="auto",
    metric="minkowski"
)

# Train model
model.fit(X_train, y_train)

print("Model trained successfully.")