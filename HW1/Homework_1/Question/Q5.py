import csv
minTemp_3DCVR = []
maxTemp_3DCVR= []
minTempAIS = []
maxTempAIS = []
minTempAE = []
maxTempAE = []
minTempADC = []
maxTempADC = []
minTempAMLS = []
maxTempAMLS = []
minTempBIDA = []
maxTempBIDA = []
minTempBDAr = []
maxTempBDAr = []
minTempBDE = []
maxTempBDE = []
minTempBDA = []
maxTempBDA = []
minTempCDE = []
maxTempCDE = []
minTempCVE = []
maxTempCVE = []
minTempCVSE = []
maxTempCVSE = []
minTempDA = []
maxTempDA = []
minTempDAE = []
maxTempDAE = []
minTempDAL = []
maxTempDAL = []
minTempDAM = []
maxTempDAM = []
minTempDAr = []
maxTempDAr = []
minTempDE = []
maxTempDE = []
minTempDEM = []
maxTempDEM = []
minTempDSC = []
maxTempDSC = []
minTempDSE = []
maxTempDSE = []
minTempDSM = []
maxTempDSM = []
minTempDS = []
maxTempDS = []
minTempDs = []
maxTempDs = []
minTempDoDE = []
maxTempDoDE = []
minTempDoDS = []
maxTempDoDS = []
minTempETLD = []
maxTempETLD = []
minTempFDA = []
maxTempFDA = []
minTempFLDA = []
maxTempFLDA = []
minTempHOD = []
maxTempHOD = []
minTempHODS = []
maxTempHODS = []
minTempHODL = []
maxTempHODL = []
minTempLDA = []
maxTempLDA = []
minTempLDE = []
maxTempLDE = []
minTempLDS = []
maxTempLDS = []
minTempLMLE = []
maxTempLMLE = []
minTempMLD = []
maxTempMLD = []
minTempML_E = []
maxTempML_E = []
minTempMLIE = []
maxTempMLIE = []
minTempMLM = []
maxTempMLM = []
minTempMLS = []
maxTempMLS = []
minTempMDA = []
maxTempMDA = []
minTempMLE = []
maxTempMLE = []
minTempPDA = []
maxTempPDA = []
minTempPDE = []
maxTempPDE = []
minTempPDS = []
maxTempPDS = []
minTempPDDA = []
maxTempPDDA = []
minTempRS = []
maxTempRS = []
minTempSDS = []
maxTempSDS = []


