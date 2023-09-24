import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd

url = "https://www.naver.com"

request = requests.get(urlsss)
print("hello world")
soup = BeautifulSoup(request.text, "html.parser")
print(request.text)
data = soup.find("table",{"class":"table"})
table = parser_functions.make2d(data)

df = pd.DataFrame(data=table[1:], columns=table[0])
df