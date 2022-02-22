import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from pmdarima import auto_arima
from statsmodels.tsa.arima_model import ARIMA
from sklearn.model_selection import train_test_split
import pickle

#The dataset I used in the modelling
df=pd.read_csv("Cleaned_Vacc_data_mod_1.csv",parse_dates=True)

#Some stuff I saw off the internet, it just works!
#Im fitting to Limpopo, so only Limpopo based Predictions!
country = "LP"
s_fit=auto_arima(df[country],trace=True)
#IF you want to see the summary, it also shows ORDER
#s_fit.summary()

#This is where, you need to change values to fit the data, the smaller the number, the better the model,though it may
#Not converge playing around with the number -20 worked fine in testing
num_train = -18
x_train = df.iloc[:num_train]
x_test = df.iloc[num_train:]

#Creating a model here with ORDER(See line 17)
model = ARIMA(x_train[country], order=(5,2,2))
model=model.fit()

#Make predictions and testing here
start1 = len(x_train)
end1 = len(x_train)+len(x_test)+100 #Adds 101 more predictions(testing)
pred1 = model.predict(start1,end1,typ="levels") #Array of predictions

#Want to write a function that only takes a date and gives out
#predicated values, it will do a lot of the heavy lifting
#like call line 33, where only the end is calculated
#This works on a case by case basis, eg LP has different order to GP and it converges much later!
#Test for other countries was done separately 

