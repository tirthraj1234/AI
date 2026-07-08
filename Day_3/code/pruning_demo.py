from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

#model = DecisionTreeClassifier(max_depth=3)# pre pruning

#model = DecisionTreeClassifier(ccp_alpha=0.01)# post pruning

print(model)