import json
from Localidad import Localidad
from Municipio import Municipio


class Sistema:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.municipios = []

    def start(self):

        self.cargar_datos()
        self.mostrar_reporte_carga()

        while True:

            menu = input("Bienvenido a MeteoCaracas. Escoja una opcion:\n1. Reporte de carga de datos\n2. Clima por municipio y localidad\n3. Buscar localidad por nombre\n4. Estadisticas de la sesion\n5. Historico por periodo\n6. Salir\n-->")

            if menu == "1":
                self.mostrar_reporte_carga()

            elif menu=="2":
                print("\nFuncionalidad en construccion: consulta de clima por municipio y localidad")

            elif menu=="3":
                print("\nFuncionalidad en construccion: busqueda de localidad por nombre")

            elif menu=="4":
                print("\nFuncionalidad en construccion: estadisticas de la sesion")

            elif menu=="5":
                print("\nFuncionalidad en construccion: historico por periodo")

            elif menu=="6":
                print("\nHasta luego.")

            else:
                print("\nOpcion no validad: seleccione una opcion del menu")

    def cargar_datos(self):
        with open(self.ruta_json, encoding="utf-8") as archivo:
            datos=json.load(archivo)



    

        