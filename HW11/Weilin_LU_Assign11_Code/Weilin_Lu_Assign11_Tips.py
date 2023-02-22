import pandas as pd
import numpy as np
import csv
print('Question 1:')
data = pd.read_csv("tips.csv")

lunch_tip = 0.0
dinner_tip= 0.0

lunch_sum = 0.0
dinner_sum = 0.0
for i in range(len(data)):
    if(data.loc[i,'time']) == 'Lunch':
        lunch_tip += data.loc[i,'tip']
        lunch_sum += data.loc[i, 'total_bill']
    elif(data.loc[i,'time']) == 'Dinner':
        dinner_tip += data.loc[i, 'tip']
        dinner_sum += data.loc[i, 'total_bill']
    else:
        pass


l = round(lunch_tip/lunch_sum,2)
d = round(dinner_tip/dinner_sum,2)
l1 = l*100
d1 = d*100
print('The average tip:')
print('LUNCH: %.2f' %l1 +'%')
print('DINNER: %.2f' %d1 +'%')
print('**************************************************************************************************')

print('Question 2:')
tip_4 = 0.0
tip_5 = 0.0
tip_6 = 0.0
tip_7 = 0.0
tip_4_sum = 0.0
tip_5_sum = 0.0
tip_6_sum = 0.0
tip_7_sum = 0.0
for i in range(len(data)):
    if(data.loc[i,'day']) == 'Thur':
        tip_4 += data.loc[i,'tip']
        tip_4_sum += data.loc[i, 'total_bill']
    elif(data.loc[i,'day']) == 'Fri':
        tip_5 += data.loc[i, 'tip']
        tip_5_sum += data.loc[i, 'total_bill']
    elif (data.loc[i, 'day']) == 'Sat':
        tip_6 += data.loc[i, 'tip']
        tip_6_sum += data.loc[i, 'total_bill']
    elif (data.loc[i, 'day']) == 'Sun':
        tip_7 += data.loc[i, 'tip']
        tip_7_sum += data.loc[i, 'total_bill']
    else:
        pass

tip_4 = round(tip_4/tip_4_sum,2)
tip_5 = round(tip_5/tip_5_sum,2)
tip_6 = round(tip_6/tip_6_sum,2)
tip_7 = round(tip_7/tip_7_sum,2)

l4 = tip_4 * 100
l5 = tip_5 * 100
l6 = tip_6 * 100
l7 = tip_7 * 100

print('The average tip:')
print('THURSDAY: %.2f' %l4 +'%')
print('FRIDDAY: %.2f' %l5 +'%')
print('SATURDAY: %.2f' %l6 +'%')
print('SUNDAY: %.2f' %l7 +'%')
print('**************************************************************************************************')

print('Question 3:')

max_tip = 0.0
count = 0

for i in range(len(data)):
    if(data.loc[i,'tip']) > max_tip:
        max_tip = data.loc[i,'tip']
        count = i
print('The highest tip:' + str(max_tip))
print('Date:' + str(data.loc[count,'day']))
print('Time:' + str(data.loc[count, 'time']))
print('**************************************************************************************************')

print('Question 4:')

data2 = data[['total_bill','tip']]
print(data2.corr())
print('**************************************************************************************************')

print('Question 5:')

data3 = data[['tip','size']]
print(data3.corr())
print('**************************************************************************************************')

print('Question 6:')

count_smk = 0

count_sum = 0

data4 = data[['smoker','size']]
for i in range(len(data4)):
    if(data.loc[i,'smoker'] == 'Yes'):
        count_smk += data.loc[i,'size']
        count_sum += data.loc[i, 'size']

    elif(data.loc[i,'smoker'] == 'No'):
        count_sum += data.loc[i,'size']

count_smk2 = (round(count_smk/count_sum,2)) * 100
print('The percentage of smoking people is: %.2f ' %count_smk2 +'%')
print('**************************************************************************************************')


print('Question 7:')
print('In each day,tip are not increasing with the time')
print('**************************************************************************************************')

print('Question 8:')

tip_smk = 0.0
tip_nsmk = 0.0
count_nsmk = 0

for i in range(len(data4)):
    if(data.loc[i,'smoker'] == 'Yes'):
        count_smk += data.loc[i,'size']
        tip_smk += data.loc[i, 'tip']

    elif(data.loc[i,'smoker'] == 'No'):
        count_nsmk += data.loc[i,'size']
        tip_nsmk += data.loc[i, 'tip']

tip_smk2 = (round(tip_smk/count_smk,2))
tip_nsmk2 = (round(tip_nsmk/count_nsmk,2))
print('The average tip:')
print('Smoking people: %.2f ' %tip_smk2)
print('Non smoking people: %.2f ' %tip_nsmk2)
print('**************************************************************************************************')