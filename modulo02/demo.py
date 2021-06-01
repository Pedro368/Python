import pymssql

conexion = pymssql.connect(server='localhost', user='test', password='test100', database='Northwind')

cursor = conexion.cursor()
cursor.execute('SELECT * FROM Customers')

row = cursor.fetchone()
while (row):
    print(f"     ID: {row[0]}")
    print(f"Empresa: {row[1]}")
    print("")
    row = cursor.fetchone()

cursor.close()
conexion.close()