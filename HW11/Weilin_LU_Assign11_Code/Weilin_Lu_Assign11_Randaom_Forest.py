from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_y1 = pd.read_csv("./train.csv")
df_y2 = pd.read_csv("./test.csv")
X1 = df_y1[["qty_ordered", "price","value","discount_amount","total","age"]]
y1 = df_y1["Method in number"]
X2 = df_y2[["qty_ordered", "price","value","discount_amount","total","age"]]
y2 = df_y2["Method in number"]
error_rate = []

print("****************************************************************************************")

print("Q1")
def Randomforest(a, b, num, depth):
    X_train = X1
    Y_train = y1
    X_test = X2
    Y_test = y2
    model = RandomForestClassifier(n_estimators=num, max_depth=depth, criterion="entropy")
    model.fit(X_train, Y_train)
    pred_log = model.predict(X_test)
    er = np.mean(pred_log != Y_test)
    er = round(er, 2)
    error_rate.append(np.mean(pred_log != Y_test))
    print("The Error Rate is {} when n={},d={}".format(str(round(er, 2)), num, depth))
    return pred_log, Y_test, er


for n in range(1, 11):
    for d in range(1, 6):
        pred_log, Y_test, er = Randomforest(X2, y2, n, d)
        plt.title('n vs d ')
        plt.xlabel('number of learners : n')
        plt.ylabel('depth ')
        if (er == 0.0):
            er = 0.001
        else:
            er = er

        plt.scatter(x=n, y=d, s=er * 1000)

plt.savefig("Error_Rate.pdf")

def RandomforestOptimal(a, b, num, depth):
    X_train = X1
    Y_train = y1
    X_test = X2
    Y_test = y2
    model = RandomForestClassifier(n_estimators=num, max_depth=depth, criterion="entropy")
    model.fit(X_train, Y_train)
    pred_log = model.predict(X_test)

    cf_1 = confusion_matrix(Y_test, pred_log)
    print('USING RANDOM FOREST CLASSIFIER:')
    print("Confusion matrix Year 2: ")
    print("TP: ", cf_1[0][0])
    print("FP: ", cf_1[0][1])
    print("FN: ", cf_1[1][0])
    print("TN: ", cf_1[1][1])
    print("****************************************************************************************")
    tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
    tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
    print("Year 2")
    print("TPR :{}".format(round(tpr, 4)))
    print("TNR :{}".format(round(tnr, 4)))


print("****************************************************************************************")
print("Input the optimal value for Year 1 ")
num = int(input("n : "))
dep = int(input("d : "))
print("When n = {} and d = {}".format(str(num), str(dep)))
print("****************************************************************************************")
RandomforestOptimal(X2, y2, num, dep)
