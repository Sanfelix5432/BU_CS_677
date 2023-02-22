
list = [1,2,3,4,5]
list2 = [5,4,3,2,1]

p1 = 0.0
p2 = 0.0

list3 = [None] * 100
#print(list3)

x= 0
for i in range(100):
    x += 0.001
    list3[i] = round(x,4)

#print(list3)



p_long = 0.0
p_short = 0.0
money = 100
stock_num = 0.0


count = 0
count_long = 0
count_short = 0



list1 = [273.309998,
282.73999,
268.01001,
271.790009,
273.549988,
264.170013,
263.420013,
267.26001,
266.5,
271.170013,
276.850006,
275.660004,
273.140015,
279.450012,
285.390015,
285.970001,
289.149994,
291.339996,
287.049988,
270.950012,
280.109985,
263.179993,
265.920013,
239.039993,
249.559998
]
list2 = [273.920013,
283.290009,
257.630005,
274.709991,
274.100006,
258.049988,
259.720001,
266.570007,
266.920013,
273.359985,
278.190002,
274.73999,
275.420013,
280.200012,
285.459991,
285.790009,
288.160004,
291.019989,
287.820007,
273.609985,
280.5,
263.25,
269.839996,
234.339996,
249.919998
]






for i in range(len(list1)-1):
    if(list2[i] > list1[i]):
        stock_num = round(money / list2[i] , 2)
        a = money
        money = 0.0
        money = stock_num * list1[i+1]
        print("Day" + str(i+1) + "increase，"+"Day" + str(i+1) + "buy when close")
        print("Day" + str(i + 2) + "sell when open")
        print('Left'+str(round(money,2))+"$")

        count_long += 1
        count +=1

        p1 = money - a
        print("Day"+ str(i+1) + "earn" + str(round(p1,2)) +'$')
        p_long += p1

        print("Long profit：" + str(round(p_long,2)) + '$')
        print(list2[i] / list1[i] -1)
        print('================')

    elif(list2[i] < list1[i]):
        stock_num = round(money / list1[i], 2)
        b = money
        money = 0.0
        money = stock_num * list2[i]
        print("Day" + str(i + 1) + "decrease，" + "Day" + str(i + 1) + "buy when open")
        print("Day" + str(i + 1) + "sell when close")
        print('Left' + str(round(money, 2)) + "$")

        count_short += 1
        count += 1

        p2 = money - b
        print("Day" + str(i + 1) + "Lose" + str(round(p2, 2)) + '$')
        p_short += p2

        print("Short profit：" + str(round(p_short, 2)) + '$')
        print(list2[i] / list1[i] -1)
        print('================')


    elif (list2[i] == list1[i]):
        print("Day" + str(i + 1) + "no change, no trade")
        print(list2[i] / list1[i] -1)
        print('================')

    else:
        continue


ave_p = (money - 100)/count
print("average nightly profit: " + str(round(ave_p,2)) + "%" )

sum_p = (money - 100)
print("sum profit: " + str(round(sum_p,2)) +'$' )


p_long = round(p_long,2)
p_short = round(p_short,2)


print("long position profit: " + str(p_long) + '$')
print("short position profit: " + str(p_short) + '$')
print('==========')
print('\n')


print(count_long)
print(count_short)

list4 = [None] * 100
d = 0

list5 = [None] * 100
temp1 = 0

list6 = [None] * 100
temp2 = 0

for k in list3:
    print("The x value is：" + str(round(k * 100,4)) +'%')


    for i in range(len(list1) - 1):
        if ((list2[i] > list1[i]) and (list2[i]/list1[i]) > k-1 ):
            stock_num = round(money / list2[i], 2)
            a = money
            money = 0.0
            money = stock_num * list1[i + 1]

            count_long += 1
            count += 1

            p1 = money - a

            p_long += p1


        elif ((list2[i] < list1[i]) and (list2[i]/list1[i]) > k-1):
            stock_num = round(money / list1[i], 2)
            b = money
            money = 0.0
            money = stock_num * list2[i]

            count_short += 1
            count += 1

            p2 = money - b

            p_short += p2


        elif (list2[i] == list1[i]):
            continue


        else:
            continue

    ave_p = (money - 100) / count
    list4[d] = round(ave_p,4)
    d += 1

    ave_p_long = p_long / count_long
    ave_p_short = p_short /count_short

    list5[temp1] = ave_p_long
    temp1 +=1
    list6[temp2] = ave_p_short
    temp2 += 1


    print("Average profir for each night: " + str(round(ave_p,4)) + "%")
    print("Average profir for each night of long keep: " + str(round(ave_p_long, 4)) + "%")
    print("Average profir for each night of short keep: " + str(round(ave_p_short, 4)) + "%")

    print('===================================')


#print(*list4,sep='\n')
print('===================================')
#print(*list3,sep='\n')

print(*list5,sep='\n')
print('===================================')
print(*list6,sep='\n')


