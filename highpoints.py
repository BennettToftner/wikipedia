import requests
from bs4 import BeautifulSoup

stateNames = []
highestPoints = []
highestBuildings = []
buildingElevations = []
urlExtensions = []

URL = "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_elevation"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

wikitable = soup.find_all('table')
rows = wikitable[0].find_all('tr')
rows.pop(len(rows) - 1)

for row in rows:
    data = row.find_all('td')
    count = 0
    for datum in data:
        if count == 0:
            name_elem = datum.find_all('a')
            stateNames.append(name_elem[0].text)
        if count == 2:
            highestPoints.append(datum.text[0:datum.text.find('f')])
        count += 1

URL = "https://en.wikipedia.org/wiki/List_of_tallest_buildings_by_U.S._state_and_territory"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

wikitable = soup.find_all('table')
rows = wikitable[0].find_all('tr')

for row in rows:
    data = row.find_all('td')
    count = 0
    for datum in data:
        if count == 1:
            link_elem = datum.find_all('a')
            urlExtensions.append(link_elem[0]['href'])
        if count == 4:
            highestBuildings.append(datum.text)
        count += 1

    
#US Virgin Islands
stateNames.pop(51)
highestPoints.pop(51)
highestBuildings.pop(50)
urlExtensions.pop(50)

#United States Minor Outlying Islands
stateNames.pop(48)
highestPoints.pop(48)

#Puerto Rico
stateNames.pop(42)
highestPoints.pop(42)
highestBuildings.pop(42)
urlExtensions.pop(42)

#Northern Mariana Islands
stateNames.pop(37)
highestPoints.pop(37)
highestBuildings.pop(37)
urlExtensions.pop(37)

#Guam
stateNames.pop(12)
highestPoints.pop(12)
highestBuildings.pop(12)
urlExtensions.pop(12)

#District of Columbia
stateNames.pop(9)
highestPoints.pop(9)
highestBuildings.pop(9)
urlExtensions.pop(9)

#American Samoa
stateNames.pop(2)
highestPoints.pop(2)
highestBuildings.pop(2)
urlExtensions.pop(2)

baseURL = "https://en.wikipedia.org"

for extension in urlExtensions:
    URL = baseURL + extension
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tables = soup.find_all('table')
    infoboxIndex = 0
    for table in tables:
        rowsTest = table.find_all('tr')
        headersTest = rowsTest[0].find_all('th')
        if len(headersTest) == 0:
            infoboxIndex += 1
        else:
            break
    infobox = tables[infoboxIndex]
    rows = infobox.find_all('tr')
    for row in rows:
        headers = row.find_all('th')
        if len(headers) > 0:
            header = headers[0]
            elevText = header.text + ""
            elevText = elevText.lower()
            if elevText.find("elevation") == 0:
                data = row.find_all('td')
                buildingElevations.append(data[0].text)




count = 0
for name in stateNames:
    print(name)
    print(highestPoints[count])
    print(highestBuildings[count])
    print(urlExtensions[count])
    print(buildingElevations[count])
    count += 1


print(len(stateNames))