"""
Script for playing arround with datasets (please don't delete, write from the last line)
"""
import pandas as pd
import numpy as np

data1 = pd.read_csv("Cleaned_Vacc_data_mod_1.csv")
data2 = pd.read_excel("File1.xlsx", "Sheet2")
data2.head()

data1.head()
linePlt = {'LinePlot':[]}
#'LinePlot'='Date','ZA-GT TotalVaccinations' ,'ZA-FS TotalVaccinations','ZA-EC TotalVaccinations','ZA-NL TotalVaccinations','ZA-LP TotalVaccinations','ZA-MP TotalVaccinations','ZA-NC TotalVaccinations','ZA-NW TotalVaccinations','ZA-WC TotalVaccinations'
provinces=[]
provinceData = {'ProvinceDate':[],'ProvinceName':[], 'ProvinceTotalVaccinations':[], 'ProvincePopulation':[]}

v = 0
for x in data1.index:
    
    #estern cape
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-EC')
    provinceData['ProvinceTotalVaccinations'].append(data1['EC'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][0])
    
    #Free State
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-FS')
    provinceData['ProvinceTotalVaccinations'].append(data1['FS'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][1])
    
    #Gauteng
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-GT')
    provinceData['ProvinceTotalVaccinations'].append(data1['GP'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][2])

    #Kwazulu-natal
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-NL')
    provinceData['ProvinceTotalVaccinations'].append(data1['KZN'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][3])
    
    #Limpopo
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-LP')
    provinceData['ProvinceTotalVaccinations'].append(data1['LP'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][4])
    
    #Mpumalanga
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-MP')
    provinceData['ProvinceTotalVaccinations'].append(data1['MP'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][5])
    
    #North West
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-NW')
    provinceData['ProvinceTotalVaccinations'].append(data1['NW'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][6])
    
    #Northern Cape
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-NC')
    provinceData['ProvinceTotalVaccinations'].append(data1['NC'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][7])
    
    #Western Cape
    provinceData['ProvinceDate'].append(data1['Date'][x])
    provinceData['ProvinceName'].append('ZA-WC')
    provinceData['ProvinceTotalVaccinations'].append(data1['WC'][x])
    provinceData['ProvincePopulation'].append(data2['Sum of 2020'][8])



provinceDataF = pd.DataFrame(provinceData)
provinceDataF.to_csv("Provincial_Data.csv")
#print(len(provinces))



