import requests

#Utilizamos la funcion get para realizar llamadas a microservicios en modo GET
url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)


print('Código de estado: ', response.status_code)
print('Estado:', response.reason)

if(response.status_code == 200):
    print('Cabeceras:', response.headers)
    print('Tipo de Contenido:', response.headers['Content-Type'])
    if(response.headers['Content-Type'] == 'Application/json'):
        data = response.json()
        print('Latitud', data['iss_position']['latitude'])
        print('Longitud', data['iss_position']['longitude'])
        print('Timestamp', data['timestamp'])
        print('Mensaje', data['message'])
    else:
        print('Contenido:', response.text)
        print('Contenido:', response.content)
else:
    print('Error:', response.reason)