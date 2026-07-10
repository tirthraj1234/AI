# import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# load dataset
iris = load_iris()

X = iris.data
y = iris.target

print("Features Shape:", X.shape)
print("Target Shape:", y.shape)

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# create svm model
model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale"
)

# train model
model.fit(X_train, y_train)

print("Model trained successfully.")

# make predictions
y_pred = model.predict(X_test)

print("Predictions:")
print(y_pred)

# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

