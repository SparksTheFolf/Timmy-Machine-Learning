import sklearn
from sklearn import tree

print('Machine Learning by Nolant108, MIT Licence Nolan Trapp (c) 2020, github.com/nolant108')

f11 = float(input("Enter features 1-1 to be predicted: "))
f12 = float(input("Enter features 1-2 to be predicted: "))
f21 = float(input("Enter features 2-1 to be predicted: "))
f22 = float(input("Enter features 2-2 to be predicted: "))
f31 = float(input("Enter features 3-1 to be predicted: "))
f32 = float(input("Enter features 3-2 to be predicted: "))
f41 = float(input("Enter features 4-1 to be predicted: "))
f42 = float(input("Enter features 4-2 to be predicted: "))
f51 = float(input("Enter features 5-1 to be predicted: "))
f52 = float(input("Enter features 5-2 to be predicted: "))
f61 = float(input("Enter features 6-1 to be predicted: "))
f62 = float(input("Enter features 6-2 to be predicted: "))
f71 = float(input("Enter features 7-1 to be predicted: "))
f72 = float(input("Enter features 7-2 to be predicted: "))
f81 = float(input("Enter features 8-1 to be predicted: "))
f82 = float(input("Enter features 8-2 to be predicted: "))

print('Here is your Machine Learning inputs')
print([f11, f12],[f21, f22] ,[f31, f32] ,[f41, f42] ,[f51, f52] ,[f61, f62] ,[f71, f72] , [f81, f82])
print('-------------------------------------------------------------------------------------------')
features = [[f11, f12],[f21, f22] ,[f31, f32] ,[f41, f42] ,[f51, f52] ,[f61, f62] ,[f71, f72] , [f81, f82]]

print('Now create your labes for the pairs(Ex: f1-1, f1-2 = Likes && f2-1, f2-2 = Hates: )')

l1 = input("Input Label 1 for F1-1, F1-2: ")
l2 = input("Input Label 2 for F2-1, F2-2: ")
l3 = input("Input Label 3 for F3-1, F3-2: ")
l4 = input("Input Label 4 for F4-1, F4-2: ")
l5 = input("Input Label 5 for F5-1, F5-2: ")
l6 = input("Input Label 6 for F6-1, F6-2: ")
l7 = input("Input Label 7 for F7-1, F7-2: ")
l8 = input("Input Label 8 for F8-1, F8-2: ")

print('Here is your Machine Learning labels')
print([ l1, l2, l3, l4, l5, l6, l7, l8])
print('---------------------------------------------------')
labels = [ l1, l2, l3, l4, l5, l6, l7, l8]


print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val1, val2]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))


print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))


print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))

print('------------NEW CLASS VALUE INPUT------------')

val1 = float(input("Enter Value1 to be predicted: "))
val2 = float(input("Enter Value2 to be predicted: "))
print('------------------------------------------------------------------')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Your predicted value is: ')
print(clf.predict([[val2, val1]]))