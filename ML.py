import sklearn
from sklearn import tree
val1 = float(input("Enter value1(10-100, x10 increments): "))
val2 = float(input("Enter value2(1&10): "))
features = [[10, 10], [100, 10], [20, 1], [10, 1], [ 90, 10], [ 70, 10], [40, 1], [80, 1]]
labels = ["Hates", "Likes", "Hates", "Hates", "Likes", "Likes", "Hates", "Hates"] 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[val1, val2]]))
