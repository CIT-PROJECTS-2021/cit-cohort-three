"""1. Find top movies on IMDB since 1980 using web scraping
and save the result in a csv file. The csv file should have
the following columns: title, year, rating, metascore, votes,
gross, director, actors, runtime, genre, description.
The csv file should be sorted by rating in descending order.
The csv file should have the following columns: title, year, rating,
metascore, votes, gross, director, actors, runtime, genre, description.
The csv file should be sorted by rating in descending order.

2. Scrap Hacker News project and save the result in a csv file.
The csv file should have the following columns: title, link, points,
comments, author, rank. The csv file should be sorted by rank in
ascending order.
"""
# URL, how save dict into a csv

import requests
import csv
from bs4 import BeautifulSoup


def get_hacker_news():
    url = "https://news.ycombinator.com/news"
    response = requests.get(url)

    data = []

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('tr', class_ = 'athing')

    for row in rows:
            # extract title
        title = row.find('span', class_ = 'titleline').find('a').text
        link = row.find('span', class_ = 'titleline').find('a')['href']
        score = row.find_next_sibling('tr').find('span', class_ = 'score')

        if score:
            score = score.text
        else:
            score = "0 points"

        comments = row.find_next_sibling('tr').find_all('a')[-1].text

        author = row.find_next_sibling('tr').find('a', class_ = 'hnuser')

        if author:
            author = author.text
        else:
            author = "Unknown"

        rank = int(row.find('span', class_ = 'rank').text.split('.')[0])

        data.append({
            'title': title,
            'link': link,
            'score': score,
            'comments': "{} comments".format(comments.split('\xa0')[0]),
            'author': author,
            'rank': rank
        })

    return data

# sorted(data, key = lambda x : x[0]['rank'], reversed = True)


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

def main():
    hacker_news = get_hacker_news()
    save_to_csv(hacker_news, "hacker_news.csv")
    print("Done")


if __name__ == '__main__':
    main()