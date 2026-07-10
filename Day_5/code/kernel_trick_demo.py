from sklearn import datasets
from sklearn.svm import SVC

# Load dataset
X, y = datasets.load_iris(return_X_y=True)

# Train SVM using RBF Kernel
model = SVC(kernel="rbf")

model.fit(X, y)

print("Kernel Used:", model.kernel)
print("Model trained successfully.")