from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
bs = BeautifulSoup(html.read(), 'html.parser')
