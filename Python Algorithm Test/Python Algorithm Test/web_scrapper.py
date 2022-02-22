from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/omega/Documents/Datathon-Dirisa/chromedriver_win32/chromedriver.exe')
driver.get('https://sacoronavirus.co.za/latest-vaccine-statistics/?gclid=CjwKCAjwuvmHBhAxEiwAWAYj-FwIAphr88eENf9dD1BLgmzj0FpZdQ0DwkdJ8yI9ZSbSk0bW7wdRXRoCIAAQAvD_BwE')
result = []
content = driver.page_source
soup = BeautifulSoup(content)
for element in soup.find_all(attrs='visualContainerHost'):
    print(element)
    

print(result)

