from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df_train = pd.read_csv("./train.csv")
df_test = pd.read_csv("./test.csv")

X = df_train[["qty_ordered", "price","value","discount_amount","total","age"]]
y = df_train["Method in number"]

X1 = df_test[["qty_ordered", "price","value","discount_amount","total","age"]]
y1 = df_test["Method in number"]


def logistic_regression(a, b):
    scaler = StandardScaler().fit(X)
    a = scaler.transform(a)
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    log_reg_classifier = LogisticRegression()
    model = log_reg_classifier.fit(X_train, Y_train)
    pred_log = log_reg_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)
    coeff = model.coef_
    print("Equation for log regression is : y = {}*x + ({}) ".format(round(coeff[0][0],4), round(coeff[0][1],4)))

    print("The Accuracy is {}%  with Logistic regression".format(accuracy*100))
    return pred_log, Y_test


pred_log, Y_test = logistic_regression(X, y)
print()
cf_1 = confusion_matrix(Y_test, pred_log)
print("Confusion matrix for Part 2  is")
print("TP: ", cf_1[0][0])
print("FP: ", cf_1[0][1])
print("FN: ", cf_1[1][0])
print("TN: ", cf_1[1][1])
print("--------------------------------------------")
tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
print("TPR  for Test is {}".format(tpr))
print("TNR  for Test is {}".format(tnr))