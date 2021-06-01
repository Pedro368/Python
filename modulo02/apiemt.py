import requests

url = {
    'Base' : 'https://openapi.emtmadrid.es/v1/',
    'Login' : 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/'
}
headers = { 'X-ClientId' : 'd84d5b34-3778-43cd-a491-17a5618bc49c', 'passKey' : 'AF76995F19AB2C095D125FFA2C52182F86DAFD8FECE31114F816E86AA19E18065007C243723DF4BD069EA28163147B34B0F110FFB5269AC55D9DE16DE4407B9C'}
toker = None

response = requests.get(url)
print(response.json()['message'])