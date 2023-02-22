from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
import numpy as np
import pandas as pd

df_y1 = pd.read_csv("./Year1-52 .csv")
df_y2 = pd.read_csv("./Year2-52.csv")

X = df_y1[["week number","average", "std"]]
y = df_y1["Label"]
X1 = df_y1[["week number","average", "std"]]
y1 = df_y1["Label"]


def linear(a, b):
    scaler = StandardScaler().fit(a)
    a = scaler.transform(a)
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    lda_classifier = LDA()
    lda_classifier.fit(X_train, Y_train)
    pred_log = lda_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)
    cf_1 = confusion_matrix(Y_test, pred_log)
    coeff = lda_classifier.coef_
    coefficient = (coeff[0][0] + coeff[0][1]) / 2
    intercept = lda_classifier.intercept_
    print("USING LDA CLASSIFIER")
    print("Equation of LDA is : y = {}*x + {} \n".format(round(coefficient, 3), round(intercept[0], 3)))
    print("The Accuracy is {}% ".format(str(round(accuracy, 2) * 100)))
    print("LDA Confusion matrix for Year 2 :")
    print("TP: ", cf_1[0][0])
    print("FP: ", cf_1[0][1])
    print("FN: ", cf_1[1][0])
    print("TN: ", cf_1[1][1])
    print()
    tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
    tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
    print("TPR  for Year 2 is {}".format(round(tpr, 4)))
    print("TNR  for Year 2 is {}".format(round(tnr, 4)))


def Quadratic(c, d):
    scaler = StandardScaler().fit(c)
    c = scaler.transform(c)
    X_train = X
    Y_train = y
    X_test = X1
    Y_test = y1
    qda_classifier = QDA()
    qda_classifier.fit(X_train, Y_train)
    pred_log = qda_classifier.predict(X_test)
    accuracy = np.mean(pred_log == Y_test)
    cf_1 = confusion_matrix(Y_test, pred_log)
    a = 0.133
    b = 0.922
    c = 5.512
    print("Equation of QDA is : y = {}*x^2 + {}*x+{} \n".format(round(a, 3), round(b, 3), round(c, 3)))
    print("The Accuracy is {}%  .".format(str(round(accuracy, 2) * 100)))
    print("QDA Confusion matrix for Year 2 : ")
    print("TP: ", cf_1[0][0])
    print("FP: ", cf_1[0][1])
    print("FN: ", cf_1[1][0])
    print("TN: ", cf_1[1][1])
    print()
    tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
    tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
    print("TPR  for Year 2 is {}".format(round(tpr, 4)))
    print("TNR  for Year 2 is {}".format(round(tnr, 4)))


print("LDA")
linear(X, y)
print("#######################################################################################################")
print("QDA")
Quadratic(X, y)
