class Municipio:

    def __init__(self, nombre):
        self.nombre=nombre
        self.localidades=[]

    def agregar_localidad(self, localidad):
        self.localidades.append(localidad)

    def localidades_con_coordenadas(self):

        return [localidad for localidad in self.localidades if localidad.tiene_coordenadas()]

    def localidades_sin_coordenadas(self):

        return [localidad for localidad in self.localidades if not localidad.tiene_coordenadas()]

    def busqueda_de_localidad_por_nombre(self, texto_buscado):

        return [localidad for localidad in self.localidades if localidad.coincide_con(texto_buscado)]

    def show(self):
        print(f"Municipio: {self.nombre} ({len(self.localidades)} localidades)")


    


