from sklearn.metrics import confusion_matrix
from sklearn import tree
import numpy as np
import pandas as pd

df_y1 = pd.read_csv("./Year1-52.csv")
df_y2 = pd.read_csv("./Year1-52.csv")

X1 = df_y1[["average", "std"]]
y1 = df_y1["Label"]
X2 = df_y2[["average", "std"]]
y2 = df_y2["Label"]


def decisionTree(a, b):
    X_train = X1
    Y_train = y1
    X_test = X2
    Y_test = y2
    tree_classifier = tree.DecisionTreeClassifier(criterion="entropy")
    tree_classifier = tree_classifier.fit(X_train, Y_train)
    pred_log = tree_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)

    cm1 = confusion_matrix(Y_test, pred_log)
    print('USING Decision Tree CLASSIFIER:')
    print("Accuracy: {}%".format(str(round(accuracy*100, 3))))
    print("Confusion matrix for Year 2  is:")
    print("TP: ", cm1[0][0])
    print("FP: ", cm1[0][1])
    print("FN: ", cm1[1][0])
    print("TN: ", cm1[1][1])
    print()
    tpr = cm1[1][1] / (cm1[1][1] + cm1[1][0])
    tnr = cm1[0][0] / (cm1[0][0] + cm1[0][1])
    print("Year 2 TPR = {}".format(round(tpr, 3)))
    print("Year 2 TNR = {}".format(round(tnr, 3)))
decisionTree(X2,y2)