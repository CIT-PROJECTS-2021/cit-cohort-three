import requests
from bs4 import BeautifulSoup

url = "https://kallyas.github.io/cakeshop/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
title = soup.title.text
# print(title)