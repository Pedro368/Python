import sqlite3

connection = sqlite3.connect('Ficheros\\demo.db')
cursor = connection.cursor()



#En una base de datos nueva, necesitamos inicialmente crear las tablas
#Estas sentencias se ejecutan una sola vez

command = "SELECT *count() FROM sqlite_master WHERE type = 'table' AND name = 'Alumno'"
cursor.execute(command)
tablas = cursor.fetchone()[0]
if(tablas == 0):
    command = "CREATE TABLE Alumno (id, nombre, apellidos, curso, notas)"
    cursor.execute(command)

#Insertar un registro en la base de datos
command = "INSERT INTO Alumno (id, nombre) VALUES ('A00', 'Borja')"