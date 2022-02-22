#web scrapping
import requests as rq
from bs4 import BeautifulSoup as bs

html_text = rq.get('https://tradingeconomics.com/south-africa/population').text



