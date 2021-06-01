import json


def PrintData(cliente):
    print(f"ID: {cliente['CustomerID']}")
    print(f"Empresa: {cliente['CompanyName']}")
    print(f"Contacto: {cliente['ContactName']} ({cliente['ContactTitle']})")
    print(f"Direccion: {cliente['Address']}")
    print(f"            {cliente['PostalCode']} {cliente['City']} {cliente['Country']}")
    print(f"Telefono: {cliente['Phone']} Fax: {cliente['Fax']}")

file = open("clientes.json", "rt", encoding='UTF-8')
dataJSON = file.read()
file.close()

clientes = json.loads(dataJSON)

input("ID: ")

busqueda = list(filter(lambda x : x['CustomerID'] == ID, clientes))
if(len(busqueda) == 0):
    print("El identificador no existe.")
else:
    PrintData(busqueda[0])