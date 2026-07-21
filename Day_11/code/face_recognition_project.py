from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ----------------------------------------
# Load Dataset
# ----------------------------------------
faces = fetch_olivetti_faces(shuffle=True, random_state=42)

X = faces.data
y = faces.target

print("=" * 60)
print("Face Recognition using PCA")
print("=" * 60)

print("Dataset Shape :", X.shape)
print("Target Shape  :", y.shape)

# ----------------------------------------
# Split Dataset
# ----------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ----------------------------------------
# Feature Scaling
# ----------------------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ----------------------------------------
# Apply PCA
# ----------------------------------------
pca = PCA(n_components=100, whiten=True, random_state=42)

X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

print("\nOriginal Features :", X.shape[1])
print("Reduced Features  :", X_train_pca.shape[1])

# ----------------------------------------
# Train Model
# ----------------------------------------
model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X_train_pca, y_train)

# ----------------------------------------
# Prediction
# ----------------------------------------
predictions = model.predict(X_test_pca)

# ----------------------------------------
# Evaluation
# ----------------------------------------
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy :", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nProject Completed Successfully!")