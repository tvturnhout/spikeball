from sklearn.linear_model import SGDClassifier
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
y_train = [item for item in y if item not in y_test]


# clf 
clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(X_train, y_train)


