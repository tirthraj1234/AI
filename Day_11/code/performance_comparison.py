from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# Logistic Regression
pca_model = LogisticRegression(random_state=42)
lda_model = LogisticRegression(random_state=42)

pca_model.fit(X_train_pca, y_train)
lda_model.fit(X_train_lda, y_train)

# Predictions
pca_pred = pca_model.predict(X_test_pca)
lda_pred = lda_model.predict(X_test_lda)

# Accuracy
print("=" * 50)
print("PCA Accuracy :", accuracy_score(y_test, pca_pred))

print("\nLDA Accuracy :", accuracy_score(y_test, lda_pred))

print("\nPCA Confusion Matrix")
print(confusion_matrix(y_test, pca_pred))

print("\nLDA Confusion Matrix")
print(confusion_matrix(y_test, lda_pred))

print("\nPCA Classification Report")
print(classification_report(y_test, pca_pred))

print("\nLDA Classification Report")
print(classification_report(y_test, lda_pred))