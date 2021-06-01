from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')



## MOSTRAR EL ESTADO DEL SERVIDOR(MOTOR BASE DE DATOS)

## ASIGNAMOS A LA VARIABLE db EL OBJETO QUE REPRESENTA LA BASE DE DATOS ADMIN
db = client.admin

# EJECUTAMOS COMANDOS EN LA BASE DE DATOS UTILIZANDO LA FUNCION COMMAND
# EL COMANDO SERVERSTATUS NOS RETORNA EL ESTADO DEL SERVIDOR
status = db.command("serverStatus")
pprint(status)

# TRABAJANDO CON DATOS
# SELECICONAR LA BASE DE DATOS CON LA QUE VAMOS A TRABAJAR
#northwindDB = client['Northwind']
northwindDB = client.Northwind

#LISTAR LAS COLECCIONES DE LA BASE DE DATOS
print(northwindDB.list_collection_names())

#SELECCIONAR UNA COLECCION DE LA BASE DE DATOS
#collection = client.Northwind.customers
#collection = client['Northwind']['customers']
#collection = northwindDB['customers']
collection = northwindDB.customers

#UTILIZAMOS estimated_document_count() PARA SABER EL NUMERO DE DOCUMENTOS DE LA COLECCION
result = collection.estimated_document_count()

#BUSCAR DOCUMENTOS DENTRO DE UNA COLECCION
result = collection.find({'CustomerID': 'ANATR'})
pprint(result.count())
pprint(result.alive)
pprint(result.next())
pprint(result.alive)

print(result)

{"_id":{"$oid":"6091317a7821e32a6403ef82"},"OrderID":"10248","ProductID":"11","UnitPrice":"14.00","Quantity":"12","Discount":"0"}