with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="3D Computer Vision Researcher":
          minTemp_3DCVR.append(float(row[7]))
          maxTemp_3DCVR.append(float(row[7]))
    print ("Min Salary of 3D Computer Vision Researcher is ",min(minTemp_3DCVR))
    print ("Max Salary of 3D Computer Vision Researcher is ",max(maxTemp_3DCVR))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="AI Scientist":
          minTempAIS.append(float(row[7]))
          maxTempAIS.append(float(row[7]))
    print ("Min salary of AI Scientist is",min(minTempAIS))
    print ("Max salary of AI Scientist is",max(maxTempAIS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Analytics Engineer":
          minTempAE.append(float(row[7]))
          maxTempAE.append(float(row[7]))
    print ("Min salary of Analytics Engineer is",min(minTempAE))
    print ("Max salary of Analytics Engineer is",max(maxTempAE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Applied Data Scientist":
          minTempADC.append(float(row[7]))
          maxTempADC.append(float(row[7]))
    print ("Min salary of Applied Data Scientist is",min(minTempADC))
    print ("Max salary of Applied Data Scientist is",max(maxTempADC))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Applied Machine Learning Scientist":
          minTempAMLS.append(float(row[7]))
          maxTempAMLS.append(float(row[7]))
    print ("Min salary of Applied Machine Learning Scientist is",min(minTempAMLS))
    print ("Max salary of Applied Machine Learning Scientist is",max(maxTempAMLS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="BI Data Analyst":
          minTempBIDA.append(float(row[7]))
          maxTempBIDA.append(float(row[7]))
    print ("Min salary of Applied Machine Learning Scientist is",min(minTempBIDA))
    print ("Max salary of Applied Machine Learning Scientist is",max(maxTempBIDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Big Data Architect":
          minTempBDAr.append(float(row[7]))
          maxTempBDAr.append(float(row[7]))
    print ("Min salary of Big Data Architect is",min(minTempBDAr))
    print ("Max salary of Big Data Architect is",max(maxTempBDAr))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Big Data Engineer":
          minTempBDE.append(float(row[7]))
          maxTempBDE.append(float(row[7]))
    print ("Min salary of Big Data Engineer is",min(minTempBDE))
    print ("Max salary of Big Data Engineer is",max(maxTempBDE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Business Data Analyst":
          minTempBDA.append(float(row[7]))
          maxTempBDA.append(float(row[7]))
    print ("Min salary of Business Data Analyst is",min(minTempBDA))
    print ("Max salary of Business Data Analyst is",max(maxTempBDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Cloud Data Engineer":
          minTempCDE.append(float(row[7]))
          maxTempCDE.append(float(row[7]))
    print ("Min salary of Cloud Data Engineer is",min(minTempCDE))
    print ("Max salary of Cloud Data Engineer is",max(maxTempCDE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Computer Vision Engineer":
          minTempCVE.append(float(row[7]))
          maxTempCVE.append(float(row[7]))
    print ("Min salary of Computer Vision Engineer is",min(minTempCVE))
    print ("Max salary of Computer Vision Engineer is",max(maxTempCVE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Computer Vision Software Engineer":
          minTempCVSE.append(float(row[7]))
          maxTempCVSE.append(float(row[7]))
    print ("Min salary of Computer Vision Software Engineer is",min(minTempCVSE))
    print ("Max salary of Computer Vision Software Engineer is",max(maxTempCVSE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Analyst":
          minTempDA.append(float(row[7]))
          maxTempDA.append(float(row[7]))
    print ("Min salary of Data Analyst is",min(minTempDA))
    print ("Max salary of Data Analyst is",max(maxTempDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Analytics Engineer":
          minTempDAE.append(float(row[7]))
          maxTempDAE.append(float(row[7]))
    print ("Min salary of Data Analytics Engineer is",min(minTempDAE))
    print ("Max salary of Data Analytics Engineer is",max(maxTempDAE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Analytics Lead":
          minTempDAL.append(float(row[7]))
          maxTempDAL.append(float(row[7]))
    print ("Min salary of Data Analytics Lead is",min(minTempDAL))
    print ("Max salary of Data Analytics Lead is",max(maxTempDAL))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Analytics Manager":
          minTempDAM.append(float(row[7]))
          maxTempDAM.append(float(row[7]))
    print ("Min salary of Data Analytics Manager is",min(minTempDAM))
    print ("Max salary of Data Analytics Manager is",max(maxTempDAM))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Architect":
          minTempDAr.append(float(row[7]))
          maxTempDAr.append(float(row[7]))
    print ("Min salary of Data Architect is",min(minTempDAr))
    print ("Max salary of Data Architectr is",max(maxTempDAr))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Engineer":
          minTempDE.append(float(row[7]))
          maxTempDE.append(float(row[7]))
    print ("Min salary of Data Engineer is",min(minTempDE))
    print ("Max salary of Data Engineer is",max(maxTempDE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Engineering Manager":
          minTempDEM.append(float(row[7]))
          maxTempDEM.append(float(row[7]))
    print ("Min salary of Data Engineering Manager is",min(minTempDEM))
    print ("Max salary of Data Engineering Manager is",max(maxTempDEM))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Science Consultant":
          minTempDSC.append(float(row[7]))
          maxTempDSC.append(float(row[7]))
    print ("Min salary of Data Science Consultant is",min(minTempDSC))
    print ("Max salary of Data Science Consultant is",max(maxTempDSC))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Science Engineer":
          minTempDSE.append(float(row[7]))
          maxTempDSE.append(float(row[7]))
    print ("Min salary of Data Science Engineer is",min(minTempDSE))
    print ("Max salary of Data Science Engineer is",max(maxTempDSE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Science Manager":
          minTempDSM.append(float(row[7]))
          maxTempDSM.append(float(row[7]))
    print ("Min salary of Data Science Manager is",min(minTempDSM))
    print ("Max salary of Data Science Manager is",max(maxTempDSM))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Scientist":
          minTempDS.append(float(row[7]))
          maxTempDS.append(float(row[7]))
    print ("Min salary of Data Scientist is",min(minTempDS))
    print ("Max salary of Data Scientist is",max(maxTempDS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Data Specialist":
          minTempDs.append(float(row[7]))
          maxTempDs.append(float(row[7]))
    print ("Min salary of Data Specialist is",min(minTempDs))
    print ("Max salary of Data Specialist is",max(maxTempDs))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Director of Data Engineering":
          minTempDoDE.append(float(row[7]))
          maxTempDoDE.append(float(row[7]))
    print ("Min salary of Director of Data Engineering is",min(minTempDoDE))
    print ("Max salary of Director of Data Engineering is",max(maxTempDoDE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Director of Data Science":
          minTempDoDS.append(float(row[7]))
          maxTempDoDS.append(float(row[7]))
    print ("Min salary of Director of Data Science is",min(minTempDoDS))
    print ("Max salary of Director of Data Science is",max(maxTempDoDS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="ETL Developer":
          minTempETLD.append(float(row[7]))
          maxTempETLD.append(float(row[7]))
    print ("Min salary of ETL Developer is",min(minTempETLD))
    print ("Max salary of ETL Developer is",max(maxTempETLD))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Finance Data Analyst":
          minTempFDA.append(float(row[7]))
          maxTempFDA.append(float(row[7]))
    print ("Min salary of Finance Data Analyst is",min(minTempFDA))
    print ("Max salary of Finance Data Analyst is",max(maxTempFDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Financial Data Analyst":
          minTempFLDA.append(float(row[7]))
          maxTempFLDA.append(float(row[7]))
    print ("Min salary of Financial Data Analyst is",min(minTempFLDA))
    print ("Max salary of Financial Data Analyst is",max(maxTempFLDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Head of Data":
          minTempHOD.append(float(row[7]))
          maxTempHOD.append(float(row[7]))
    print ("Min salary of Head of Data is",min(minTempHOD))
    print ("Max salary of Head of Data is",max(maxTempHOD))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Head of Data Science":
          minTempHODS.append(float(row[7]))
          maxTempHODS.append(float(row[7]))
    print ("Min salary of Head of Data Science is",min(minTempHODS))
    print ("Max salary of Head of Data Science is",max(maxTempHODS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Head of Machine Learning":
          minTempHODL.append(float(row[7]))
          maxTempHODL.append(float(row[7]))
    print ("Min salary of Head of Machine Learning is",min(minTempHODL))
    print ("Max salary of Head of Machine Learning is",max(maxTempHODL))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Lead Data Analyst":
          minTempLDA.append(float(row[7]))
          maxTempLDA.append(float(row[7]))
    print ("Min salary of Lead Data Analyst is",min(minTempLDA))
    print ("Max salary of Lead Data Analyst is",max(maxTempLDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Lead Data Engineer":
          minTempLDE.append(float(row[7]))
          maxTempLDE.append(float(row[7]))
    print ("Min salary of Lead Data Engineer is",min(minTempLDE))
    print ("Max salary of Lead Data Engineer is",max(maxTempLDE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Lead Data Scientist":
          minTempLDS.append(float(row[7]))
          maxTempLDS.append(float(row[7]))
    print ("Min salary of Lead Data Scientist is",min(minTempLDS))
    print ("Max salary of Lead Data Scientist is",max(maxTempLDS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Lead Machine Learning Engineer":
          minTempLMLE.append(float(row[7]))
          maxTempLMLE.append(float(row[7]))
    print ("Min salary of Lead Machine Learning Engineer is",min(minTempLMLE))
    print ("Max salary of Lead Machine Learning Engineer is",max(maxTempLMLE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Machine Learning Developer":
          minTempMLD.append(float(row[7]))
          maxTempMLD.append(float(row[7]))
    print ("Min salary of Machine Learning Developer is",min(minTempMLD))
    print ("Max salary of Machine Learning Developer is",max(maxTempMLD))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Machine Learning Engineer":
          minTempML_E.append(float(row[7]))
          maxTempML_E.append(float(row[7]))
    print ("Min salary of Machine Learning Engineer is",min(minTempML_E))
    print ("Max salary of Machine Learning Engineer is",max(maxTempML_E))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Machine Learning Infrastructure Engineer":
          minTempMLIE.append(float(row[7]))
          maxTempMLIE.append(float(row[7]))
    print ("Min salary of Machine Learning Infrastructure Engineer is",min(minTempMLIE))
    print ("Max salary of Machine Learning Infrastructure Engineer is",max(maxTempMLIE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Machine Learning Manager":
          minTempMLM.append(float(row[7]))
          maxTempMLM.append(float(row[7]))
    print ("Min salary of Machine Learning Manager is",min(minTempMLM))
    print ("Max salary of Machine Learning Manager is",max(maxTempMLM))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Machine Learning Scientist":
          minTempMLS.append(float(row[7]))
          maxTempMLS.append(float(row[7]))
    print ("Min salary of Machine Learning Scientist is",min(minTempMLS))
    print ("Max salary of Machine Learning Scientist is",max(maxTempMLS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Marketing Data Analyst":
          minTempMDA.append(float(row[7]))
          maxTempMDA.append(float(row[7]))
    print ("Min salary of Marketing Data Analyst is",min(minTempMDA))
    print ("Max salary of Marketing Data Analyst is",max(maxTempMDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="ML Engineer":
          minTempMLE.append(float(row[7]))
          maxTempMLE.append(float(row[7]))
    print ("Min salary of ML Engineer is",min(minTempMLE))
    print ("Max salary of ML Engineer is",max(maxTempMLE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Principal Data Analyst":
          minTempPDA.append(float(row[7]))
          maxTempPDA.append(float(row[7]))
    print ("Min salary of Principal Data Analyst is",min(minTempPDA))
    print ("Max salary of Principal Data Analyst is",max(maxTempPDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Principal Data Engineer":
          minTempPDE.append(float(row[7]))
          maxTempPDE.append(float(row[7]))
    print ("Min salary of Principal Data Engineer is",min(minTempPDE))
    print ("Max salary of Principal Data Engineer is",max(maxTempPDE))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Principal Data Scientist":
          minTempPDS.append(float(row[7]))
          maxTempPDS.append(float(row[7]))
    print ("Min salary of Principal Data Scientist is",min(minTempPDS))
    print ("Max salary of Principal Data Scientist is",max(maxTempPDS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Product Data Analyst":
          minTempPDDA.append(float(row[7]))
          maxTempPDDA.append(float(row[7]))
    print ("Min salary of Product Data Analyst is",min(minTempPDDA))
    print ("Max salary of Product Data Analyst is",max(maxTempPDDA))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Research Scientist":
          minTempRS.append(float(row[7]))
          maxTempRS.append(float(row[7]))
    print ("Min salary of Research Scientist is",min(minTempRS))
    print ("Max salary of Research Scientist is",max(maxTempRS))
with open('ds_salaries.csv', 'r',newline="") as csvfile:
    my_reader = csv.reader(csvfile,)
    for row in my_reader:
         if row[4] =="Staff Data Scientist":
          minTempSDS.append(float(row[7]))
          maxTempSDS.append(float(row[7]))
    print ("Min salary of Staff Data Scientist is",min(minTempSDS))
    print ("Max salary of Staff Data Scientist is",max(maxTempSDS))
