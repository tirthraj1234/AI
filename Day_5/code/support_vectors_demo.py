from sklearn import datasets
from sklearn.svm import SVC

# Load sample dataset
X, y = datasets.load_iris(return_X_y=True)

# Train SVM model
model = SVC(kernel="linear")
model.fit(X, y)

print("Number of Support Vectors:", model.n_support_)
print("Support Vector Indices:")
print(model.support_)