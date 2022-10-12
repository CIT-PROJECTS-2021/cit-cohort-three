import requests
from bs4 import BeautifulSoup
import json

url = "https://cit-projects-2021.github.io/fake-jobs"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
heading = soup.h1.text.strip()
print(heading)
# print(title)

# using classes
# card = soup.find(class_ = "column is-half")
# print(card.prettify())
cards = soup.find_all(class_ = "column is-half")
# print(len(cards))

# job_title = card.find('h2', class_ = "title is-5").text
# print(job_title)
#
# company = card.find('h3', class_ = 'subtitle is-6 company').text
# print(company)
#
# location = card.find('p', class_ = 'location').text.strip()
# print(location)
#
# date = card.find('p', class_ = 'is-small has-text-grey').find('time').text
#
# print(date)

jobs = {}

for index, card in enumerate(cards):
    job_title = card.find('h2', class_ = "title is-5").text
    company = card.find('h3', class_ = 'subtitle is-6 company').text
    location = card.find('p', class_ = 'location').text.strip()
    date = card.find('p', class_ = 'is-small has-text-grey').find('time').text
    jobs[index+1] = {'job_title': job_title, 'company': company, 'location': location, 'date': date}


with open('jobs.json', 'w') as json_file:
    json.dump(jobs, json_file, indent=4)

