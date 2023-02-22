import csv
minTemp = []
maxTemp = []
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
        if row[4]== "":
          minTemp.append(float(row[7]))
          maxTemp.append(float(row[7]))
    print ("Max Salary of 3D Computer Vision Researcher is ",min(minTemp))
    print ("Min Salary of 3D Computer Vision Researcher is ",max(maxTemp))        
