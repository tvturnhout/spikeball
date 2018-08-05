from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import tree
import json
from random import shuffle


def make_float(raw):
    try:
        return float(raw)
    except:
        return raw

with open('events.txt', 'r') as f:
    data = [line.strip() for line in f]

data_new = []
for item in data:
    data_new.append([make_float(s) for s in item.split(',')])

# If you want to randomize training and testing
shuffle(data_new)

X = []
y = []
for item in data_new:
    X.append(item[:-1])
    if item[-1] == 'n':
        y.append(0)
    elif item[-1] == 'r':
        y.append(1)


X_test = X[::3]
y_test = y[::3]
X_train = [item for item in X if item not in X_test]
y_train = []
index_list = []
for item in X_train:
    index_list.append(X.index(item))
for item in index_list:
    y_train.append(y[item])


# clf 
clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(X_train, y_train)
print( "SGD: " + str(clf.score(X_test, y_test)) )

clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
print( "Tree: " + str(clf.score(X_test, y_test)) )

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X_train, y_train)
print( "MLP: " + str(clf.score(X_test, y_test)) )


