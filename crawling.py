import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd

url = "https://www.kangwon.ac.kr/www/selecttnCafMenuListWU.do?key=1077&sc1=CC10&sc2=CC"

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
print(request.text)
data = soup.find("table",{"class":"table"})
table = parser_functions.make2d(data)

df = pd.DataFrame(data=table[1:], columns=table[0])
df