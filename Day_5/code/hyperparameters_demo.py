from sklearn import datasets
from sklearn.svm import SVC

# Load dataset
X, y = datasets.load_iris(return_X_y=True)

# Create SVM model
model = SVC(
    C=1.0,
    gamma="scale",
    kernel="rbf"
)

model.fit(X, y)

print("Kernel:", model.kernel)
print("C:", model.C)
print("Gamma:", model.gamma)