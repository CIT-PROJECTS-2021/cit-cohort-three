1. Scrape CBS news https://www.cbsnews.com/latest/rss/main and get the following data
    - Title
    - Link
    - Image
    - description


    Using SqlAlchemy create a table called `cbs_news` and insert the data into the table.

    Implement one route called `/cbs_news` that returns the data in json format.
    
    
    
    from bs4 import BeautifulSoup

page = requests.get("[https://www.cbsnews.com/latest/rss/main]")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text
# Extract title of page
page_title = soup.title.text
# print the result
print(page_title)

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_body, page_head)

# Extract and store in top_items according to instructions on the left
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({"src": src, "alt": alt})

print(image_data)

info = {
   "href": "<https://www.cbsnews.com/latest/rss/main>",
   "text": "<https://www.cbsnews.com/latest/rss/main>"


**NOTE**: Use lxml to parse the xml data.


import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://www.cbsnews.com/latest/rss/main)/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
all_products = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)
