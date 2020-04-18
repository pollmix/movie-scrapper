import json
import requests
from bs4 import BeautifulSoup
import app

data_reset = open("data.json", "w")
data_reset.write("")
data_reset.close()

data = open("data.json", "a")


def parse_url(url):
    return BeautifulSoup(requests.get(url).text, 'lxml')


website_url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'


movies_tr = parse_url(website_url).find(
    'table', class_='wikitable sortable').tbody.find_all('tr')

movies_link = []

for tr in movies_tr:
    if tr.find('a'):
        movies_link.append('https://en.wikipedia.org'+tr.find('a').get('href'))


movies_info = []

i = 1

for link in movies_link:
    movie_info = {
        "Title": None,
        "Directed by": None,
        "Produced by": None,
        "Written by": None,
        "Starring": None,
        "Music by": None,
        "Cinematography": None,
        "Edited by": None,
        "Distributed by": None,
        "Release date": None,
        "Running time": None,
        "Country": None,
        "Language": None,
        "Budget": None,
        "Box office": None,
    }

    try:
        table_row = parse_url(link).find(
            'table', class_="infobox vevent").tbody.find_all('tr')

        for index, tr in enumerate(table_row):
            if index == 0:
                movie_info["Title"] = tr.find('th').text

            if tr.find('th') and tr.find('td') and tr.find('th').text in movie_info:
                movie_info[tr.find('th').text] = tr.find('td').text

        movies_info.append(movie_info)

        print(movie_info)
        
        # Adding data to database
        app.add_movie_from_scrape(movie_info)

        if i == 5:
            break

        i = i + 1

    except:
        print('\n'+link + " is not formatted well. Escaped"+'\n')


data.write(json.dumps(movies_info))
data.close()