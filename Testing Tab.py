import urllib.request
import re
from bs4 import BeautifulSoup

barcode = input("barcode: ")


html_page = urllib.request.urlopen("https://www.coop.nl/zoeken/" + barcode)
soup = BeautifulSoup(html_page)
for link in soup.findAll(barcode):
    if link.get('href').find('/product') == 1:
        print(link)


