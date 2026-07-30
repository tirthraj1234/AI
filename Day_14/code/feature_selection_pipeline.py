import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# FEATURE SELECTION PIPELINE


print("=" * 70)
print("FEATURE SELECTION PIPELINE")
print("=" * 70)


# Step 1 : Load Dataset


iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

print("\nDataset Loaded Successfully")
print("Number of Samples :", X.shape[0])
print("Number of Features:", X.shape[1])

print("\nOriginal Features")
print(X.columns.tolist())


# Step 2 : Train-Test Split


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])


# Step 3 : Build Pipeline


pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("selector", SelectKBest(score_func=f_classif, k=2)),
    ("classifier", LogisticRegression(max_iter=500))
])

print("\nPipeline Created Successfully")


# Step 4 : Train Pipeline


pipeline.fit(X_train, y_train)

print("Pipeline Training Completed")


# Step 5 : Prediction


y_pred = pipeline.predict(X_test)

print("\nPredictions")

print(y_pred)


# Step 6 : Model Evaluation


accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy")

print(f"{accuracy:.4f}")

print("\nClassification Report")

print(classification_report(y_test, y_pred))


# Step 7 : Selected Features


selector = pipeline.named_steps["selector"]

selected_features = X.columns[selector.get_support()]

print("\nSelected Features")

for feature in selected_features:
    print(feature)


# Step 8 : Feature Scores


scores = selector.scores_

feature_scores = pd.DataFrame({
    "Feature": X.columns,
    "Score": scores
})

feature_scores = feature_scores.sort_values(
    by="Score",
    ascending=False
)

print("\nFeature Scores")

print(feature_scores)

