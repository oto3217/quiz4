import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

payloads = {'limit': 50}
url = 'https://myanimelist.net/topanime.php'
headers = {'Accept-Language': 'en-US'}

file = open('animelist.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['Title', 'Rating'])

for page in range(1, 6):
    payloads['offset'] = (page - 1) * 50

    response = requests.get(url, params=payloads, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    anime_list = soup.find_all('tr', class_='ranking-list')

    for anime in anime_list:
        title = anime.find('div', class_='di-ib clearfix').text.strip()
        rating = anime.find('td', class_='score').text.strip()

        print(f'Title: {title}\nRating: {rating}\n')

        csv_obj.writerow([title, rating])

    sleep(15)

file.close()
