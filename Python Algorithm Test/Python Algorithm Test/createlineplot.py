import pandas as pd
import numpy as np

data1 = pd.read_csv("Progress_Data.csv")

data2 = pd.read_csv("Provincial_Data.csv")
'Date','ZA-GT TotalVaccinations' ,'ZA-FS TotalVaccinations','ZA-GT TotalVaccinations','ZA-NL TotalVaccinations','ZA-LP TotalVaccinations','ZA-MP TotalVaccinations','ZA-NC TotalVaccinations','ZA-NW TotalVaccinations','ZA-WC TotalVaccinations'



provinceData = {'Date':[],'ZA-EC TotalVaccinations':[], 'ZA-FS TotalVaccinations':[],
                 'ZA-GT TotalVaccinations':[], 'ZA-NL TotalVaccinations':[], 'ZA-LP TotalVaccinations':[],
                 'ZA-MP TotalVaccinations':[], 'ZA-NW TotalVaccinations':[], 'ZA-NC TotalVaccinations':[], 
                 'ZA-WC TotalVaccinations':[]}
nationalData = {'Date':[], 'National_Total':[]}

date = ''
for d2 in data2.index:
    if(data2['ProvinceDate'][d2] != date):
        date = data2['ProvinceDate'][d2]
        provinceData['Date'].append(date)
        nationalData['Date'].append(date)
        
        total =int(data2['ProvinceTotalVaccinations'][d2]) + int(data2['ProvinceTotalVaccinations'][d2+1])+int(data2['ProvinceTotalVaccinations'][d2+2])+int(data2['ProvinceTotalVaccinations'][d2+3])+int(data2['ProvinceTotalVaccinations'][d2+4])+int(data2['ProvinceTotalVaccinations'][d2+5])+int(data2['ProvinceTotalVaccinations'][d2+6])+int(data2['ProvinceTotalVaccinations'][d2+7])+int(data2['ProvinceTotalVaccinations'][d2+8])        
        nationalData['National_Total'].append(total)
        
        provinceData['ZA-EC TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2])
        provinceData['ZA-FS TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+1])
        provinceData['ZA-GT TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+2])
        provinceData['ZA-NL TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+3])
        provinceData['ZA-LP TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+4])
        provinceData['ZA-MP TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+5])
        provinceData['ZA-NW TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+6])
        provinceData['ZA-NC TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+7])
        provinceData['ZA-WC TotalVaccinations'].append(data2['ProvinceTotalVaccinations'][d2+8])
        
provinceDataF = pd.DataFrame(provinceData)
nationalDataF = pd.DataFrame(nationalData)
nationalDataF.to_csv("new_national_data.csv")
provinceDataF.to_csv("new_provincial_data.csv")
print(provinceDataF)