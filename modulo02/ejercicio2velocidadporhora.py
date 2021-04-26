kilometros_recorrido = int(input("¿Cuantos kilometros has recorrido? "))
horas_empleados = int(input("¿Cuantas horas has necesitado? "))

velocidad = kilometros_recorrido/horas_empleados
print(velocidad)

if(velocidad<30):
    print("Velocidad Moderada")
elif(velocidad>=30 and velocidad<75):
    print("Velocidad Media")
elif(velocidad>=75):
    print("Velocidad Alta")