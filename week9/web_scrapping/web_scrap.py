"""
Web scraping with python
"""

from bs4 import BeautifulSoup

# 3 ways

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Web Scraping</h1>
    <title>Web Scraping</title>
    <p>Web scraping is a technique to automatically access and extract large amounts of information from a website, which can save a huge amount of time and effort.</p>
    <p>Web scraping can be done manually through a web browser. However, this process is both time-consuming and error-prone. Fortunately, there are several web scraping tools that can help you automate the process.</p>
    <p>Web scraping tools can be used to extract data from websites and save it to a local file or database in a structured format. This data can then be used for a variety of purposes, including data mining, data processing, data cleansing, and data analysis.</p>
    <p>Web scraping tools can be used to extract data from websites and save it to a local file or database in a structured format. This data can then be used for a variety of purposes, including data mining, data processing, data cleansing, and data analysis.</p>
    <h1>ANother Heading</h1>
</body>
</html>
"""

soup = BeautifulSoup(html_str, 'html.parser')
# print(soup.prettify())
# soup.find('h1')
title = soup.title.text
heading = soup.h1.text
print(f"The title is {title} and the heading is {heading}")
sentence = soup.p.string
print(sentence)

paragraphs = soup.find_all('p')
# for index, paragraph in enumerate(paragraphs):
#     print(f"Paragraph {index+1} is {paragraph.text}")


headings = soup.find_all("h1")
print(headings)
for index, heading in enumerate(headings):
    print(f"Heading {index+1} is {heading.text} \n")

