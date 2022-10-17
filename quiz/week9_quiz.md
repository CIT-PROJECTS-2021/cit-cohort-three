
# End of week 9 quiz

1. Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order. The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order.




2. Scrap Hacker News project and save the result in a csv file. The csv file should have the following columns: title, link, points, comments, author, rank. The csv file should be sorted by rank in ascending order.

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]

# create a empty list for storing
# movie information
list = []
 
# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
     
    # Separating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)

for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
          ') -', 'Starring:', movie['star_cast'], movie['rating'])

#saving the list as dataframe
#then converting into .csv file
df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv',index=False)

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
 
 
# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
 
 
 
 
# create a empty list for storing
# movie information
list = []
 
# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
     
    # Separating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)
 
# printing movie details with its rating.
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
        ') -', 'Starring:', movie['star_cast'], movie['rating'])
 
 
##.......##
df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv',index=False)

