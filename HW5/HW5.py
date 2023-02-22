import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

print('Question 1:')

print('Q1 (1):')

url = r"https://archive.ics.uci.edu/ml/" + r"machine-learning-databases/iris/iris.data"
data = pd.read_csv(url, names = [
    "sepal-length", "sepal-width",
    "petal-length", "petal-width",
    "Class"
])

print(data)

print(data.describe())
print('==============================================================')
print('\n')

print('Q1 (2):')
df_se = data[:50]
df_ve = data[50:100]
df_vi = data[100:]
df_all = data[50:]

print('SE')
print(df_se.describe())
print('==============================================================')
print('\n')

print('VE')
print(df_ve.describe())
print('==============================================================')
print('\n')

print('VI')
print(df_vi.describe())
print('==============================================================')

print('VE & VI')
print(df_all.describe())
print('==============================================================')
print('\n')


print('Q1 (3):')

print('SE')
print(df_se.corr())
print('==============================================================')
print('\n')

print('VE')
print(df_ve.corr())
print('==============================================================')
print('\n')

print('VI')
print(df_vi.corr())
print('==============================================================')
print('\n')


print('Question 2:')

print('Q2 (1):')

df_all2 = df_all.drop(labels = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width' ], axis = 1)



from sklearn.model_selection import train_test_split

df_all_train,df_all_test,df_all2_train,df_all2_test= train_test_split(df_all,df_all2,test_size=0.5,random_state = 80,shuffle = True)


features = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']
pair_plot = sns.pairplot(df_all_train[features])
plt.show()


print('training set: ')
print(df_all_train)
print('=============================================================================')

print('==============================================================')
print('\n')

print('Q2 (2):')


df1 = df_all_train[['sepal-length']]

df2 = df_all_train[['sepal-width']]


df3 = df_all_train[['petal-length']]


df4 = df_all_train[['petal-width']]


df5 = df_all_train[['Class']]

list0 = [
0,
1,
0,
0,
1,
0,
0,
0,
1,
1,
1,
1,
0,
0,
0,
1,
1,
0,
1,
0,
1,
0,
0,
1,
0,
0,
0,
0,
1,
1,
0,
1,
0,
0,
1,
1,
1,
0,
1,
0,
1,
1,
0,
1,
0,
1,
0,
1,
0,
1
]

list1 =[
1,
0,
0,
0,
0,
0,
0,
0,
1,
1,
0,
1,
0,
0,
0,
1,
0,
0,
0,
1,
1,
0,
0,
1,
0,
0,
1,
1,
1,
0,
0,
1,
0,
1,
0,
1,
1,
1,
1,
0,
0,
0,
0,
1,
0,
1,
0,
1,
0,
0
]

list2 =[
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0

]

list3 = [
1,
1,
1,
0,
1,
0,
0,
0,
1,
1,
1,
1,
0,
0,
0,
1,
1,
0,
1,
0,
1,
0,
1,
1,
0,
0,
1,
1,
1,
1,
0,
1,
0,
0,
1,
1,
1,
0,
1,
0,
1,
1,
0,
1,
0,
1,
0,
1,
0,
1

]

list4 = [
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0

]



list5 = [None] * 50  #S
list6 = [None] * 50  #SW
list7 = [None] * 50  #PL
list8 = [None] * 50  #PW





#list5，SL confusion matrix
print('PW:CalculateQ2 confusion matrix ')
for i in range(50):
    if(list0[i] == 0) and (list1[i] == 0):
        list5[i] = 'TN'
    elif(list0[i] == 0) and (list1[i] == 1):
        list5[i] = 'FP'
    elif(list0[i] == 1) and (list1[i] == 1):
        list5[i] = 'TP'
    elif(list0[i] == 1) and (list1[i] == 0):
        list5[i] = 'FN'
    else:
        continue

#list6，SW confusion matrix
print('PW:CalculateQ2 confusion matrix ')
for i in range(50):
    if (list0[i] == 0) and (list2[i] == 0):
        list6[i] = 'TN'
    elif (list0[i] == 0) and (list2[i] == 1):
        list6[i] = 'FP'
    elif (list0[i] == 1) and (list2[i] == 1):
        list6[i] = 'TP'
    elif (list0[i] == 1) and (list2[i] == 0):
        list6[i] = 'FN'
    else:
        continue

#list7，PL confusion matrix
print('PW:CalculateQ2 confusion matrix ')
for i in range(50):
    if (list0[i] == 0) and (list3[i] == 0):
        list7[i] = 'TN'
    elif (list0[i] == 0) and (list3[i] == 1):
        list7[i] = 'FP'
    elif (list0[i] == 1) and (list3[i] == 1):
        list7[i] = 'TP'
    elif (list0[i] == 1) and (list3[i] == 0):
        list7[i] = 'FN'
    else:
        continue

#print('=============================================================================')
#print('\n')

#list8，PW confusion matrix
print('PW:CalculateQ2 confusion matrix ')
for i in range(50):
    if (list0[i] == 0) and (list4[i] == 0):
        list8[i] = 'TN'
    elif (list0[i] == 0) and (list4[i] == 1):
        list8[i] = 'FP'
    elif (list0[i] == 1) and (list4[i] == 1):
        list8[i] = 'TP'
    elif (list0[i] == 1) and (list4[i] == 0):
        list8[i] = 'FN'
    else:
        continue

#print('=============================================================================')
#print('\n')

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#SL confusion matrix and accuracy
print('Q2 (2)confusion for SL: ')
for i in range(50):
    if(list5[i] == 'TN'):
        temp1 += 1
    elif(list5[i] == 'FP'):
        temp2 += 1
    elif(list5[i] == 'TP'):
        temp3 += 1
    elif(list5[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q2 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')



temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#SW counfusion and accuracy
print('Q2 (2) confusion for SW: ')
for i in range(50):
    if(list6[i] == 'TN'):
        temp1 += 1
    elif(list6[i] == 'FP'):
        temp2 += 1
    elif(list6[i] == 'TP'):
        temp3 += 1
    elif(list6[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q2 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#PL counfusion and accuracy
print('Q2 (2) confusion for PL: ')
for i in range(50):
    if(list7[i] == 'TN'):
        temp1 += 1
    elif(list7[i] == 'FP'):
        temp2 += 1
    elif(list7[i] == 'TP'):
        temp3 += 1
    elif(list7[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q2 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#PW counfusion and accuracy
print('Q2 confusion for PW: ')
for i in range(50):
    if(list8[i] == 'TN'):
        temp1 += 1
    elif(list8[i] == 'FP'):
        temp2 += 1
    elif(list8[i] == 'TP'):
        temp3 += 1
    elif(list8[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q2 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


print('Question 3:')
print('Q3 (1):')

#Q3 SL EX
list9 = [
1,
0,
0,
0,
0,
0,
0,
0,
1,
1,
0,
1,
0,
0,
0,
1,
0,
0,
0,
1,
1,
0,
0,
1,
0,
0,
1,
1,
1,
0,
0,
1,
0,
1,
0,
1,
1,
1,
1,
0,
0,
0,
0,
1,
0,
1,
0,
1,
0,
0
]

#Q3 SW EX
list10 = [
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1

]

#Q3 PL EX
list11 = [
1,
1,
1,
1,
1,
1,
1,
0,
1,
1,
1,
1,
0,
0,
1,
1,
1,
0,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
0,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1
]

#Q3 PW EX
list12 = [
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1

]

list13 = [None] * 50  #Q3 SL confusion
list14 = [None] * 50  #Q3 SW condusion
list15 = [None] * 50  #Q3 PL confusion
list16 = [None] * 50  #Q3 PW confusion

#Q3 list13，SL confusion matrix

for i in range(50):
    if(list0[i] == 0) and (list9[i] == 0):
        list13[i] = 'TN'

    elif(list0[i] == 0) and (list9[i] == 1):
        list13[i] = 'FP'
    elif(list0[i] == 1) and (list9[i] == 1):
        list13[i] = 'TP'
    elif(list0[i] == 1) and (list9[i] == 0):
        list13[i] = 'FN'
    else:
        continue


#Q3 list14，SW confusion matrix

for i in range(50):
    if (list0[i] == 0) and (list10[i] == 0):
        list14[i] = 'TN'
    elif (list0[i] == 0) and (list10[i] == 1):
        list14[i] = 'FP'
    elif (list0[i] == 1) and (list10[i] == 1):
        list14[i] = 'TP'
    elif (list0[i] == 1) and (list10[i] == 0):
        list14[i] = 'FN'
    else:
        continue

#Q3 list15，PL confusion matrix

for i in range(50):
    if (list0[i] == 0) and (list11[i] == 0):
        list15[i] = 'TN'
    elif (list0[i] == 0) and (list11[i] == 1):
        list15[i] = 'FP'
    elif (list0[i] == 1) and (list11[i] == 1):
        list15[i] = 'TP'
    elif (list0[i] == 1) and (list11[i] == 0):
        list15[i] = 'FN'
    else:
        continue


#Q3 list16，PW confusion matrix

for i in range(50):
    if (list0[i] == 0) and (list12[i] == 0):
        list16[i] = 'TN'
    elif (list0[i] == 0) and (list12[i] == 1):
        list16[i] = 'FP'
    elif (list0[i] == 1) and (list12[i] == 1):
        list16[i] = 'TP'
    elif (list0[i] == 1) and (list12[i] == 0):
        list16[i] = 'FN'
    else:
        continue


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#Q3 SL confusion matrix and accuracy
print('confusion for SL: ')
for i in range(50):
    if(list13[i] == 'TN'):
        temp1 += 1
    elif(list13[i] == 'FP'):
        temp2 += 1
    elif(list13[i] == 'TP'):
        temp3 += 1
    elif(list13[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q3 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')



temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#Q3 SW confusion matrix and accuracy
print('confusion for SW: ')
for i in range(50):
    if(list14[i] == 'TN'):
        temp1 += 1
    elif(list14[i] == 'FP'):
        temp2 += 1
    elif(list14[i] == 'TP'):
        temp3 += 1
    elif(list14[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q3 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#Q3 PL confusion matrix and accuracy
print('confusion for PL: ')
for i in range(50):
    if(list15[i] == 'TN'):
        temp1 += 1
    elif(list15[i] == 'FP'):
        temp2 += 1
    elif(list15[i] == 'TP'):
        temp3 += 1
    elif(list15[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q3 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#Q3 PW confusion matrix and accuracy
print('confusion for PW: ')
for i in range(50):
    if(list16[i] == 'TN'):
        temp1 += 1
    elif(list16[i] == 'FP'):
        temp2 += 1
    elif(list16[i] == 'TP'):
        temp3 += 1
    elif(list16[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q3 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')
print('\n')




print('Question 4:')


print('Q4 (1):')

#X for SL
list17 = [
6,
6.8,
6.2,
6.9,
6.7,
7.2,
6.7,
7.7,
5.5,
5.9,
6.1,
5.6,
7.3,
7.6,
6.5,
5.8,
6.4,
7.7,
6.4,
5.8,
5.7,
6.4,
6.3,
5.5,
6.8,
6.7,
4.9,
6,
4.9,
6.6,
6.4,
6,
6.7,
5.8,
6.5,
5.8,
5.2,
5.8,
5.7,
7.9,
6.7,
6.1,
6.3,
5.5,
6.3,
5,
6.3,
5.6,
6.5,
6.2,

]

#X for SW
list18 = [
3,
2.8,
2.8,
3.2,
3,
3,
3.3,
3.8,
2.4,
3.2,
3,
3,
2.9,
3,
3,
2.7,
3.2,
2.6,
2.9,
2.7,
2.9,
2.8,
2.5,
2.5,
3.2,
3.1,
2.5,
2.2,
2.4,
2.9,
2.8,
3.4,
3.3,
2.7,
2.8,
2.6,
2.7,
2.8,
2.8,
3.8,
3.1,
2.8,
3.4,
2.3,
3.3,
2,
2.8,
3,
3.2,
2.9,

]

#X for PL
list19 = [
4.8,
4.8,
4.8,
5.7,
5,
5.8,
5.7,
6.7,
3.7,
4.8,
4.6,
4.5,
6.3,
6.6,
5.8,
4.1,
4.5,
6.9,
4.3,
5.1,
4.2,
5.6,
5,
4,
5.9,
5.6,
4.5,
5,
3.3,
4.6,
5.6,
4.5,
5.7,
5.1,
4.6,
4,
3.9,
5.1,
4.5,
6.4,
4.4,
4.7,
5.6,
4,
6,
3.5,
5.1,
4.1,
5.1,
4.3,

]

#X for PW
list20 = [
1.8,
1.4,
1.8,
2.3,
1.7,
1.6,
2.1,
2.2,
1,
1.8,
1.4,
1.5,
1.8,
2.1,
2.2,
1,
1.5,
2.3,
1.3,
1.9,
1.3,
2.2,
1.9,
1.3,
2.3,
2.4,
1.7,
1.5,
1,
1.3,
2.1,
1.6,
2.5,
1.9,
1.5,
1.2,
1.4,
2.4,
1.3,
2,
1.4,
1.2,
2.4,
1.3,
2.5,
1,
1.5,
1.3,
2,
1.3

]

#Q4 SL label
list21 = [None] * 50
#Q4 SW label
list22 = [None] * 50
#Q4 PL label
list23 = [None] * 50
#Q4 PW label
list24 = [None] * 50

print('For SL:')
SL_mu_0 = 5.936
SL_sigma_0 = 0.516171
SL_mu_1 = 6.588
SL_sigma_1 = 0.63588

for i in range(50):
    p_0 = norm.pdf((list17[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list17[i] - SL_mu_1) / SL_sigma_1)
    if p_0 >= p_1:
        list21[i] = 0
    else:
        list21[i] = 1

print('label for Q4 SL')
print('============================================================')

print('For SW:')

SW_mu_0 = 2.77
SW_sigma_0 = 0.313798
SW_mu_1 = 2.974
SW_sigma_1 = 0.322497

for i in range(50):
    p_0 = norm.pdf((list18[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list18[i] - SL_mu_1) / SL_sigma_1)
    if p_0 <= p_1:
        list22[i] = 0
    else:
        list22[i] = 1

print('label for Q4 SW')
print('============================================================')





print('For PL:')

PL_mu_0 = 4.26
PL_sigma_0 = 0.469911
PL_mu_1 = 5.552
PL_sigma_1 = 0.551895

for i in range(50):
    p_0 = norm.pdf((list19[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list19[i] - SL_mu_1) / SL_sigma_1)
    if (p_0 - p_1) >= 0:
        list23[i] = 0
    else:
        list23[i] = 1

print('label for Q4 PL')
print('============================================================')




print('For PW:')

PW_mu_0 =  1.326
PW_sigma_0 = 0.197753
PW_mu_1 = 2.026
PW_sigma_1 = 0.27465

for i in range(50):
    p_0 = norm.pdf((list20[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list20[i] - SL_mu_1) / SL_sigma_1)
    if (p_0 - p_1) <= 0:
        list24[i] = 0
    else:
        list24[i] = 1

print('label for Q4 PW')
print('============================================================')



list25 = [None] * 50
list26 = [None] * 50
list27 = [None] * 50
list28 = [None] * 50

#list25，SL confusion matrix
for i in range(50):
    if(list0[i] == 0) and (list21[i] == 0):
        list25[i] = 'TN'
    elif(list0[i] == 0) and (list21[i] == 1):
        list25[i] = 'FP'
    elif(list0[i] == 1) and (list21[i] == 1):
        list25[i] = 'TP'
    elif(list0[i] == 1) and (list21[i] == 0):
        list25[i] = 'FN'
    else:
        continue

#list26，SW confusion matrix
for i in range(50):
    if (list0[i] == 0) and (list22[i] == 0):
        list26[i] = 'TN'
    elif (list0[i] == 0) and (list22[i] == 1):
        list26[i] = 'FP'
    elif (list0[i] == 1) and (list22[i] == 1):
        list26[i] = 'TP'
    elif (list0[i] == 1) and (list22[i] == 0):
        list26[i] = 'FN'
    else:
        continue

#list27，PL confusion matrix
for i in range(50):
    if (list0[i] == 0) and (list23[i] == 0):
        list27[i] = 'TN'
    elif (list0[i] == 0) and (list23[i] == 1):
        list27[i] = 'FP'
    elif (list0[i] == 1) and (list23[i] == 1):
        list27[i] = 'TP'
    elif (list0[i] == 1) and (list23[i] == 0):
        list27[i] = 'FN'
    else:
        continue

#list28，PW confusion matrix

for i in range(50):
    if (list0[i] == 0) and (list24[i] == 0):
        list28[i] = 'TN'
    elif (list0[i] == 0) and (list24[i] == 1):
        list28[i] = 'FP'
    elif (list0[i] == 1) and (list24[i] == 1):
        list28[i] = 'TP'
    elif (list0[i] == 1) and (list24[i] == 0):
        list28[i] = 'FN'
    else:
        continue

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#SL confusion matrix and accuracy
print('confusion for SL: ')
for i in range(50):
    if(list25[i] == 'TN'):
        temp1 += 1
    elif(list25[i] == 'FP'):
        temp2 += 1
    elif(list25[i] == 'TP'):
        temp3 += 1
    elif(list25[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q4 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')



temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#SW confusion matrix and accuracy
print('confusion for SW: ')
for i in range(50):
    if(list26[i] == 'TN'):
        temp1 += 1
    elif(list26[i] == 'FP'):
        temp2 += 1
    elif(list26[i] == 'TP'):
        temp3 += 1
    elif(list26[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q4 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#PL confusion matrix and accuracy
print('confusion for PL: ')
for i in range(50):
    if(list27[i] == 'TN'):
        temp1 += 1
    elif(list27[i] == 'FP'):
        temp2 += 1
    elif(list27[i] == 'TP'):
        temp3 += 1
    elif(list27[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q4 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#PW confusion matrix and accuracy
print('confusion for PW: ')
for i in range(50):
    if(list28[i] == 'TN'):
        temp1 += 1
    elif(list28[i] == 'FP'):
        temp2 += 1
    elif(list28[i] == 'TP'):
        temp3 += 1
    elif(list28[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q4 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


print('Question 5:')

print('Q5 (1):')

#xxxxxxxxxxxxxxxxxxxxxx

#Q5 SL label
list25 = [None] * 50
#Q5 SW label
list26 = [None] * 50
#Q5 PL label
list27 = [None] * 50
#Q5 PW label
list28 = [None] * 50

print('For SL:')
SL_mu_0 = 5.936
SL_sigma_0 = 0.516171
SL_mu_1 = 6.588
SL_sigma_1 = 0.63588

for i in range(50):
    p_0 = norm.pdf((list17[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list17[i] - SL_mu_1) / SL_sigma_1)
    if p_0 >= p_1 and p_0 <= p_1 and (p_0 - p_1) >=0 :
        list25[i] = 0
    else:
        list25[i] = 1

print('label for Q5 SL')
print('============================================================')


print('For SW:')

SW_mu_0 = 2.77
SW_sigma_0 = 0.313798
SW_mu_1 = 2.974
SW_sigma_1 = 0.322497


for i in range(50):
    p_0 = norm.pdf((list18[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list18[i] - SL_mu_1) / SL_sigma_1)
    if p_0 >= p_1 and p_0 <= p_1 and (p_0 - p_1) <=0:
        list26[i] = 0
    else:
        list26[i] = 1

print('label for Q5 SW')
print('============================================================')


print('For PL:')

PL_mu_0 = 4.26
PL_sigma_0 = 0.469911
PL_mu_1 = 5.552
PL_sigma_1 = 0.551895


for i in range(50):
    p_0 = norm.pdf((list19[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list19[i] - SL_mu_1) / SL_sigma_1)
    if p_0 >= p_1 and (p_0 - p_1) >=0 and (p_0 - p_1) <=0  :
        list27[i] = 0
    else:
        list27[i] = 1

print('label for Q5 PL')
print('============================================================')


print('For PW:')

PW_mu_0 =  1.326
PW_sigma_0 = 0.197753
PW_mu_1 = 2.026
PW_sigma_1 = 0.27465


for i in range(50):
    p_0 = norm.pdf((list20[i] - SL_mu_0) / SL_sigma_0)
    p_1 = norm.pdf((list20[i] - SL_mu_1) / SL_sigma_1)
    if p_0 <= p_1 and (p_0 - p_1) >=0 and (p_0 - p_1) <=0 :
        list28[i] = 0
    else:
        list28[i] = 1

print('label for Q5 PW')
print('============================================================')



list29 = [None] * 50
list30 = [None] * 50
list31 = [None] * 50
list32 = [None] * 50

#list29，SL confusion matrix

for i in range(50):
    if(list0[i] == 0) and (list25[i] == 0):
        list29[i] = 'TN'
    elif(list0[i] == 0) and (list25[i] == 1):
        list29[i] = 'FP'
    elif(list0[i] == 1) and (list25[i] == 1):
        list29[i] = 'TP'
    elif(list0[i] == 1) and (list25[i] == 0):
        list29[i] = 'FN'
    else:
        continue


#list30，SWconfusion matrix
for i in range(50):
    if (list0[i] == 0) and (list26[i] == 0):
        list30[i] = 'TN'
        #print('TN')
    elif (list0[i] == 0) and (list26[i] == 1):
        list30[i] = 'FP'
        #print('FP')
    elif (list0[i] == 1) and (list26[i] == 1):
        list30[i] = 'TP'
        #print('TP')
    elif (list0[i] == 1) and (list26[i] == 0):
        list30[i] = 'FN'
        #print('FN')
    else:
        continue


#list31，PL confusion matrix

for i in range(50):
    if (list0[i] == 0) and (list27[i] == 0):
        list31[i] = 'TN'
        #print('TN')
    elif (list0[i] == 0) and (list27[i] == 1):
        list31[i] = 'FP'
        #print('FP')
    elif (list0[i] == 1) and (list27[i] == 1):
        list31[i] = 'TP'
        #print('TP')
    elif (list0[i] == 1) and (list27[i] == 0):
        list31[i] = 'FN'
        #print('FN')
    else:
        continue

#list32，PW confusion matrix

for i in range(50):
    if (list0[i] == 0) and (list28[i] == 0):
        list32[i] = 'TN'
        #print('TN')
    elif (list0[i] == 0) and (list28[i] == 1):
        list32[i] = 'FP'
        #print('FP')
    elif (list0[i] == 1) and (list28[i] == 1):
        list32[i] = 'TP'
        #print('TP')
    elif (list0[i] == 1) and (list28[i] == 0):
        list32[i] = 'FN'
        #print('FN')
    else:
        continue

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#SL confusion matrix and accuracy
print('confusion for SL: ')
for i in range(50):
    if(list29[i] == 'TN'):
        temp1 += 1
    elif(list29[i] == 'FP'):
        temp2 += 1
    elif(list29[i] == 'TP'):
        temp3 += 1
    elif(list29[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q5 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')



temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#SW confusion matrix and accuracy
print('confusion for SW: ')
for i in range(50):
    if(list30[i] == 'TN'):
        temp1 += 1
    elif(list30[i] == 'FP'):
        temp2 += 1
    elif(list30[i] == 'TP'):
        temp3 += 1
    elif(list30[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q5 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#PL confusion matrix and accuracy
print('confusion for PL: ')
for i in range(50):
    if(list31[i] == 'TN'):
        temp1 += 1
    elif(list31[i] == 'FP'):
        temp2 += 1
    elif(list31[i] == 'TP'):
        temp3 += 1
    elif(list31[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q5 Accuracy: %d' % int(temp5 * 100) + '%')

print('=============================================================================')


temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

#PW confusion matrix and accuracy
print('confusion for PW: ')
for i in range(50):
    if(list32[i] == 'TN'):
        temp1 += 1
    elif(list32[i] == 'FP'):
        temp2 += 1
    elif(list32[i] == 'TP'):
        temp3 += 1
    elif(list32[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Q5 Accuracy: %d' % int(temp5 * 100) + '%')

