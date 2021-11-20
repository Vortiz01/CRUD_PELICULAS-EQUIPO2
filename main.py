from sqlite3.dbapi2 import Cursor
import sys,os
from interface import deleteCod, showseparator,showMenu,showRegistroClase,updateCod
from peliculasdao import createTable, delete,getAllPeliculas,add,delete,update
entry = sys.stdin
option = 0

while True:
    os.system("pause")
    os.system("cls")
    createTable()
    showMenu()
    option = int(entry.readline().lstrip().rstrip())
    if(option <= 5 or option >= 1):
        if(option == 1):
            add()
        elif(option == 2):
            showRegistroClase(getAllPeliculas())
        elif(option == 3):
            update(updateCod())
        elif(option == 4):
            delete(deleteCod())
        elif(option == 5):
            print("GRACIAS POR USAR NUESTRO SISTEMA")
            os.system("cls")
            break
    else:
        print("Ingrese un numero del 1 al 5")


