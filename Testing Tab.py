import urllib.request
from bs4 import BeautifulSoup


barcode = input("barcode: ")


html_page = urllib.request.urlopen("https://coop.nl/zoeken/" + barcode)
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    if type(link.get('href')) == str and link.get('href').find(barcode) >= 0:
        url = link.get('href')
        print(url.rsplit('/', 1)[1].replace('-', ' '))






