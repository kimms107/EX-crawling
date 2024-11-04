from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
def	getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None	
    try:
        bsObj =	BeautifulSoup(html.read(), 'html.parser')
        value = bsObj.body.find(tag)
    except AttributeError as e:
        return None	
    return value
tag='h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag)
if value == None:
    print(f'{tag} could not be found')
else:
    print(value)
def use_urlopen(url):
    urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)
    soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
    print(soup)
def	use_requests(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.text)
    print(soup)
def	main():
    melon_url = 'https://www.melon.com/chart/index.htm'
    use_urlopen(melon_url)
    use_requests(melon_url)
main()