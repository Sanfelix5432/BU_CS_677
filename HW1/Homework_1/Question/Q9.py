import csv
salary_in_usd = []
country = []
with open('ds_salaries.csv', 'r',newline="") as csvfile:
      my_reader = list(csv.reader(csvfile,))
      for row in my_reader[1:]:
          salary_in_usd.append(float(row[7]))
          usd_index = salary_in_usd.index(max(salary_in_usd))
          usd_index_min = salary_in_usd.index(min(salary_in_usd))
          country.append(row[10])
          
      print("line:",usd_index_min,"Salary:",min(salary_in_usd),"Location:",country[usd_index_min])
      print("line:",usd_index,"Salary:",max(salary_in_usd),"Location:",country[usd_index])
