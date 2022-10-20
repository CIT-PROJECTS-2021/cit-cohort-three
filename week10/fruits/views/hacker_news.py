from flask import Blueprint, request, redirect, render_template
from bs4 import BeautifulSoup
import requests
from fruits.models import HackerNews

hviews = Blueprint('hviews', __name__)

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
        author = row.find_next_sibling('tr').find('a', class_ = 'hnuser')

        if author:
            author = author.text
        else:
            author = "Unknown"

        data.append({
            'title': title,
            'link': link,
            'author': author,
        })

    return data


@hviews.route('/hacker-news', methods=['GET', 'POST'])
def hacker_news():
    if request.method == 'POST':
        return redirect('/')

    # new data from hacker news
    data = get_hacker_news()

    # existing data from database
    hnews = HackerNews.get_all_news()

    # loop through data
    for news in data:
        # check if news already exists in database
        if not news in hnews:
            hnew = HackerNews(title=news['title'], link=news['link'])
            hnew.save()
        else:
            continue

    return render_template('hacker_news.html', data=hnews)