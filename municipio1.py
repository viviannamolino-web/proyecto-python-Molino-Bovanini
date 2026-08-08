class Municipio:

    def __init__(self, nombre):
        self.nombre = nombre
        localidades = []  # Error 1: Falta 'self.' (la lista se crea como variable local y se pierde)

    def agregar_localidad(self, localidad):
        self.localidades.apend(
            localidad
        )  # Error 2: Tipeo 'apend' en vez de 'append'

    def localidades_con_coordenadas(self):
        # Error 3: Se usa 'self.coordenadas' en vez de 'localidad.coordenadas'
        return [
            localidad for localidad in self.localidades if self.coordenadas
        ]

    def localidades_sin_coordenadas(self):
        return [
            localidad
            for localidad in self.localidades
            if not localidad.coordenadas
        ]

    def busqueda_de_localidad_por_nombre(self, texto_busqueda):
        for localidad in self.localidades:
            if localidad.nombre == texto_busqueda:
                localidad  # Error 4: Se olvidó el 'return' antes de localidad