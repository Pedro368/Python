from datetime import datetime
import time

dt1 = datetime.now().date()
dt2 = datetime.now()
print("Fecha1: ", dt1)
print("Fecha2: ", dt2)
print("Año: ", dt2.year)
print("Mes: ", dt2.month)
print("Dia: ", dt2.day)
print("Fecha2: ", dt2.hour)

fecha = "14-03-1985"
print("Escribe una fecha: ")
fecha2 = input()
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()
print("Fecha2", dt3)
dt4 = datetime.strptime(fecha2, "%d-%m-%Y").date()
print("Fecha2", dt4)
años = dt1.year - dt4.year

print("Fecha3" , dt3.strftime("%A, %d de %b de %Y"))
print(f"Tienes {años} años.")
