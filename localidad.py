
class Localidad:
    def __init__(self, nombre, nombre_municipio, latitud, longitud): 
        self.nombre = nombre
        self.nombre_municipio = nombre_municipio
        self.latitud = latitud
        self.longitud = longitud

    def tiene_coordenadas(self):

        return self.latitud is not None and self.longitud is not None

    def coincide_con(self, texto_buscado):

        return texto_buscado.lower() in self.nombre.lower()

    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nombre del Municipio: {self.nombre_municipio}")
        if self.tiene_coordenadas():
            print(f"Coordenadas: ({self.latitud}, {self.longitud})")
        else: 
            print("Coordenadas: No disponibles")

            
