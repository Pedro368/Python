from datetime import datetime

fecha_sistema = datetime.now().date()
fecha_nacimiento = input("Escribe tu fecha de nacimiento: ")
fn = datetime.strptime(fecha_nacimiento, "%d-%m-%Y").date()
años = fecha_sistema.year - fn.year

if(años>=18):
    print(f"Tienes {años} años, Eres mayor de edad")
else:
    print(f"Te faltan {(18-años)} años para ser mayor de edad")
    