from bs4 import BeautifulSoup
import os


html_path = os.path.join(os.path.dirname(__file__), 'index.html')
# print(html_path)

with open(html_path, 'r') as html_file:
    doc = html_file.read()

soup = BeautifulSoup(doc, 'html.parser')
# print(soup.prettify())
title = soup.title.text
anchors = soup.find_all('a')
# print(anchors)
# italics = soup.find('i')
# _italics = soup.find_all('b')[-1].find('i').text.strip()
b_tags = soup.find_all('b')
last_item = b_tags[-1]
child_item = last_item.find('i')
child_text = child_item.text.strip()