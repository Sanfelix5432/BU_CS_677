import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

X = [
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
##year 1

Y = [1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0]
##Year 1正确答案
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(X,Y)

print("q1: ")
print("-----------------------------------------------------------------------------------------------------------------")
b0 = model.intercept_
b1 = model.coef_
b1_1 = b1.mean()
print("The equation of Logistic Regression is:")
print("y = e^(",b0,"+",b1_1,"*x)","/(1 + e^(",b0,"+",b1_1,"*x))")
print("ln(y/1-y) = ",b0,"+",b1_1,"*x")
print("=================================================================================================================")

print("q2: ")
print("q3: ")

#Year 2
data_test = [
[1,0.096,1.243153249],	
[2,-0.062,0.579974137],
[3,-0.175,0.662746809],
[4,0.098,0.849099523],
[5,0.42,1.606782499],
[6,0.214,0.461226625],
[7,-0.6675,1.011743545],
[8,0.024,0.779442108],
[9,0.156,0.970376216],
[10,-0.288,0.790044303],
[11,-0.15,1.279120792],
[12,0.254,0.365554374],
[13,0.452,	0.414813211],
[14,0.0925,0.753364675],
[15,0.172,0.744123646],
[16,-0.178,1.229845519],
[17,-0.624,0.676779137],
[18,0.136,0.108074049],
[19,0.494,0.363703176],
[20,0.654,2.234699085],
[21,-0.3975,1.4106352],
[22,0.198,0.661452946],
[23,0.296,0.870591753],
[24,1.222,1.318529484],
[25,-0.234,1.313955859],
[26,0.6575,0.747010709],
[27,-1.654,3.138053537],
[28,-0.582,1.712270423],
[29,-0.338,1.277329245],
[30,0.536,0.989282568],
[31,-0.572,1.130318539],
[32,-0.39,0.578402974],
[33,0.732,0.659674162],
[34,0.672,1.030422244],
[35,0.042,2.37052104],
[36,-0.7275,0.86988026],
[37,0.124,1.232550202],
[38,0.244,0.947591684],
[39,-0.078,0.870241346],
[40,0.682,1.799588842],
[41,-1.37,1.007000497],
[42,-0.174,0.751851049],
[43,0.372,1.071806886],
[44,0.484,2.39685836],
[45,-0.566,2.357685306],
[46,1.616,3.988537326],
[47,1.0325,1.504490501],
[48,0.984,3.02159395],
[49,0.946,3.357153556],
[50,-0.014,2.483511627],
[51,-0.9625,3.772553291],
[52,-0.5,6.570941079]
]
print(model.predict(data_test))

#Year 2 标准label
list0 = [0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1]
#Year 2 预测label
listl = [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1]

listl_1 = [None] * 52

print("The confusion matrix for Year 2:")

for i in range(52):
    if(list0[i] == 0) and (listl[i] == 0):
        listl_1[i] = 'TN'
    elif(list0[i] == 0) and (listl[i] == 1):
        listl_1[i] = 'FP'
    elif(list0[i] == 1) and (listl[i] == 1):
        listl_1[i] = 'TP'
    elif(list0[i] == 1) and (listl[i] == 0):
        listl_1[i] = 'FN'
    else:
        continue
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in range(50):
    if(listl_1[i] == 'TN'):
        temp1 += 1
    elif(listl_1[i] == 'FP'):
        temp2 += 1
    elif(listl_1[i] == 'TP'):
        temp3 += 1
    elif(listl_1[i] == 'FN'):
        temp4 += 1
    else:
        continue
print('TP: %d' % temp3 )
print('TN: %d' % temp1 )
print('FP: %d' % temp2 )
print('FN: %d' % temp4 )
temp5 = (temp1+temp3)/(temp1+temp2+temp3+temp4)
print('Accuracy: %d' % int(temp5 * 100) + '%')
print("=================================================================================================================")

print("q4: ")
print("-----------------------------------------------------------------------------------------------------------------")

temp6 = temp3/(temp3+temp4)
temp7 = temp1/(temp1+temp2)
print('TPR: %f' % temp6)
print('TNR: %f' % temp7)