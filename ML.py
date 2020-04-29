import sklearn
from sklearn import tree
val1 = float(input("Enter Toy Size Value(1-10): "))
val2 = float(input("Enter Toy Complexity Value(1-10): "))
features = [[1,1],[10,10], [5 ,5 ], [ 10, 6], [10, 7], [6,7], [8,9], [5,10]]
labels = ["Hates","Likes", "Hates", "Hates", "Likes", "Likes", "Likes", "Hates"] 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[val2, val1]]))