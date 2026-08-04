import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# MODEL SELECTION DEMONSTRATION


print("=" * 70)
print("MODEL SELECTION DEMONSTRATION")
print("=" * 70)


# Step 1 : Load Dataset


iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

print("\nDataset Loaded Successfully")
print("Samples :", X.shape[0])
print("Features:", X.shape[1])


# Step 2 : Train-Test Split


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])


# Step 3 : Define Models


models = {
    "Logistic Regression": LogisticRegression(max_iter=300),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5)
}

results = []


# Step 4 : Train and Evaluate Models


for name, model in models.items():

    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_accuracy = accuracy_score(y_train, train_pred)
    test_accuracy = accuracy_score(y_test, test_pred)

    results.append([
        name,
        round(train_accuracy, 4),
        round(test_accuracy, 4)
    ])


# Step 5 : Display Results


results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Training Accuracy",
        "Testing Accuracy"
    ]
)

print("\nModel Comparison")
print(results_df)


# Step 6 : Select Best Model


best_model = results_df.sort_values(
    by="Testing Accuracy",
    ascending=False
).iloc[0]

print("\nBest Model")
print(f"Model Name      : {best_model['Model']}")
print(f"Testing Accuracy: {best_model['Testing Accuracy']}")


# Step 7 : Overfitting Check


print("\nOverfitting Analysis")

for _, row in results_df.iterrows():

    gap = abs(
        row["Training Accuracy"] -
        row["Testing Accuracy"]
    )

    if gap > 0.10:
        status = "Possible Overfitting"
    else:
        status = "Good Generalization"

    print(f"{row['Model']} --> {status}")

