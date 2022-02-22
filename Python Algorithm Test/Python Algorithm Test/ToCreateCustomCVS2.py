import pandas as pd
"""
For the progress
"""

data1 = pd.read_csv("Cleaned_Vacc_data_mod_1.csv")
data2 = pd.read_excel("File1.xlsx", "Sheet2")

data2.head()

data1.head()

data1['EC'][90]

provinceData = {'CODE':[],'Vaccinations':[], 'Pop':[], 'Rate':[]}

provinces = ['EC', 'NW', 'GP', 'FS', 'KZN', 'LP','MP', 'NC', 'WC']
codes = ['ZA-EC','ZA-NW','ZA-GT', 'ZA-FS', 'ZA-NL', 'ZA-LP','ZA-MP', 'ZA-NC', 'ZA-WC']

for c in range(len(codes)):
    # calculate percentage
    Rate = (int(data1[provinces[c]][90])/int(data2['Sum of 2020'][c]))*100 #percentatage of rate per province
    provinceData['CODE'].append(codes[c])
    provinceData['Vaccinations'].append(data1[provinces[c]][90])
    provinceData['Pop'].append(data2['Sum of 2020'][c])
    provinceData['Rate'].append(Rate)

#not to forget national
Rate = (int(data1['total'][90])/int(data2['Sum of 2020'][9]))*100 #percentatage of national
provinceData['CODE'].append('NAT')
provinceData['Vaccinations'].append(data1['total'][90])
provinceData['Pop'].append(data2['Sum of 2020'][9])
provinceData['Rate'].append(Rate)


provinceDataF = pd.DataFrame(provinceData)
print(provinceDataF)
provinceDataF.to_csv("Progress_Data.csv")
print(len(provinces))
