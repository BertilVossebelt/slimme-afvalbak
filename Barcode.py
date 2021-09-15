import requests

barcode = input("barcode: ")
# print('https://www.jumbo.com/zoeken?searchTerms=' + barcode)
result = requests.get('https://www.jumbo.com/zoeken?searchTerms=' + barcode)
print(result)
