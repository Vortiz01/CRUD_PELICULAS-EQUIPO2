import sys

from pelicula import Pelicula
entry = sys.stdin

def showseparator():
    print("="*120)

def showMenu():
    showseparator()
    print("")
    print("\t\t\t\t\t\tPELICULAS APP V0.0.1")
    print("")
    showseparator()

    print("1-------Ingresar Pelicula")
    print("2-------Mostrar Peliculas")
    print("3-------Actualizar Pelicula")
    print("4-------Eliminar Pelicula")
    showseparator()
    print("5-------Salir del Sistema")
    print("Ingrese su opcion:")
    
def showRegistroClase(peliculas):
    print("codPelicula\tnomPelicula\t\tAutor\t\tGenero\t\t\tProtagonista\t\tFechaEstreno")
    showseparator()
    for pelicula in peliculas:
        pelicula.obtenerFormatoColumna()
    showseparator()

def getParametros():
    showseparator()
    print("Registros de datos")
    showseparator()
    print("Ingrese el codigo de la pelicula:")
    codPeli = entry.readline().lstrip().rstrip()
    print("Ingrese el nombre de la pelicula")
    nombre = entry.readline().lstrip().rstrip()
    print("Ingrese el autor: ")
    autor = entry.readline().lstrip().rstrip()
    print("Ingrese el genero de la pelicula: ")
    genero = entry.readline().lstrip().rstrip()
    print("Ingrese el nombre del protagonista: ")
    prota = entry.readline().lstrip().rstrip()
    print("Ingrese la fecha en que se estreno la pelicula [dd/mm/aaaa]:")
    fechaEstreno = entry.readline().lstrip().rstrip()
    parametros = (codPeli,nombre,autor,genero,prota,fechaEstreno)
    return parametros

def updateCod():
    showseparator()
    print("Ingrese el codigo del registro a actualizar:")
    cod = entry.readline().lstrip().rstrip()
    return cod

def deleteCod():
    showseparator()
    print("Eliminar Registro")
    showseparator()
    print("Ingrese el codigo del regitro a eliminar: ")
    codDelete = entry.readline().rstrip().lstrip()
    return codDelete