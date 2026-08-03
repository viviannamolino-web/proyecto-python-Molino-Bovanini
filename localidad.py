class Localidad:
    def __init__(self, nombre, latitud=None, longitud=None)
        self.nombre=nombre
        self.latitud=latitud
        self.longitud=longitud

    def tiene_coordenadas(self):

        return self.latitud is not None and self.longitud is not None