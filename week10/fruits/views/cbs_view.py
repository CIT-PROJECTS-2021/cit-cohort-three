from flask import Blueprint
from fruits.models import CBSNews
import requests
from bs4 import BeautifulSoup


cviews = Blueprint('cbs', __name__, url_prefix='/cbs_news')

# /cbs_news
# /cbs_news/add

def scrape_cbs():
    url = 'https://www.cbsnews.com/latest/rss/main'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="xml")
    news = soup.find_all('item')
    data = []
    for new in news:
        # print(new.link.text)
        # <Link />
        title = new.title.text
        link = new.link.text
        image = new.image.text
        description = new.description.text
        data.append({
            'title': title,
            'link': link,
            'image': image,
            'description': description,
        })
    return data
        



@cviews.route('/')
def index():
    data = scrape_cbs()
    
    # existing data
    cbs_data = CBSNews.get_all_news()

    # check if data already exists
    for news in data:
        if news['title'].lower() not in [cbs.title.lower() for cbs in cbs_data]:
            cbs = CBSNews(
                title=news['title'],
                link=news['link'],
                image=news['image'],
                description=news['description'],
            )
            cbs.save()
        else:
            continue

    return {'data': [cbs.serialize() for cbs in CBSNews.get_all_news()]}
