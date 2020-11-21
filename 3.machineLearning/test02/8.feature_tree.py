from sklearn.datasets import load_iris, load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

feature_data = load_wine()
decision_tree = DecisionTreeClassifier(random_state=0, max_depth=3)
decision_tree = decision_tree.fit(feature_data.data, feature_data.target)
tree = export_text(decision_tree, feature_names=feature_data['feature_names'])
print(tree)