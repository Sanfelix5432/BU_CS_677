import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.stats import norm
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
#train(choose any 52 weeks) 随便选52周的平均值和标准差以及
data2 = [
[1,-0.09,0.299583044,1],
[2,-0.012,0.132174128,1],	
[3,-0.062,0.023874673,1],
[4,-0.16,0.175641681,1],		
[5,-0.12,0.199874961,1],
[6,0.224,0.148425065,0],	
[7,0.308,0.976611489,0],	
[8,-0.16,0.423969339,1],
[9,0.425,0.990168336,0],
[10,0.28,1.498065419,0],
[11,-0.076,0.849399788,1],
[12,-0.624,1.651735451,1],
[13,-0.526,1.213148795,1],	
[14,0.0175,0.798931578,0],		
[15,0.032,0.655949693,0],	
[16,0.154,0.404264765,0],
[17,-0.424,0.351539471,1],
[18,0.046,0.41506626,0],
[19,-0.038,0.122759928,1],
[20,0.056,0.273276417,0],
[21,-0.148,0.52485236,1],
[22,0.188,0.369012195,0],	
[23,-0.2125,0.535435959,1],
[24,0.292,0.593481255,0],
[25,-0.248,0.521890793,1],
[26,0.392,0.178521707,0],	
[27,-0.246,0.42571117,1],
[28,0.186,0.694895676,0],	
[29,-0.208,0.498266997,1],	
[30,0.14,0.663287268,0],	
[31,-0.156,0.616952186,1],	
[32,-0.192,0.484221024,1],
[33,0.086,0.521277277,0],	
[34,0.2425,1.154220516,0],	
[35,0.092,0.736525628,0],	
[36,-0.345,0.840694158,1],		
[37,0.014,0.328222486,0],	
[38,-0.618,0.785792594,1],	
[39,0.435,0.291376046,0],
[40,0.02,0,0],
[41,0.5,0.869741341,0]	,	
[42,0.156,0.323001548,0],
[43,0.1375,0.491010862,0],	
[44,-0.016,0.536078352,1],	
[45,-0.012,0.52803409,1],	
[46,-0.152,0.472831894,1],
[47,0.245,0.577840809,0],
[48,-0.672,0.834188228,1],	
[49,0.292,0.746438209,0],	
[50,0.058,0.445555833,0],
[51,-0.33,0.368306937,1],
[52,0.284,0.246840029,0]

]
#year 1 test 你所选区的第一年的数据
data3= [
[1,0.5,0.869741341],	
[2,0.156,0.323001548],		
[3,0.1375,0.491010862],		
[4,-0.016,0.536078352],
[5,-0.012,0.52803409],
[6,-0.152,0.472831894],
[7,0.245,0.577840809],
[8,-0.672,0.834188228],	
[9,0.292,0.746438209],	
[10,0.058,0.445555833],	
[11,-0.33,0.368306937],	
[12,0.284,0.246840029],
[13,-0.228,0.529688588],
[14,0,0.31136795],
[15,-0.2925,0.557157967],
[16,0.24,0.297153159],
[17,0.068,0.181300855],
[18,0.058,0.229934773],
[19,-0.306,0.587690395],
[20,-0.176,0.245519857],
[21,-0.1575,0.140089257],
[22,0.224,0.465274113],
[23,-0.102,0.299449495],		
[24,0.16,0.241971073],
[25,0.174,0.336645214],
[26,0.0925,0.13671747],
[27,-0.026,0.208997608],
[28,-0.234,0.231149302],
[29,-0.06,0.16263456],
[30,-0.222,0.279051966],	
[31,-0.2,0.15411035],	
[32,0.13,0.058309519],
[33,-0.058,0.199924986],
[34,-0.208,0.350385502],
[35,0.0375,0.52442826],	
[36,0.078,0.334394976],	
[37,0.086,0.181190507,],
[38,-0.182,0.437515714],
[39,-0.092,0.319092463],	
[40,-0.07,0.177623197],	
[41,0.02,0.168522995],	
[42,0.222,0.431300359],
[43,0.182,0.187936159],
[44,-0.054,0.293052896],
[45,0.066,0.358371316],
[46,-0.094,0.739209037],
[47,0.2025,0.208706333],
[48,0.026,0.321605348],
[49,0.122,0.244887729],	
[50,-0.074,0.18622567],
[51,0.06,0.244267613],		
[52,0.16,0.127279221]
]
datamat = np.array(data2)
X = datamat[:,0:3]
Y = datamat[:,3]
knn = KNeighborsClassifier(n_neighbors=11,weights='distance')
knn.fit(X,Y)
print("k* = k = 9")
print(knn.predict([data3[0]]))
print(knn.predict([data3[1]]))
print(knn.predict([data3[2]]))
print(knn.predict([data3[3]]))
print(knn.predict([data3[4]]))
print(knn.predict([data3[5]]))
print(knn.predict([data3[6]]))
print(knn.predict([data3[7]]))
print(knn.predict([data3[8]]))
print(knn.predict([data3[9]]))
print(knn.predict([data3[10]]))
print(knn.predict([data3[11]]))
print(knn.predict([data3[12]]))
print(knn.predict([data3[13]]))
print(knn.predict([data3[14]]))
print(knn.predict([data3[15]]))
print(knn.predict([data3[16]]))
print(knn.predict([data3[17]]))
print(knn.predict([data3[18]]))
print(knn.predict([data3[19]]))
print(knn.predict([data3[20]]))
print(knn.predict([data3[21]]))
print(knn.predict([data3[22]]))
print(knn.predict([data3[23]]))
print(knn.predict([data3[24]]))
print(knn.predict([data3[25]]))
print(knn.predict([data3[26]]))
print(knn.predict([data3[27]]))
print(knn.predict([data3[28]]))
print(knn.predict([data3[29]]))
print(knn.predict([data3[30]]))
print(knn.predict([data3[31]]))
print(knn.predict([data3[32]]))
print(knn.predict([data3[33]]))
print(knn.predict([data3[34]]))
print(knn.predict([data3[35]]))
print(knn.predict([data3[36]]))
print(knn.predict([data3[37]]))
print(knn.predict([data3[38]]))
print(knn.predict([data3[39]]))
print(knn.predict([data3[40]]))
print(knn.predict([data3[41]]))
print(knn.predict([data3[42]]))
print(knn.predict([data3[43]]))
print(knn.predict([data3[44]]))
print(knn.predict([data3[45]]))
print(knn.predict([data3[46]]))
print(knn.predict([data3[47]]))
print(knn.predict([data3[48]]))
print(knn.predict([data3[49]]))
print(knn.predict([data3[50]]))
print(knn.predict([data3[51]]))
print("###################################################################")

list3 = [1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0] #第一年正确的结果
list4 = [1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0] #第一年预测出来的结果

list5 = [None] * 52

for i in range(50):
    if(list3[i] == 0) and (list4[i] == 0):
        list5[i] = 'TN'
    elif(list3[i] == 0) and (list4[i] == 1):
        list5[i] = 'FP'
    elif(list3[i] == 1) and (list4[i] == 1):
        list5[i] = 'TP'
    elif(list3[i] == 1) and (list4[i] == 0):
        list5[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(52):
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
print('Accuracy: %d' % int(temp5 * 100) + '%')
temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('Sensitivity: %f' % temp6)
print('Specificity: %f' % temp7)