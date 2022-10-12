import requests
from bs4 import BeautifulSoup
import json
import re

search_term = input("What product do you want to search for?: ")

url = f"https://www.newegg.ca/p/pl?d={search_term.replace(' ', '+')}"

page = requests.get(url).text

# lxml
doc = BeautifulSoup(page, 'html.parser')


page_text = doc.find(class_ = 'list-tool-pagination-text').strong
page_text = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, page_text + 1):
    url = f"{url}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')

    products_div = doc.find('div', class_ = 'item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
    items = products_div.find_all(class_ = "item-cell")

    for index, item in enumerate(items):
       try:
           product_name = item.find("div", class_ = "item-info").find("a").text
           link = item.find("div", class_ = "item-info").find("a").href
           price = item.find(class_ = "price-current").strong.text
           image = item.find('img').src
       except:
        pass

        items_found[index+1] = {"product_name": product_name, "price": int(price.replace(",", '')), "image": image, "link": link}

print(items_found)