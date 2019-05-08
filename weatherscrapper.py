import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.5569&lon=-121.9914#.XNHK4pNKi_U")
soup = BeautifulSoup(page.content,'html.parser')
print(soup)

# To find all the links with a tag

print(soup.findall("a"))
