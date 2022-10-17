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

import requests
import csv
from bs4 import BeautifulSoup


def save_to_csv(data, filename):
    """Save data to csv file"""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())


def get_top_movies():
    """Get top movies on IMDB since 1980"""
    url = 'https://www.imdb.com/search/title/?release_date=1980-01-01,2019-12-31&sort=num_votes,desc'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('div', class_='lister-item mode-advanced')
    data = []
    for movie in movies:
        title = movie.h3.a.text
        year = movie.h3.find('span', class_='lister-item-year').text
        rating = movie.strong.text
        metascore = movie.find('span', class_='metascore').text if movie.find('span', class_='metascore') else None
        votes = movie.find('span', attrs={'name': 'nv'})['data-value']
        gross = movie.find('span', attrs={'name': 'nv'})['data-value'] if movie.find('span', attrs={'name': 'nv'}) else None
        director = movie.find('p', class_='').text.split('|')[0].strip()
        actors = movie.find('p', class_='').find_all('a')[1:]
        actors = [actor.text.strip() for actor in actors]
        runtime = movie.find('span', class_='runtime').text if movie.find('span', class_='runtime') else None
        genre = movie.find('span', class_='genre').text.strip()
        description = movie.find_all('p', class_='text-muted')[1].text.strip()
        data.append({
            'title': title,
            'year': year,
            'rating': rating,
            'metascore': metascore,
            'votes': votes,
            'gross': gross,
            'director': director,
            'actors': actors,
            'runtime': runtime,
            'genre': genre,
            'description': description
        })
    return data



def get_hacker_news():
    """Get top 100 stories on Hacker News"""
    url = 'https://news.ycombinator.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = soup.find_all('tr', class_='athing')
    data = []
    for story in stories:
        title = story.find('span', class_='titleline').a.text
        link = story.find('span', class_='titleline').a['href']
        points = story.find_next_sibling('tr').find('span', class_='score').text.split()[0]
        comments = story.find_next_sibling('tr').find_all('a')[-1].text.split()[0]
        author = story.find_next_sibling('tr').find('a', class_='hnuser').text
        rank = story.find('span', class_='rank').text.split('.')[0]
        data.append({
            'title': title,
            'link': link,
            'points': points,
            'comments': comments,
            'author': author,
            'rank': rank
        })
    return data


def main():
    """Main function"""
    data = get_top_movies()
    save_to_csv(data, 'top_movies.csv')
    data = get_hacker_news()
    save_to_csv(data, 'hacker_news.csv')
    print("Finished scraping and saving data to csv files")


if __name__ == '__main__':
    main()