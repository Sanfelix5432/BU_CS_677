import csv
salaries_0 = []
salaries_50 = []
salaries_100 = []
ratio = []
total_ratio = []
counter = 0
with open('ds_salaries.csv', 'r',newline="") as csvfile:
      my_reader = list(csv.reader(csvfile,))
      for row in my_reader[1:]:
          if row[9]=="0":
              salaries_0.append(float(row[7]))
              ratio.append(float(row[9]))
          elif row[9]=="50":
              salaries_50.append(float(row[7]))
              ratio.append(float(row[9]))
          elif row[9]=="100":
              salaries_100.append(float(row[7]))
              ratio.append(float(row[9]))
              
                  
              

                  
      AvgSalaries_0 = sum(salaries_0)/len(ratio)
      AvgSalaries_50 = sum(salaries_50)/len(ratio)
      AvgSalaries_100 = sum(salaries_100)/len(ratio)
      print("The average salary for 0 remote ratio is  :",AvgSalaries_0)
      print("The average salary for 50 remote ratio is  :",AvgSalaries_50)
      print("The average salary for 100 remote ratio is  :",AvgSalaries_100)

      for row in my_reader[1:]:
          total_ratio.append(float(row[9]))
      print("There are",len(set(total_ratio)),"entry/entries","They are:",set(total_ratio))
          
      
