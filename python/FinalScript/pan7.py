# This Script gets the predictated total vaccines
# The format of the output is an integer number X
# X can be retrievd as it is or Turned to a JSon objec

import pickle
from datetime import datetime, timedelta
import warnings
import pandas as pd

warnings.filterwarnings("ignore")

Herd_Immunity_percent = 67 / 100  # 67 % of the population must be vaccinated to achieve herd immunity
                                  # Source "https://www.gov.za/covid-19/vaccine/strategy"


my_dict = {"ZA-LP": "lP",
           "ZA-GT": "GP",
           "ZA-FS": "FS",
           "ZA-NW": "NW",
           "ZA-NL": "KZN",
           "ZA-EC": "EC",
           "ZA-NC": "NC",
           "ZA-WC": "WC",
           "ZA-MP": "MP",
           "ZA-FULLY": "people_fully_vaccinated"}


# Helper to retrive Start and End values
# Input the province code
# Returns a list of (startValue, endValue)
def getMLValues(province):
    name = "values_" + province + ".txt"
    vv = []
    with open(name, 'r') as f:
        vv = f.read().split()
        vv[0] = int(vv[0])
        vv[1] = int(vv[1])
    return vv


# Helper to Calculates time delta from 25 july to specified date
def getTimeDelta(date):
    date_format = "%Y-%m-%d"
    a = datetime.strptime('2021-07-25', date_format)
    b = datetime.strptime(date, date_format)
    delta = b - a
    return int(delta.days)


# Helper to Calculate predicted vaccination values
def calTVaccs(time_delta, startV, endV, prov_name):
    # load the model
    name = "model_" + prov_name
    with open(name, 'rb') as f:
        m2 = pickle.load(f)
    # Predict
    x = m2.predict(startV, endV + time_delta - 1, typ="levels")
    f.close()
    if prov_name == my_dict["ZA-FULLY"]:
        return x.loc[9:]
    else:
        return x.loc[91:]


# Province input, expected input format "Full province code"" e.g "ZA-GP"/ "ZA-GT"
# Date input, expected input format "YYYY-MM-DD" eg "2021-08-13"
# Both inputs are Strings!
# Output Array of predicted total vaccinations
def predictTotalVaccinated_Array(province_name, date):
    delta = getTimeDelta(date)
    prov = my_dict[province_name]
    startV, endV = getMLValues(prov)
    x = calTVaccs(delta, startV, endV, prov)
    return x.astype("int64")


# Predict total vaccines given a date
# Province input, expected input format "Full province code"" e.g "ZA-GP"/ "ZA-GT"
# Date input, expected input format "YYYY-MM-DD" eg "2021-08-13"
# Both inputs are Strings!
# Output is a single value, The predicted total vaccinations at the specified date
def predictTotalVaccinated_Single(province_name, date):
    delta = getTimeDelta(date)
    startV, endV = getMLValues(my_dict[province_name])
    return predictTotalVaccinated_Array(province_name, date)[endV + delta - 1]


# Helper to read population Data
# Input province code, format "Province code" eg "ZA-GT" for Gauteng
# Output population size
def getPopulationSize(province):
    a = province
    if province == "ZA-FULLY":
        a = "Total"

    df = pd.read_csv("./Cleaned_Province_Population.csv")
    result = int(df[df.Province == a].Population)
    return result


# Helper to find int delta between from 25-July to 5 years later
# To a number greater than provided num
def getIntDelta(num, prov):
    arr = predictTotalVaccinated_Array(prov, "2026-07-25")
    count = 0
    for x in arr:
        if x > num:
            break
        count += 1

    return count + 1  # Account for the next day


# Helper to find delta from 25 - july to delta
def getDateFromDelta(delta):
    date_format = "%Y-%m-%d"
    a = datetime.strptime('2021-07-25', date_format)
    date = a + timedelta(delta)
    return date.date()


# Get date of expected herd immunity from 25 July(baseline)
# Input province code, format "Province code" eg "ZA-GT" for Gauteng
# Output date String
def getDateOfExpectedHerdImmunity(province):
    pop_immune = getPopulationSize(province) * Herd_Immunity_percent
    d = getIntDelta(int(pop_immune), province)
    return getDateFromDelta(d)

