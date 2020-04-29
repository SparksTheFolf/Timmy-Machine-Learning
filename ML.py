import sklearn
from sklearn import tree
val1 = float(input("Enter value1(10-100, x10 increments): "))
val2 = float(input("Enter value2(1-10): "))
features = [[1,10],[10,100], [5 ,50 ], [ 10, 60], [10, 70], [6,70], [8,90], [5,100]]
labels = ["Hates","Likes", "Hates", "Hates", "Likes", "Likes", "Likes", "Hates"] 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[val1, val2]]))
