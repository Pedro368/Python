class Cliente:
    Identificador = None
    Nombre = None
    Apellidos = None
    Genero = None
    Pais = None
    FechaNacimiento = None

def __init__

def BuscarClienteId (Item):


def BuscarClienteHombre (Item):
    Male = 0
    Female = 0
    if == item.Genero == "Male":
        return True
    else:
        return False

def BuscarClienteMujer (Item):
    Male = 0
    Female = 0
    if == item.Genero == "Female":
        return True
    else:
        return False

path = "D:\\Python curso EOI\\Python\\modulo02\\fichero.txt"
file = open(path)

for d in (open(path).readlines()):
    data = d.split(",")
for linea in (file.readlines()):
    datos = linea.split(",")
    if(datos[0].isdigit() == True):
        cliente = Cliente(datos[7].strip(), datos[1].strip(), datos[2].strip())
        cliente.Genero = datos[3].strip()
        clientes.append(cliente)

resultado = list(filter(lambda x: x.Identificador == "1562", clientes))
print(len(resultado))

hombres = list(filter)
print