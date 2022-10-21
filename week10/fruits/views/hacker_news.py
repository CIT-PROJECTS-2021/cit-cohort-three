import json
from flask import Blueprint, request, redirect, render_template
from bs4 import BeautifulSoup
import requests
from fruits.models import HackerNews
from fruits import db
from sqlalchemy import text, engine

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
        # news['title'] is the title of the news
        if news.get('title').lower() not in [hn.title.lower() for hn in hnews]:
            hnew = HackerNews(title=news['title'], link=news['link'])
            hnew.save()
        else:
            continue

    return render_template('hacker_news.html', data=hnews)



@hviews.route('/hacker-news/search', methods=['GET', 'POST'])
def search_hacker_news():
    # /hacker-news/search?q=python
    query = request.args['q']
    # search in database for anythign that matches the query
    # SELECT * FROM hacker_news WHERE title LIKE '%python%'
    # data = db.session.query(HackerNews).filter(HackerNews.title.like(f'%{query}%')).all()
    # sql = text('SELECT * FROM hacker_news WHERE title LIKE :query')
    # data = db.engine.execute(sql, query=f'%{query}%').fetchall()
    data = HackerNews.query.filter(HackerNews.title.like(f'%{query}%')).all()
    # print(data)
    # [<HackNews 1>, <HackNews 2>]
    return {'data': [news.serialize() for news in data]}


@hviews.route('/search')
def search():
    return render_template('search.html')