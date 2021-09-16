import urllib.request
from bs4 import BeautifulSoup
from api.setter import Setter

barcode = input("barcode: ")

html_page = urllib.request.urlopen("https://coop.nl/zoeken/" + barcode)
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    if type(link.get('href')) == str and link.get('href').find(barcode) >= 0:
        url = link.get('href')
        product_name = url.rsplit('/', 1)[1].replace('-', ' ')
        Setter().set(barcode, product_name)
