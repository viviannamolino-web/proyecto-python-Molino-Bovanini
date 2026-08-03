import json
from Localidad import Localidad
from Municipio import Municipio


class Sistema:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.municipios = []

    def start(self):

        while True:

            menu = input("Bienvenido a MeteoCaracas. Escoja una opcion:\n1. Reporte de carga de datos\n2. Clima por municipio y localidad\n3. Buscar localidad por nombre\n4. Estadisticas de la sesion\n5. Historico por periodo\n6. Salir\n-->")

            if menu == "1":
                None



    

        