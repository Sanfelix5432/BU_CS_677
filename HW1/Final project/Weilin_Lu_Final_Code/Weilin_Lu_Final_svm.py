from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df_y1 = pd.read_csv("./train.csv")
df_y2 = pd.read_csv("./test.csv")

X = df_y1[["qty_ordered", "price","value","discount_amount","total","age"]]
y = df_y1["Method in number"]
X1 = df_y2[["qty_ordered", "price","value","discount_amount","total","age"]]
y1 = df_y2["Method in number"]

def svm_classification(a, b, z):
    scaler = StandardScaler().fit(X)
    a = scaler.transform(a)
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1

    svm_classifier = svm.SVC(kernel=z)
    svm_classifier.fit(X_train, Y_train)
    pred_log = svm_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)

    print("The Accuracy is {}% ".format(round(accuracy*100, 2)))
    return pred_log, Y_test


print("For Linear")
pred_log, Y_test = svm_classification(X1, y1, 'linear')

cf_1 = confusion_matrix(Y_test, pred_log)
print("Confusion matrix for Year 2  is:")
print("TP: ", cf_1[0][0])
print("FP: ", cf_1[0][1])
print("FN: ", cf_1[1][0])
print("TN: ", cf_1[1][1])
print()
tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
print("TPR  for test is {}".format(round(tpr, 4)))
print("TNR  for test is {}".format(round(tnr, 4)))

print('-------------------------------------------------------------------------------------------------')
print("For Gaussian:")
svm_classification(X1, y1, 'rbf')


def svm_poly(a, b):
    scaler = StandardScaler().fit(X)
    a = scaler.transform(a)
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1

    svm_classifier = svm.SVC(kernel='poly', degree=2)
    svm_classifier.fit(X_train, Y_train)
    pred_log = svm_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)

    print("The Accuracy is {}% with SVM Polynomial for degree 2 ".format(round(accuracy*100, 2)))
    return pred_log, Y_test

print("-------------------------------------------------------------------------------------------------------")
print("For Polynomial")
svm_poly(X1, y1)