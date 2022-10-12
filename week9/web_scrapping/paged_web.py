import threading
import requests
from bs4 import BeautifulSoup
import json
import time

search_term = input("What product do you want to search for?: ")

url = f"https://www.newegg.ca/p/pl?d={search_term.replace(' ', '+')}"

page = requests.get(url).text

# lxml
doc = BeautifulSoup(page, 'html.parser')


page_text = doc.find(class_ = 'list-tool-pagination-text').strong
page_text = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

def scrape_data(url):
    for page in range(1, page_text + 1):
        url = f"{url}&page={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, 'html.parser')

        products_div = doc.find('div', class_ = 'item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
        items = products_div.find_all(class_ = "item-cell")

        for index, item in enumerate(items):
            product_name = item.find("div", class_ = "item-info").find("a").text
            link = item.find("div", class_ = "item-info").find("a").get("href")
            price_elm = item.find(class_ = "price-current").find("strong")
        
            if price_elm:
                price = price_elm.text

            image = item.find('img').get('src')

            items_found[index+1] = {"product_name": product_name, "price": int(price.replace(",", '')), "image": image, "link": link}

            # time.sleep(5)


scrape_data(url)

items_found = sorted(items_found.items(), key = lambda x: x[1]["price"])
items_found = dict(items_found)

with open("items.json", "w") as file:
    json.dump(items_found, file, indent=4)

print("Done")