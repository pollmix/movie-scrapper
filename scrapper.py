import json
import requests
from bs4 import BeautifulSoup
from Service.MovieService import add_movie_from_scrape
import sys

# Store result into a json file
# data_reset = open("data.json", "w")
# data_reset.write("")
# data_reset.close()
# data = open("data.json", "a")


def parse_url(url):
    return BeautifulSoup(requests.get(url).text, 'lxml')


website_url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'

print('Start scrapping the main list...')

movies_tr = parse_url(website_url).find(
    'table', class_='wikitable sortable').tbody.find_all('tr')

movies_link = []

for tr in movies_tr:
    if tr.find('a'):
        movies_link.append('https://en.wikipedia.org'+tr.find('a').get('href'))


# movies_info = []

print('Start scrapping individual movie...')

i = 1
n = -1

if len(sys.argv) > 1:
    try: 
        n = int(sys.argv[1])
    except:
        pass

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
        "number_of_ratings": None,
        "ratings": None,
    }

    try:
        table_row = parse_url(link).find(
            'table', class_="infobox vevent").tbody.find_all('tr')

        for index, tr in enumerate(table_row):
            if index == 0:
                movie_info["Title"] = tr.find('th').text

            if tr.find('th') and tr.find('td') and tr.find('th').text in movie_info:
                movie_info[tr.find('th').text] = tr.find('td').text

        # movies_info.append(movie_info)

        print("Scrapping " + link)
        
        # Adding data to database
        add_movie_from_scrape(movie_info)

        if i == n:
            break

        i = i + 1

    except:
        print('\n'+link + " is not formatted well. Escaped"+'\n')


# data.write(json.dumps(movies_info))
# data.close()

print('Scrapping done...')
