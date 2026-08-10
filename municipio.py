class Municipio:
    """representa un municipio del area metropolitana de caracas y agrupa sus localidades"""

    def __init__(self, nombre):
        """inicia un municipio sin coordenadas todavia 
        parametros:
        nombre del municipio (string)"""
        self.nombre=nombre
        self.localidades=[]

    def agregar_localidad(self, localidad):
        """agrega un objeto localidad a la lista de localidades del municipio"""
        self.localidades.append(localidad)

    def localidades_con_coordenadas(self):
        """devuelve la lista de objetos de localidad del municipio que tienen coordenadas validas"""

        return [localidad for localidad in self.localidades if localidad.tiene_coordenadas()]

    def localidades_sin_coordenadas(self):
        """devuelve la lista de objetos de localidad del municipio que no tienen coordenadas"""

        return [localidad for localidad in self.localidades if not localidad.tiene_coordenadas()]

    def buscar_localidad_por_nombre(self, texto_busqueda):
        """busca localidades del municipio cuyo nombre contenga el texto indicado
        parametro:
        texto o parte del texto buscado (string)
        devuelve localidades del municipio que coinciden con la busqueda en forma de lista"""

        return[localidad for localidad in self.localidades if localidad.coincide_con(texto_busqueda)]

    def show(self):
        """imprime en pantalla el nombre del municipio y la cantidad de localidades que contiene"""
        print(f"Municipio: {self.nombre} ({len(self.localidades)} localidades)")

       


