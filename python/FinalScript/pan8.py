import pickle
from datetime import datetime
import warnings
import pandas as pd
import pan7 as helper_functions

class predictions:
    # Cleaned up script
    # Province names should be specified by Codes eg "Limpopo" -> "ZA-LP"
    # Date values follow format -> "YYYY-MM--DD" eg "2021-07-29"

    # Date of expected herd immunity
    def getExpectedHerdImmunity():
        return helper_functions.getDateOfExpectedHerdImmunity("ZA-FULLY")


    # Predictions of total vaccinations in province, at the specified date
    # Output Array of total vaccines up to date
    def getProvinceVaccinatedTotal_Array(prov, date):
        return helper_functions.predictTotalVaccinated_Array(prov, date)


    # Prediction of total vaccinations in province, at the specified date
    # Output total vaccines up to date
    def getProvinceVaccinatedTotal_Single(prov, date):
        return helper_functions.predictTotalVaccinated_Single(prov, date)
    print(getProvinceVaccinatedTotal_Array("ZA-LP", "2021-08-05"))
