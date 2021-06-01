import requests

url = 'https://www.zippopotam.us/es/'
postalCode = input('Codigo Postal: ')

response = requests.get(url + postalCode)

if(response.status_code == 200):
        data = response.json()
        for d in data['places']:
            print('Ciudad:', d['place name'])
            print('Region:', d['state'])
            print('Longitud:', d['longitude'])
            print('Latitud:', d['latitude'])
            print('')
else:
    print('Error:', response.reason)