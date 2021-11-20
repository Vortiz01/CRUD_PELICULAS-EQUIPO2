class Pelicula:
    codPelicula = ""
    nombre = ""
    autor = ""
    genero = ""
    prota = ""
    fechaEstreno = ""

    def obtenerFormatoColumna(self):
        print(self.codPelicula +"\t\t"+ self.nombre +"\t\t" + self.autor +"\t\t" + self.genero +"\t\t" + self.prota +"\t\t\t" + self.fechaEstreno)