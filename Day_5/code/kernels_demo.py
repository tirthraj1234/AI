from sklearn import datasets
from sklearn.svm import SVC

# Load dataset
X, y = datasets.load_iris(return_X_y=True)

kernels = ["linear", "poly", "rbf", "sigmoid"]

for kernel in kernels:
    model = SVC(kernel=kernel)
    model.fit(X, y)
    print(f"{kernel} kernel trained successfully.")