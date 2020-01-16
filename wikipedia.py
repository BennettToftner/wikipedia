import requests
from bs4 import BeautifulSoup

countryNames = []
countryPops = []

URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

wikitable = soup.find(id='main')
rows = wikitable.find_all('tr')

for row in rows:
    data = row.find_all('td')
    count = 0
    for datum in data:
        if count == 0:
            name_elem = datum.find_all('a')
            countryNames.append(name_elem[0].text)
        if count == 4:
            countryPops.append(datum.text)
        count = count + 1

count = 0
for name in countryNames:
    print(name)
    print(countryPops[count])
    count += 1
