import requests

url = 'http://school.labs.com.es/api/students/'
postalCode = input('Codigo Postal: ')

response = requests.get(url + postalCode)
