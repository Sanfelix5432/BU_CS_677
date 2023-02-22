import csv
#2020
Salaries_RS_2020 = []
Salaries_PDDA_2020 = []
Salaries_PDS_2020 = []
Salaries_MLE_2020 = []
Salaries_MLS_2020 = []
Salaries_MLM_2020 = []
Salaries_MLIE_2020 = []
Salaries_ML_E_2020 = []
Salaries_LDS_2020 = []
Salaries_LDE_2020 = []
Salaries_LDA_2020 = []
Salaries_DoDS_2020 = []
Salaries_DS_2020 = []
Salaries_DSM_2020 = []
Salaries_DSC_2020 = []
Salaries_DEM_2020 = []
Salaries_DE_2020 = []
Salaries_DA_2020 = []
Salaries_CVE_2020 = []
Salaries_BDA_2020 = []
Salaries_BIDA_2020 = []
Salaries_BDE_2020 = []
Salaries_AIS_2020 = []
#2021
Salaries_SDS_2021 = []
Salaries_RS_2021 = []
Salaries_PDS_2021 = []
Salaries_PDA_2021 = []
Salaries_PDE_2021 = []
Salaries_MLE_2021 = []
Salaries_MDA_2021 = []
Salaries_MLS_2021 = []
Salaries_MLIE_2021 = []
Salaries_ML_E_2021 = []
Salaries_MLD_2021 = []
Salaries_LDS_2021 = []
Salaries_LDE_2021 = []
Salaries_LDA_2021 = []
Salaries_HoDS_2021 = []
Salaries_HOD_2021 = []
Salaries_FLDA_2021 = []
Salaries_FDA_2021 = []
Salaries_DoDS_2021 = []
Salaries_DoDE_2021 = []
Salaries_DSL_2021 = []
Salaries_DS_2021 = []
Salaries_DSM_2021 = []
Salaries_DSE_2021 = []
Salaries_DSC_2021 = []
Salaries_DEM_2021 = []
Salaries_DE_2021 = []
Salaries_DAr_2021 = []
Salaries_DAM_2021 = []
Salaries_DAE_2021 = []
Salaries_DA_2021 = []
Salaries_CVSE_2021 = []
Salaries_CVE_2021 = []
Salaries_CDE_2021 = []
Salaries_BDA_2021 = []
Salaries_BDE_2021 = []
Salaries_BDAr_2021 = []
Salaries_BIDA_2021 = []
Salaries_AMLS_2021 = []
Salaries_ADS_2021 = []
Salaries_AIS_2021 = []
Salaries_3DCVR_2021 = []
#2022
Salaries_RS_2022 = []
Salaries_PDS_2022 = []
Salaries_PDA_2022 = []
Salaries_NLPE_2022 = []
Salaries_MLE_2022 = []
Salaries_MLS_2022 = []
Salaries_MLIE_2022 = []
Salaries_ML_E_2022 = []
Salaries_LMLE_2022 = []
Salaries_LDE_2022 = []
Salaries_HoML_2022 = []
Salaries_HoDS_2022 = []
Salaries_FLDA_2022 = []
Salaries_ETLD_2022 = []
Salaries_DoDS_2022 = []
Salaries_DS_2022 = []
Salaries_DSM_2022 = []
Salaries_DSE_2022 = []
Salaries_DE_2022 = []
Salaries_DAr_2022 = []
Salaries_DAM_2022 = []
Salaries_DAL_2022 = []
Salaries_DAE_2022 = []
Salaries_DA_2022 = []
Salaries_CVSE_2022 = []
Salaries_CVE_2022 = []
Salaries_BDA_2022 = []
Salaries_AMLS_2022 = []
Salaries_AE_2022 = []
Salaries_AIS_2022 = []
with open('ds_salaries.csv', 'r',newline="") as csvfile:
      my_reader = list(csv.reader(csvfile,))
      for row in my_reader[1:]:
           if row[1]=="2020":                 
              if row[4]=="Research Scientist":
                Salaries_RS_2020.append(float(row[7]))
              elif row[4]=="Product Data Analyst":
                Salaries_PDDA_2020.append(float(row[7]))
              elif row[4]=="Principal Data Scientist":
                Salaries_PDS_2020.append(float(row[7]))                
              elif row[4]=="ML Engineer":
                Salaries_MLE_2020.append(float(row[7]))                
              elif row[4]=="Machine Learning Scientist":
                Salaries_MLS_2020.append(float(row[7])) 
              elif row[4]=="Machine Learning Manager":
                Salaries_MLM_2020.append(float(row[7]))
              elif row[4]=="Machine Learning Infrastructure Engineer":
                Salaries_MLIE_2020.append(float(row[7]))                
              elif row[4]=="Machine Learning Engineer":
                Salaries_ML_E_2020.append(float(row[7]))                
              elif row[4]=="Lead Data Scientist":
                Salaries_LDS_2020.append(float(row[7]))
              elif row[4]=="Lead Data Engineer":                  
                Salaries_LDE_2020.append(float(row[7]))                
              elif row[4]=="Lead Data Analyst":
                Salaries_LDA_2020.append(float(row[7]))                
              elif row[4]=="Director of Data Science":
                Salaries_DoDS_2020.append(float(row[7])) 
              elif row[4]=="Data Scientist":
                Salaries_DS_2020.append(float(row[7]))                
              elif row[4]=="Data Science Manager":
                Salaries_DSM_2020.append(float(row[7]))                
              elif row[4]=="Data Science Consultant":
                Salaries_DSC_2020.append(float(row[7]))              
              elif row[4]=="Data Engineering Manager":
                Salaries_DEM_2020.append(float(row[7]))           
              elif row[4]=="Data Engineer":
                Salaries_DE_2020.append(float(row[7])) 
              elif row[4]=="Data Analyst":
                Salaries_DA_2020.append(float(row[7]))
              elif row[4]=="Computer Vision Engineer":
                Salaries_CVE_2020.append(float(row[7]))
              elif row[4]=="Business Data Analyst":
                Salaries_BDA_2020.append(float(row[7]))
              elif row[4]=="Big Data Engineer":
                Salaries_BDE_2020.append(float(row[7]))
              elif row[4]=="BI Data Analyst":
                Salaries_BIDA_2020.append(float(row[7]))
              elif row[4]=="AI Scientist":
                Salaries_AIS_2020.append(float(row[7]))
           elif row[1]=="2021":
              if row[4]=="Staff Data Scientist":
                Salaries_RS_2021.append(float(row[7]))
              elif row[4]=="Research Scientist":
                Salaries_RS_2021.append(float(row[7]))
              elif row[4]=="Principal Data Scientist":
                Salaries_PDS_2021.append(float(row[7])) 
              elif row[4]=="Principal Data Analyst":
                Salaries_PDA_2021.append(float(row[7])) 
              elif row[4]=="ML Engineer":
                Salaries_MLE_2021.append(float(row[7]))
              elif row[4]=="Marketing Data Analyst":
                Salaries_MDA_2021.append(float(row[7]))
              elif row[4]=="Machine Learning Scientist":
                Salaries_MLS_2021.append(float(row[7])) 
              elif row[4]=="Machine Learning Infrastructure Engineer":
                Salaries_MLIE_2021.append(float(row[7])) 
              elif row[4]=="Machine Learning Engineer":
                Salaries_ML_E_2021.append(float(row[7])) 
              elif row[4]=="Machine Learning Developer":
                Salaries_MLD_2021.append(float(row[7])) 
              elif row[4]=="Lead Data Scientist":
                Salaries_LDS_2021.append(float(row[7]))
              elif row[4]=="Lead Data Engineer":                  
                Salaries_LDE_2021.append(float(row[7]))  
              elif row[4]=="Lead Data Analyst":
                Salaries_LDA_2021.append(float(row[7]))
              elif row[4]=="Head of Data Science":
                Salaries_HoDS_2021.append(float(row[7]))
              elif row[4]=="Head of Data":
                Salaries_HOD_2021.append(float(row[7]))
              elif row[4]=="Financial Data Analyst":
                Salaries_FLDA_2021.append(float(row[7]))
              elif row[4]=="Finance Data Analyst":
                Salaries_FDA_2021.append(float(row[7]))
              elif row[4]=="Director of Data Science":
                Salaries_DoDS_2021.append(float(row[7]))
              elif row[4]=="Director of Data Engineering":
                Salaries_DoDE_2021.append(float(row[7]))
              elif row[4]=="Data Specialist":
                Salaries_DSL_2021.append(float(row[7]))
              elif row[4]=="Data Scientist":
                Salaries_DS_2021.append(float(row[7])) 
              elif row[4]=="Data Science Manager":
                Salaries_DSM_2021.append(float(row[7])) 
              elif row[4]=="Data Science Engineer":
                Salaries_DSE_2021.append(float(row[7]))
              elif row[4]=="Data Science Consultant":
                Salaries_DSC_2021.append(float(row[7])) 
              elif row[4]=="Data Engineering Manager":
                Salaries_DEM_2021.append(float(row[7])) 
              elif row[4]=="Data Engineer":
                Salaries_DE_2021.append(float(row[7]))
              elif row[4]=="Data Architect":
                Salaries_DAr_2021.append(float(row[7]))
              elif row[4]=="Data Analytics Manager":
                Salaries_DAM_2021.append(float(row[7]))
              elif row[4]=="Data Analyst":
                Salaries_DA_2021.append(float(row[7]))
              elif row[4]=="Computer Vision Software Engineer":
                Salaries_CVSE_2021.append(float(row[7]))
              elif row[4]=="Computer Vision Engineer":
                Salaries_CVE_2021.append(float(row[7]))
              elif row[4]=="Cloud Data Engineer":
                Salaries_CDE_2021.append(float(row[7]))
              elif row[4]=="Business Data Analyst":
                Salaries_BDA_2021.append(float(row[7]))
              elif row[4]=="Big Data Engineer":
                Salaries_BDE_2021.append(float(row[7]))
              elif row[4]=="Big Data Architect":
                Salaries_BDAr_2021.append(float(row[7]))
              elif row[4]=="BI Data Analyst":
                Salaries_BIDA_2021.append(float(row[7]))
              elif row[4]=="Applied Machine Learning Scientist":
                Salaries_AMLS_2021.append(float(row[7]))
              elif row[4]=="Applied Data Scientist":
                Salaries_ADS_2021.append(float(row[7]))
              elif row[4]=="AI Scientist":
                Salaries_AIS_2021.append(float(row[7]))
              elif row[4]=="3D Computer Vision Researcher":
                Salaries_3DCVR_2021.append(float(row[7]))
              elif row[4]=="Data Analytics Engineer":
                Salaries_DAE_2021.append(float(row[7]))     
           elif row[1]=="2022":
               if row[4]=="Research Scientist":
                Salaries_RS_2022.append(float(row[7]))
               elif row[4]=="Principal Data Scientist":
                Salaries_PDS_2022.append(float(row[7])) 
               elif row[4]=="Principal Data Analyst":
                Salaries_PDA_2022.append(float(row[7]))
               elif row[4]=="NLP Engineer":
                Salaries_NLPE_2022.append(float(row[7]))
               elif row[4]=="ML Engineer":
                Salaries_MLE_2022.append(float(row[7]))
               elif row[4]=="Machine Learning Scientist":
                Salaries_MLS_2022.append(float(row[7]))
               elif row[4]=="Machine Learning Infrastructure Engineer":
                Salaries_MLIE_2022.append(float(row[7]))
               elif row[4]=="Machine Learning Engineer":
                Salaries_ML_E_2022.append(float(row[7]))
               elif row[4]=="Lead Machine Learning Engineer":
                Salaries_LMLE_2022.append(float(row[7]))
               elif row[4]=="Lead Data Engineer":                  
                Salaries_LDE_2022.append(float(row[7])) 
               elif row[4]=="Head of Machine Learning":                  
                Salaries_HoML_2022.append(float(row[7]))
               elif row[4]=="Head of Data Science":
                Salaries_HoDS_2022.append(float(row[7]))
               elif row[4]=="Financial Data Analyst":
                Salaries_FLDA_2022.append(float(row[7]))
               elif row[4]=="ETL Developer":
                Salaries_ETLD_2022.append(float(row[7]))
               elif row[4]=="Director of Data Science":
                Salaries_DoDS_2022.append(float(row[7]))
               elif row[4]=="Data Scientist":
                Salaries_DS_2022.append(float(row[7]))
               elif row[4]=="Data Science Manager":
                Salaries_DSM_2022.append(float(row[7]))
               elif row[4]=="Data Science Engineer":
                Salaries_DSE_2022.append(float(row[7]))
               elif row[4]=="Data Engineer":
                Salaries_DE_2022.append(float(row[7]))
               elif row[4]=="Data Architect":
                Salaries_DAr_2022.append(float(row[7]))
               elif row[4]=="Data Analytics Manager":
                Salaries_DAM_2022.append(float(row[7]))
               elif row[4]=="Data Analytics Lead":
                Salaries_DAL_2022.append(float(row[7]))
               elif row[4]=="Data Analytics Engineer":
                Salaries_DAE_2022.append(float(row[7]))
               elif row[4]=="Data Analyst":
                Salaries_DA_2022.append(float(row[7]))
               elif row[4]=="Computer Vision Software Engineer":
                Salaries_CVSE_2022.append(float(row[7]))
               elif row[4]=="Computer Vision Engineer":
                Salaries_CVE_2022.append(float(row[7]))
               elif row[4]=="Business Data Analyst":
                Salaries_BDA_2022.append(float(row[7]))
               elif row[4]=="Applied Machine Learning Scientist":
                Salaries_AMLS_2022.append(float(row[7]))
               elif row[4]=="Analytics Engineer":
                Salaries_AE_2022.append(float(row[7]))
               elif row[4]=="AI Scientist":
                Salaries_AIS_2022.append(float(row[7]))
               
      AvgRS_2020 = sum(Salaries_RS_2020)/len(Salaries_RS_2020)
      AvgRS_2021 = sum(Salaries_RS_2021)/len(Salaries_RS_2021)
      AvgRS_2022 = sum(Salaries_RS_2022)/len(Salaries_RS_2022)
      Change_RS = abs(AvgRS_2022 - AvgRS_2020)
       
      AvgPDA_2021 = sum(Salaries_PDA_2021)/len(Salaries_PDA_2021)
      AvgPDA_2022 = sum(Salaries_PDA_2022)/len(Salaries_PDA_2022)
      Change_PDA = abs(AvgPDA_2021-AvgPDA_2022)
      
      AvgPDS_2020 = sum(Salaries_PDS_2020)/len(Salaries_PDS_2020)
      AvgPDS_2021 = sum(Salaries_PDS_2021)/len(Salaries_PDS_2021)
      AvgPDS_2022 = sum(Salaries_PDS_2022)/len(Salaries_PDS_2022)
      Change_PDS = abs(AvgPDS_2020-AvgPDS_2021)
      
      AvgMLE_2020 = sum(Salaries_MLE_2020)/len(Salaries_MLE_2020)
      AvgMLE_2021 = sum(Salaries_MLE_2021)/len(Salaries_MLE_2021)
      AvgMLE_2022 = sum(Salaries_MLE_2022)/len(Salaries_MLE_2022)
      Change_MLE = abs(AvgMLE_2022-AvgMLE_2020)
        
      AvgMLS_2020 = sum(Salaries_MLS_2020)/len(Salaries_MLS_2020)
      AvgMLS_2021 = sum(Salaries_MLS_2021)/len(Salaries_MLS_2021)
      AvgMLS_2022 = sum(Salaries_MLS_2022)/len(Salaries_MLS_2022)
      Change_MLS = abs(AvgMLS_2022-AvgMLS_2020)
      
      AvgMLM_2020 = sum(Salaries_MLM_2020 )/len(Salaries_MLM_2020)
      
      AvgML_E_2020 = sum(Salaries_ML_E_2020)/len(Salaries_ML_E_2020)
      AvgML_E_2021 = sum(Salaries_ML_E_2021)/len(Salaries_ML_E_2021)
      AvgML_E_2022 = sum(Salaries_ML_E_2022)/len(Salaries_ML_E_2022)
      Change_ML_E = abs(AvgML_E_2022-AvgML_E_2021)
      
      AvgMLIE_2020 = sum(Salaries_MLIE_2020)/len(Salaries_MLIE_2020)
      AvgMLIE_2021 = sum(Salaries_MLIE_2021)/len(Salaries_MLIE_2021)
      AvgMLIE_2022 = sum(Salaries_MLIE_2022)/len(Salaries_MLIE_2022)
      Change_MLIE = abs(AvgMLIE_2021-AvgMLIE_2020)

      AvgLDE_2020 = sum(Salaries_LDE_2020)/len(Salaries_LDE_2020)
      AvgLDE_2021 = sum(Salaries_LDE_2021)/len(Salaries_LDE_2021)
      AvgLDE_2022 = sum(Salaries_LDE_2022)/len(Salaries_LDE_2022)
      Change_LDE = abs(AvgLDE_2021-AvgLDE_2020)
      
      AvgLDS_2020 = sum(Salaries_LDS_2020)/len(Salaries_LDS_2020)
      AvgLDS_2021 = sum(Salaries_LDS_2021)/len(Salaries_LDS_2021)
      Change_LDS = abs(AvgLDS_2021-AvgLDS_2020)

      
      AvgLDA_2020 = sum(Salaries_LDA_2020)/len(Salaries_LDA_2020)
      AvgLDA_2021 = sum(Salaries_LDA_2021)/len(Salaries_LDA_2021)
      Change_LDA = abs(AvgLDA_2021-AvgLDA_2020)
      
      
      AvgDoDS_2020 = sum(Salaries_DoDS_2020)/len(Salaries_DoDS_2020)
      AvgDoDS_2021 = sum(Salaries_DoDS_2021)/len(Salaries_DoDS_2021)
      AvgDoDS_2022 = sum(Salaries_DoDS_2022)/len(Salaries_DoDS_2022)
      Change_DoDS = abs(AvgDoDS_2021-AvgDoDS_2020)

      
      AvgDS_2020 = sum(Salaries_DS_2020)/len(Salaries_DS_2020)
      AvgDS_2021 = sum(Salaries_DS_2021)/len(Salaries_DS_2021)
      AvgDS_2022 = sum(Salaries_DS_2022)/len(Salaries_DS_2022)
      Change_DS = abs(AvgDS_2022-AvgDS_2021)

      
      AvgDSM_2020 = sum(Salaries_DSM_2020)/len(Salaries_DSM_2020)
      AvgDSM_2021 = sum(Salaries_DSM_2021)/len(Salaries_DSM_2021)
      AvgDSM_2022 = sum(Salaries_DSM_2022)/len(Salaries_DSM_2022)
      Change_DSM = abs(AvgDSM_2021-AvgDSM_2020)

      AvgDSC_2020 = sum(Salaries_DSC_2020)/len(Salaries_DSC_2020)
      AvgDSC_2021 = sum(Salaries_DSC_2021)/len(Salaries_DSC_2021)
      Change_DSC = abs(AvgDSC_2021-AvgDSC_2020)
      
      AvgDEM_2020 = sum(Salaries_DEM_2020 )/len(Salaries_DEM_2020)
      AvgDEM_2021 = sum(Salaries_DEM_2021 )/len(Salaries_DEM_2021)
      Change_DEM = abs(AvgDEM_2021-AvgDEM_2020)
      
      AvgDE_2020 = sum(Salaries_DE_2020)/len(Salaries_DE_2020)
      AvgDE_2021 = sum(Salaries_DE_2021)/len(Salaries_DE_2021)
      AvgDE_2022 = sum(Salaries_DE_2022)/len(Salaries_DE_2022)
      Change_DE = abs(AvgDE_2021-AvgDE_2022)
      
      AvgDA_2020 = sum(Salaries_DA_2020)/len(Salaries_DA_2020)
      AvgDA_2021 = sum(Salaries_DA_2021)/len(Salaries_DA_2021)
      AvgDA_2022 = sum(Salaries_DA_2022)/len(Salaries_DA_2022)
      Change_DA = abs(AvgDA_2020-AvgDA_2022)

      
      AvgCVE_2020 = sum(Salaries_CVE_2020)/len(Salaries_CVE_2020)
      AvgCVE_2021= sum(Salaries_CVE_2021)/len(Salaries_CVE_2021)
      AvgCVE_2022= sum(Salaries_CVE_2022)/len(Salaries_CVE_2022)
      Change_CVE = abs(AvgCVE_2021-AvgCVE_2022)
      
      AvgBDA_2020 = sum(Salaries_BDA_2020)/len(Salaries_BDA_2020)
      AvgBDA_2021 = sum(Salaries_BDA_2021)/len(Salaries_BDA_2021)
      AvgBDA_2022 = sum(Salaries_BDA_2022)/len(Salaries_BDA_2022)
      Change_BDA = abs(AvgBDA_2022-AvgBDA_2020)
      
      AvgBIDA_2020 = sum(Salaries_BIDA_2020)/len(Salaries_BIDA_2020)
      AvgBIDA_2021 = sum(Salaries_BIDA_2021)/len(Salaries_BIDA_2021)
      Change_BIDA = abs(AvgBIDA_2021-AvgBIDA_2020)
      
      AvgBDE_2020 = sum(Salaries_BDE_2020)/len(Salaries_BDE_2020)
      AvgBDE_2021 = sum(Salaries_BDE_2021)/len(Salaries_BDE_2021)
      Change_BDE = abs(AvgBDE_2021-AvgBDE_2020)
      
      AvgAIS_2020 = sum(Salaries_AIS_2020 )/len(Salaries_AIS_2020 )
      AvgAIS_2021 = sum(Salaries_AIS_2021 )/len(Salaries_AIS_2021)
      AvgAIS_2022 = sum(Salaries_AIS_2022 )/len(Salaries_AIS_2022)
      Change_AIS = abs(AvgAIS_2021-AvgAIS_2020)
      
      AvgHoDS_2021 = sum(Salaries_HoDS_2021)/len(Salaries_HoDS_2021)
      AvgHoDS_2022 = sum(Salaries_HoDS_2022)/len(Salaries_HoDS_2022)
      Change_HoDS = abs(AvgHoDS_2021-AvgHoDS_2022)

      AvgFLDA_2021 = sum(Salaries_FLDA_2021)/len(Salaries_FLDA_2021)
      AvgFLDA_2022 = sum(Salaries_FLDA_2022)/len(Salaries_FLDA_2022)
      Change_FLDA = abs(AvgFLDA_2021-AvgFLDA_2022)

      AvgDSE_2021 = sum(Salaries_DSE_2021)/len(Salaries_DSE_2021)
      AvgDSE_2022 = sum(Salaries_DSE_2022)/len(Salaries_DSE_2022)
      Change_DSE = abs(AvgDSE_2021-AvgDSE_2022)

      AvgDAr_2021 = sum(Salaries_DAr_2021)/len(Salaries_DAr_2021)
      AvgDAr_2022 = sum(Salaries_DAr_2022)/len(Salaries_DAr_2022)
      Change_DAr = abs(AvgDAr_2021-AvgDAr_2022)

      AvgDAM_2021 = sum(Salaries_DAM_2021)/len(Salaries_DAM_2021)
      AvgDAM_2022 = sum(Salaries_DAM_2022)/len(Salaries_DAM_2022)
      Change_DAM = abs(AvgDAM_2021-AvgDAM_2022)
      
      AvgDAE_2021 = sum(Salaries_DAE_2021)/len(Salaries_DAE_2021)
      AvgDAE_2022 = sum(Salaries_DAE_2022)/len(Salaries_DAE_2022)
      Change_DAE = abs(AvgDAE_2021-AvgDAE_2022)

      AvgCVSE_2021 = sum(Salaries_CVSE_2021)/len(Salaries_CVSE_2021)
      AvgCVSE_2022 = sum(Salaries_CVSE_2022)/len(Salaries_CVSE_2022)
      Change_CVSE = abs(AvgCVSE_2021-AvgCVSE_2022)      

      AvgAMLS_2021 = sum(Salaries_AMLS_2021)/len(Salaries_AMLS_2021)
      AvgAMLS_2022 = sum(Salaries_AMLS_2022)/len(Salaries_AMLS_2022)
      Change_AMLS = abs(AvgAMLS_2021-AvgAMLS_2022)
      
      AvgDAL_2022 = sum(Salaries_DAL_2022)/len(Salaries_DAL_2022)
      AvgPDDA_2020 = sum(Salaries_PDDA_2020)/len(Salaries_PDDA_2020)
      AvgMDA_2021 = sum(Salaries_MLE_2021)/len(Salaries_MDA_2021)
      AvgMLD_2021 = sum(Salaries_MLD_2021)/len(Salaries_MLD_2021)
      AvgHOD_2021 = sum(Salaries_HOD_2021)/len(Salaries_HOD_2021)
      AvgFDA_2021 = sum(Salaries_FDA_2021)/len(Salaries_FDA_2021)
      AvgDoDE_2021 = sum(Salaries_DoDE_2021)/len(Salaries_DoDE_2021)
      AvgDSL_2021 = sum(Salaries_DSL_2021)/len(Salaries_DSL_2021)
      AvgDAM_2021 = sum(Salaries_DAM_2021)/len(Salaries_DAM_2021)
      AvgCDE_2021 = sum(Salaries_CDE_2021)/len(Salaries_CDE_2021)
      AvgBDAr_2021 = sum(Salaries_BDAr_2021)/len(Salaries_BDAr_2021)
      AvgADS_2021 = sum(Salaries_ADS_2021)/len(Salaries_ADS_2021)
      Avg3DCVR_2021 = sum(Salaries_3DCVR_2021)/len(Salaries_3DCVR_2021)
      AvgNLPE_2022 = sum(Salaries_NLPE_2022)/len(Salaries_NLPE_2022)
      AvgLMLE_2022 = sum(Salaries_LMLE_2022)/len(Salaries_LMLE_2022)
      AvgHoML_2022 = sum(Salaries_HoML_2022)/len(Salaries_HoML_2022)
      AvgETLD_2022 = sum(Salaries_ETLD_2022)/len(Salaries_ETLD_2022)
      AvgAE_2022 = sum(Salaries_AE_2022)/len(Salaries_AE_2022)

      print("2020Average Salary  of Research Scientist is :",AvgRS_2020)
      print("2021Average Salary  of Research Scientist is :",AvgRS_2021)
      print("2022Average Salary  of Research Scientist is :",AvgRS_2022)
      print("The biggest change of Research Scientist is",Change_RS)
      print("")
      print("2020Average Salary  of Principal Data Scientist is :",AvgPDS_2020)
      print("2021Average Salary  of Principal Data Scientist is :",AvgPDS_2021)
      print("2022Average Salary  of Principal Data Scientist is :",AvgPDS_2022)
      print("The change of biggest of Principal Data Scientist is",Change_PDA)
      print("")
      print("2020Average Salary  of ML Engineer is :",AvgMLE_2020)
      print("2021Average Salary  of ML Engineer is :",AvgMLE_2021)
      print("2022Average Salary  of ML Engineer is :",AvgMLE_2022)
      print("The biggest change of ML Engineer is",Change_MLE)
      print("")
      print("2020Average Salary  of Machine Learning Scientist is :",AvgMLS_2020 )
      print("2021Average Salary  of Machine Learning Scientist is :",AvgMLS_2021 )
      print("2022Average Salary  of Machine Learning Scientist is :",AvgMLS_2022 )
      print("The biggest change of Machine Learning Scientist is",Change_MLS)
      print('')
      print("2020Average Salary  of Machine Learning Manager is :",AvgMLM_2020)
      print("")
      print("2020Average Salary  of Machine Learning Engineer is :",AvgML_E_2020)
      print("2021Average Salary  of Machine Learning Engineer is :",AvgML_E_2021)
      print("2022Average Salary  of Machine Learning Engineer is :",AvgML_E_2022)
      print("The biggest change of Machine Learning Engineer is",Change_ML_E)
      print("")
      print("2020Average Salary  of Machine Learning Infrastructure Engineer is :",AvgMLIE_2020)
      print("2020Average Salary  of Machine Learning Infrastructure Engineer is :",AvgMLIE_2021)
      print("2020Average Salary  of Machine Learning Infrastructure Engineer is :",AvgMLIE_2022)
      print("The biggest change of Machine Learning Infrastructure Engineer is",Change_MLIE)
      print("")
      print("2020Average Salary  of Lead Data Scientist is :",AvgLDS_2020)
      print("2020Average Salary  of Lead Data Scientist is :",AvgLDS_2021)
      print("The biggest change of Lead Data Scientist is",Change_LDS)
      print("")
      print("2020Average Salary  of Lead Data Engineer is :",AvgLDE_2020)
      print("2021Average Salary  of Lead Data Engineer is :",AvgLDE_2021)
      print("2022Average Salary  of Lead Data Engineer is :",AvgLDE_2022)
      print("The biggest change of Research Scientist is",Change_LDE)
      print("")
      print("2020Average Salary  of Research Scientist is :",AvgRS_2020)
      print("2021Average Salary  of Research Scientist is :",AvgRS_2021)
      print("2022Average Salary  of Research Scientist is :",AvgRS_2022)
      print("The biggest change of Research Scientist is",Change_RS)
      print("")
      print("2020Average Salary  of Principal Data Scientist is :",AvgPDS_2020)
      print("2021Average Salary  of Principal Data Scientist is :",AvgPDS_2021)
      print("2022Average Salary  of Principal Data Scientist is :",AvgPDS_2022)
      print("The change of biggest of Principal Data Scientist is",Change_PDA)
      print("")
      print("2020Average Salary  of ML Engineer is :",AvgMLE_2020)
      print("2021Average Salary  of ML Engineer is :",AvgMLE_2021)
      print("2022Average Salary  of ML Engineer is :",AvgMLE_2022)
      print("The biggest change of ML Engineer is",Change_MLE)
      print("")
      print("2020Average Salary  of Machine Learning Scientist is :",AvgMLS_2020 )
      print("2021Average Salary  of Machine Learning Scientist is :",AvgMLS_2021 )
      print("2022Average Salary  of Machine Learning Scientist is :",AvgMLS_2022 )
      print("The biggest change of Machine Learning Scientist is",Change_MLS)
      print('')
      print("2020Average Salary  of Machine Learning Manager is :",AvgMLM_2020)
      print("")
      print("2020Average Salary  of Machine Learning Engineer is :",AvgML_E_2020)
      print("2021Average Salary  of Machine Learning Engineer is :",AvgML_E_2021)
      print("2022Average Salary  of Machine Learning Engineer is :",AvgML_E_2022)
      print("The biggest change of Machine Learning Engineer is",Change_ML_E)
      print("")
      print("2020Average Salary  of Machine Learning Infrastructure Engineer is :",AvgMLIE_2020)
      print("2020Average Salary  of Machine Learning Infrastructure Engineer is :",AvgMLIE_2021)
      print("2020Average Salary  of Machine Learning Infrastructure Engineer is :",AvgMLIE_2022)
      print("The biggest change of Machine Learning Infrastructure Engineer is",Change_MLIE)
      print("")
      print("2020Average Salary  of Lead Data Scientist is :",AvgLDS_2020)
      print("2020Average Salary  of Lead Data Scientist is :",AvgLDS_2021)
      print("The biggest change of Lead Data Scientist is",Change_LDS)
      print("")
      print("2020Average Salary  of Lead Data Engineer is :",AvgLDE_2020)
      print("2021Average Salary  of Lead Data Engineer is :",AvgLDE_2021)
      print("2022Average Salary  of Lead Data Engineer is :",AvgLDE_2022)
      print("The biggest change of Research Scientist is",Change_LDE)
      print('')
      print("2020Average Salary  of Lead Data Analyst is :",AvgLDA_2020)
      print("2020Average Salary  of Lead Data Analyst is :",AvgLDA_2021)
      print("The biggest change of Lead Data Analyst is",Change_LDA)
      print('')
      print("2020Average Salary  of Director of Data Science is :",AvgDoDS_2020)
      print("2021Average Salary  of Director of Data Science is :",AvgDoDS_2021)
      print("2022Average Salary  of Director of Data Science is :",AvgDoDS_2022)
      print("The biggest change of Director of Data Science is",Change_DoDS)
      print("")
      print("2020Average Salary  of Data Scientist is :",AvgDS_2020)
      print("2021Average Salary  of Data Scientist is :",AvgDS_2021)
      print("2022Average Salary  of Data Scientist is :",AvgDS_2022)
      print("The biggest change of Data Scientist is",Change_DS)
      print("")
      print("2020Average Salary  of Data Science Manager is :",AvgDSM_2020)
      print("2021Average Salary  of Data Science Manager is :",AvgDSM_2021)
      print("2022Average Salary  of Data Science Manager is :",AvgDSM_2022)
      print("The biggest change of Data Science Manager is",Change_DSM)
      print("")
      print("2020Average Salary  of Data Science Consultant is :",AvgDSC_2020)
      print("2021Average Salary  of Data Science Consultant is :",AvgDSC_2021)
      print("The biggest change of Data Science Consultant is",Change_DSC)
      print("")
      print("2020Average Salary  of Data Engineering Manager is :",AvgDEM_2020)
      print("2021Average Salary  of Data Engineering Manager is :",AvgDEM_2021)
      print("The biggest change of Data Engineering Manager is",Change_DEM)
      print("")
      print("2020Average Salary  of Data Engineer is :",AvgDE_2020)
      print("2021Average Salary  of Data Engineer is :",AvgDE_2021)
      print("2022Average Salary  of Data Engineer is :",AvgDE_2022)
      print("The biggest change of Data Engineer is",Change_DE)
      print("")
      print("2020Average Salary  of Data Analyst is :",AvgDA_2020)
      print("2021Average Salary  of Data Analyst is :",AvgDA_2021)
      print("2022Average Salary  of Data Analyst is :",AvgDA_2022)
      print("The biggest change of Data Analyst is",Change_DA)
      print("")
      print("2020Average Salary  of Computer Vision Engineer is :",AvgCVE_2020)
      print("2021Average Salary  of Computer Vision Engineer is :",AvgCVE_2021)
      print("2022Average Salary  of Computer Vision Engineer is :",AvgCVE_2022)
      print("The biggest change of Computer Vision Engineer is",Change_CVE)
      print("")
      print("2020Average Salary  of Business Data Analyst is :",AvgBDA_2020)
      print("2021Average Salary  of Business Data Analyst is :",AvgBDA_2021)
      print("2022Average Salary  of Business Data Analyst is :",AvgBDA_2022)
      print("The biggest change of Business Data Analyst is",Change_BDA)
      print("")
      print("2020Average Salary  of BI Data Analyst is :",AvgBIDA_2020)
      print("2021Average Salary  of BI Data Analyst is :",AvgBIDA_2021)
      print("The biggest change of BI Data Analyst is",Change_BIDA)
      print("")
      print("2020Average Salary  of Big Data Engineer is :",AvgBDE_2020)
      print("2021Average Salary  of Big Data Engineer is :",AvgBDE_2021)
      print("The biggest change of Big Data Engineer is",Change_BDE)
      print("")
      print("2020Average Salary  of AI Scientist is :",AvgAIS_2020)
      print("2021Average Salary  of AI Scientist is :",AvgAIS_2021)
      print("2021Average Salary  of AI Scientist is :",AvgAIS_2022)
      print("The biggest change of AI Scientist is",Change_AIS)
      print("")
      print("2021Average Salary  of Principal Data Analyst is :",AvgPDA_2021)
      print("2022Average Salary  of Principal Data Analyst is :",AvgPDA_2022)
      print("The biggest change of Principal Data Analyst is",Change_PDA)
      print("")
      print("2021Average Salary  of Head of Data Science is :",AvgHoDS_2021)
      print("2022Average Salary  of Head of Data Science is :",AvgHoDS_2022)
      print("The biggest change of Head of Data Science is",Change_HoDS)
      print("")
      print("2021Average Salary  of Financial Data Analyst is :",AvgFLDA_2021)
      print("2022Average Salary  of Financial Data Analyst is :",AvgFLDA_2022)
      print("The biggest change of Financial Data Analyst is",Change_FLDA)
      print("")
      print("2021Average Salary  of Data Science Engineer is :",AvgDSE_2021)
      print("2022Average Salary  of Data Science Engineer is :",AvgDSE_2022)
      print("The biggest change of Data Science Engineer is",Change_DSE)
      print("")
      print("2021Average Salary  of Data Architect is :",AvgDAr_2021)
      print("2022Average Salary  of Data Architect is :",AvgDAr_2022)
      print("The biggest change of Data Architect is",Change_DAr)
      print("")
      print("2021Average Salary  of Data Analytics Manager is :",AvgDAM_2021)
      print("2022Average Salary  of Data Analytics Manager is :",AvgDAM_2022)
      print("The biggest change of Data Analytics Manager is",Change_DAM)
      print("")
      print("2021Average Salary  of Computer Vision Software Engineer is :",AvgCVSE_2021)
      print("2022Average Salary  of Computer Vision Software Engineer is :",AvgCVSE_2022)
      print("The biggest change of Computer Vision Software Engineer is",Change_CVSE)
      print("")
      print("2021Average Salary  of Applied Machine Learning Scientist is :",AvgAMLS_2021)
      print("2022Average Salary  of Applied Machine Learning Scientist is :",AvgAMLS_2022)
      print("The biggest change of Applied Machine Learning Scientist is",Change_AMLS)
      print("")
      print("2021Average Salary  of Data Analytics Engineer is :",AvgDAE_2021)
      print("2022Average Salary  of Data Analytics Engineer is :",AvgDAE_2022)
      print("The biggest change of Data Analytics Engineer is",Change_DAE)
      
      print("")      
      print("2022Average Salary  of Data Analytics Lead is :",AvgDAL_2022)
      print("2020Average Salary  of Product Data Analyst is :",AvgPDDA_2020)     
      print("2021Average Salary  of Marketing Data Analyst is :",AvgMDA_2021)
      print("2021Average Salary  of Machine Learning Developer is :",AvgMLD_2021)
      print("2021Average Salary  of Head of Data is :",AvgHOD_2021)
      print("2021Average Salary  of Finance Data Analyst is :",AvgFDA_2021)
      print("2021Average Salary  of Director of Data Engineering is :",AvgDoDS_2021)
      print("2021Average Salary  of Data Specialist is :",AvgDSL_2021)
      print("2021Average Salary  of Computer Cloud Data Engineer Engineer is :",AvgCDE_2021)
      print("2021Average Salary  of Big Data Architect is :",AvgBDAr_2021)
      print("2021Average Salary  of Applied Data Scientist is :",AvgADS_2021)
      print("2021Average Salary  of 3D Computer Vision Researcher is :",Avg3DCVR_2021)
      print("2021Average Salary  of NLP Engineer is :",AvgNLPE_2022)
      print("2021Average Salary  of Lead Machine Learning Engineer is :",AvgLMLE_2022)
      print("2021Average Salary  of Head of Machine Learning is :",AvgHoML_2022)
      print("2021Average Salary  of ETL Developer is :",AvgETLD_2022)
      print("2021Average Salary  of Analytics Engineer is :",AvgAE_2022)

      print("To getthe biggest change and samllest change,I first exclude the titles thatappear only once, and then subtract the highest and lowest wages in the title to get the wage difference. The biggest change is:Financial Data Analyst,$350000,smallest change is: Data Analytics Manager:$818 ")






      



