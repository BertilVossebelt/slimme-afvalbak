import requests

barcode = input("barcode: ")
result = requests.get('https://www.coop.nl/zoeken/' + barcode)
print(result.content)


