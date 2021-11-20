import sys
from sqlite3.dbapi2 import Cursor
from dao import getConn
from interface import getParametros, showseparator
from pelicula import Pelicula
entry = sys.stdin

conn = getConn()
cursor = conn.cursor()

def createTable():
    global conn
    global cursor

    cursor.execute("CREATE TABLE IF NOT EXISTS PELICULAS (codPelicula text primary key,nomPelicula text not null,autor text not null,genero text not null,prota text not null,fechaEstreno text)")
    conn.commit()

def getAll():
    global cursor
    global conn
    cursor.execute("SELECT * FROM PELICULAS")
    rows = cursor.fetchall()
    return rows

def add():
    global conn
    global cursor

    insertSQL = "INSERT INTO PELICULAS (codPelicula, nomPelicula, autor, genero, prota, fechaEstreno) VALUES (?, ?, ?, ?, ?, ?)"
    parametros = getParametros()
    cursor.execute(insertSQL,parametros)
    conn.commit()
    print("REGISTRO INSERTADO CON EXITO!!!")

def getAllPeliculas():
    rows = getAll()
    peliculas_list = list()
    for row in rows:
        pelicula = Pelicula() 
        pelicula.codPelicula = row[0]
        pelicula.nombre = row[1]
        pelicula.autor = row[2]
        pelicula.genero = row[3]
        pelicula.prota = row[4]
        pelicula.fechaEstreno = row[5]
        peliculas_list.append(pelicula)
    return peliculas_list

def update(codPelicula):
    global cursor
    global conn
    print("Ingrese el nombre de la pelicula:")
    nom = entry.readline().rstrip().lstrip()
    print("Ingrese el autor de la pelicula:")
    autor = entry.readline().rstrip().lstrip()
    print("Ingrese el genero de la pelicula:")
    genero = entry.readline().rstrip().lstrip()
    print("Ingrese el protagonista de la pelicula:")
    prota = entry.readline().rstrip().lstrip()
    print("Ingrese la Fecha de esteno de la pelicula [dd/mm/aaaa]:")
    fecha = entry.readline().rstrip().lstrip()
    updatesql = "UPDATE PELICULAS set nomPelicula=?, autor=?, genero=?, prota=?, fechaEstreno=? where codPelicula=?;"
    cursor.execute(updatesql,(nom,autor,genero,prota,fecha,codPelicula))
    print("REGISTRO ACTUALIZADO CON EXITO!!!")
    showseparator()
    conn.commit()

def delete(codPelicula):
    global cursor
    global conn
    print("Seguro que desea eliminar el registro? [S - N]")
    decision = entry.readline().lstrip().rstrip().upper()

    if decision == "N":
        exit()
    elif decision == "S":
        deleteSql = "DELETE FROM PELICULAS WHERE codPelicula = ?;"
        cursor.execute(deleteSql,codPelicula)
        print("REGISTRO ELIMINADO CON EXITO!!!")
        showseparator()
        conn.commit()
