import sklearn
from sklearn import tree
features = [[1,1],[10,10], [5 ,5 ], [ 10, 6], [10, 7], [6,7], [8,9], [5,10]]
labels = ["Hates","Likes", "Hates", "Hates", "Likes", "Likes", "Likes", "Hates"] 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([['9', '2']]))