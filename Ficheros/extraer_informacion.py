from pymongo import MongoClient

#Conecion con MongoDB
connect = MongoClient('mongodb://localhost:27017/')
db = connect.Northwind

#Cuantos productos tenemos?
productos = db.products
numProductos = productos.estimated_document_count()
print("Numero de productos: ", numProductos)

#Buscar y Mostrar todos los productos
listProductos = productos.find()

for n in listProductos:
    print(f"{n['ProductName']}")

print("")

cursor = productos.find()
while(cursor.alive):
    print(cursor.next()['ProductName'])

print("")

#Buscar todos los productos. Con un filter buscamos los productos con UnitsInStock = 0
listProductos = productos.find
pro = list(filter(lambda p: p['UnitsInStock'] == '0', listProductos))
for p in pro:
    print(f"{p['ProductName']}")

#Buscar los productos con UnitsInStock = 0
cursor = productos.find({'UnitsInStock' : '0'})
while(cursor.alive):
    print(cursor.next()['ProductName'])

#Coste o valor de nuestro stock - producto -> UnitsInStock, UnitPrice

#listProductos = productos.find({'UnitsInStock' : { '$ne': '0'}})
listProductos = productos.find()
valorStock = 0
for n in listProductos:
    valorStock + (float(n['UnitPrice']) * float(n['UnitsInStock']))
    print(f"\nValor del Stock: {valorStock:1.2f}")