from sklearn.model_selection import train_test_split
from sklearn . preprocessing import StandardScaler
from sklearn . metrics import confusion_matrix
from sklearn . naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import os

df_Y1 = pd.read_csv("./Year1-52 .csv")
df_Y2 = pd.read_csv("./Year2-52.csv")

X = df_Y1[["week number","average", "std"]]
y = df_Y1["Label"]
x1 = df_Y2[["week number","average", "std"]]
y1 = df_Y1["Label"]

print('Q1')

def naive_bayesian(a, b):
    X_train = X
    Y_train = y
    X_test = x1
    Y_test = y1
    NB_classifier = GaussianNB().fit(X_train, Y_train)
    pred_log = NB_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)
    print("The Accuracy is {} % with Naive Bayesian".format(accuracy*100))
    return pred_log, Y_test

pred_log,Y_test = naive_bayesian(X,y)

cf_1 = confusion_matrix(Y_test, pred_log)
print("Confusion matrix is")
print("TP: ", cf_1[0][0])
print("FP: ", cf_1[0][1])
print("FN: ", cf_1[1][0])
print("TN: ", cf_1[1][1])
tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
print("TPR  for Year 2 is {}".format(tpr))
print("TNR  for Year 2 is {}".format(tnr))
