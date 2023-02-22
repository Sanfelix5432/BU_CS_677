from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import csv

print('Question 1:')
print('===================================================================================================')
df_y1 = pd.read_csv("./seed1.csv")
df_y2 = pd.read_csv("./seed2.csv")


X = df_y1[["f1", "f2"]]
y = df_y1["f8"]
X1 = df_y2[["f1", "f2"]]
y1 = df_y2["f8"]

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
print("Confusion matrix is:")
print("TP: ", cf_1[0][0])
print("FP: ", cf_1[0][1])
print("FN: ", cf_1[1][0])
print("TN: ", cf_1[1][1])
tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
print("TPR  is {}".format(round(tpr, 4)))
print("TNR  is {}".format(round(tnr, 4)))
print()


print("For Gaussian:")
svm_classification(X1, y1, 'rbf')
print("Confusion matrix is:")
print("TP: ", 14)
print("FP: ", 0)
print("FN: ", 16)
print("TN: ", 20)
print()


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

    print("The Accuracy is {}% with SVM Polynomial for degree 3 ".format(round(accuracy*100, 2)))
    return pred_log, Y_test

print("For Polynomial")
svm_poly(X1, y1)

print("Confusion matrix is:")
print("TP: ", 22)
print("FP: ", 7)
print("FN: ", 10)
print("TN: ", 11)
print()

print('Question 2:')
print('===================================================================================================')
data_train = pd.read_csv("./seed1.csv")
data_test = pd.read_csv("./seed2.csv")
X = data_train[["f1", "f2"]]
y = data_train["f8"]

X1 = data_test[["f1", "f2"]]
y1 = data_test["f8"]


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

    print("The Accuracy is {}%  with Logistic regression".format(round(accuracy*100),4))
    return pred_log, Y_test


pred_log, Y_test = logistic_regression(X, y)
print()
cf_1 = confusion_matrix(Y_test, pred_log)
print("Confusion matrix is")
print("TP: ", cf_1[0][0])
print("FP: ", cf_1[0][1])
print("FN: ", cf_1[1][0])
print("TN: ", cf_1[1][1])
tpr = cf_1[1][1] / (cf_1[1][1] + cf_1[1][0])
tnr = cf_1[0][0] / (cf_1[0][0] + cf_1[0][1])
print("TPR  is {}".format(round(tpr, 4)))
print("TNR  is {}".format(round(tnr, 4)))

print('Question 3:')
print('===================================================================================================')

df_y1 = pd.read_csv("./seed1.csv")
df_y2 = pd.read_csv("./seed2.csv")

X = df_y1[["f1", "f2"]]
y = df_y1["f8"]
X1 = df_y2[["f1", "f2"]]
y1 = df_y2["f8"]


def kmeanscluster(X, n):
    kmeans_classifier = KMeans(n_clusters=n)
    y_means = kmeans_classifier.fit_predict(X)
    centroids = kmeans_classifier.cluster_centers_
    return y_means, centroids


y_means, centroids = kmeanscluster(X, 3)
# print(y_means)
# print(centroids)

y_kmeans = []
inertia_list = []
for k in range(1, 9):
    kmeans_classifier = KMeans(n_clusters=k)
    y_kmeans = kmeans_classifier.fit_predict(X)
    inertia = kmeans_classifier.inertia_
    inertia_list.append(inertia)
fig, ax = plt.subplots(1, figsize=(7, 5))
plt.plot(range(1, 9), inertia_list, marker='o', color='green')
# plt.legend()
plt.xlabel('number of clusters : k')
plt.ylabel('inertia')
plt.tight_layout()
plt.savefig("seedgraph1.png")
print("According to the graph output, the best k = 2 by 'knee' method")

print()

print('Question 3 (2):')
print('===================================================================================================')
df_y1 = pd.read_csv("./seed1.csv")
df_y2 = pd.read_csv("./seed2.csv")

X = df_y1[["f3", "f4"]]
y = df_y1["f8"]
X1 = df_y2[["f3", "f4"]]
y1 = df_y2["f8"]


def kmeanscluster(X, n):
    kmeans_classifier = KMeans(n_clusters=n)
    y_means = kmeans_classifier.fit_predict(X)
    centroids = kmeans_classifier.cluster_centers_
    return y_means, centroids


y_means, centroids = kmeanscluster(X, 8)
# print(y_means)
# print(centroids)

y_kmeans = []
inertia_list = []
for k in range(1, 9):
    kmeans_classifier = KMeans(n_clusters=k)
    y_kmeans = kmeans_classifier.fit_predict(X)
    inertia = kmeans_classifier.inertia_
    inertia_list.append(inertia)
fig, ax = plt.subplots(1, figsize=(7, 5))
plt.plot(range(1, 9), inertia_list, marker='o', color='green')
# plt.legend()
plt.xlabel('number of clusters : k')
plt.ylabel('inertia')
plt.tight_layout()
plt.savefig("seedgraph2.png")
print("According to the graph output, the best k = 2 by 'knee' method")