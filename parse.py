import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
data = []
for p in range(1, 6):
#    url = f"https://www.kinopoisk.ru/lists/top250/?page={p}&tab=all"
    r = requests.get(f"https://www.kinopoisk.ru/lists/top250/?page={p}&tab=all")
    soup = BeautifulSoup(r.text, 'lxml')
#    films = soup.findAll('div', class_='desktop-rating-selection-film-item')
    sleep(3)
    for film in soup.findAll('div', class_='desktop-rating-selection-film-item'):
        print('go', p)
        link = "https://www.kinopoisk.ru"+film.find('a', class_="selection-film-item-meta__link").get('href')
        russian_name = film.find('p', class_='selection-film-item-meta__name').text
        original_name = film.find('p', class_='selection-film-item-meta__original-name').text
        country = film.find('span', class_='selection-film-item-meta__meta-additional-item').text
        film_type = film.findAll('span', class_='selection-film-item-meta__meta-additional-item')[1].text
        rate = film.find('span', class_='rating__value rating__value_positive').text
        header = ['link', 'russian_name', 'original_name', 'country', 'film_type', 'rate']
        data.append([link, russian_name, original_name, country, film_type, rate])
df = pd.DataFrame(data, columns=header)
df.to_csv("/Users/seligenenko/kino.csv", sep=';', encoding='utf8')