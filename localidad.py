
class Localidad:
    """representa una localidad dentro de un municipio del area metropolitana de caracas"""
    def __init__(self, nombre, nombre_municipio, latitud, longitud): 
        """parametros:
        nombre de la localidad (string)
        nombre del municipio al que pertenece (string)
        latitud geografica (float si tiene, None si no tiene)
        longitud georgrafica (float si tiene, None si no tiene)"""
        self.nombre = nombre
        self.nombre_municipio = nombre_municipio
        self.latitud = latitud
        self.longitud = longitud

    def tiene_coordenadas(self):
        """devuelve True si la localidad tiene latitud y longitud conocidas, False en caso contrario"""

        return self.latitud is not None and self.longitud is not None

    def coincide_con(self, texto_buscado):
        """indica si el nombre de la localidad contiene el texto buscado, no importan mayusculas o minusculas
        parametros:
        texto o parte del nombre que el usuario esta buscando 
        
        devuelve true si el nombre de la localidad contiene el texto buscado"""

        return texto_buscado.lower() in self.nombre.lower()

    def show(self):
        """imprime en la pantalla el nombre, municipio y coordenadas de la localidad"""
        print(f"Nombre: {self.nombre}")
        print(f"Nombre del Municipio: {self.nombre_municipio}")
        if self.tiene_coordenadas():
            print(f"Coordenadas: ({self.latitud}, {self.longitud})")
        else: 
            print("Coordenadas: No disponibles")

            
