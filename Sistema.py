import json
from Localidad import Localidad
from Municipio import Municipio


class Sistema:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.municipios = []

    def start(self):

        self.cargar_datos()
        self.mostrar_reporte_de_carga()

        while True:

            menu = input("Bienvenido a MeteoCaracas. Escoja una opcion:\n1. Reporte de carga de datos\n2. Clima por municipio y localidad\n3. Buscar localidad por nombre\n4. Estadisticas de la sesion\n5. Historico por periodo\n6. Salir\n-->")

            if menu == "1":
                self.mostrar_reporte_de_carga()

            elif menu=="2":
                print("\nFuncionalidad en construccion: consulta de clima por municipio y localidad")
                print()

            elif menu=="3":
                print("\nFuncionalidad en construccion: busqueda de localidad por nombre")
                print()

            elif menu=="4":
                print("\nFuncionalidad en construccion: estadisticas de la sesion")
                print()

            elif menu=="5":
                print("\nFuncionalidad en construccion: historico por periodo")
                print()

            elif menu=="6":
                print("\nHasta luego.")

            else:
                print("\nOpcion no valida. Seleccione una opcion del menu:")
                print()

    def cargar_datos(self):
        with open(self.ruta_json, encoding="utf-8") as archivo:
            datos=json.load(archivo)

        self.municipios=[]
        for nombre_municipio, lista_localidades in datos.items():
            nombre_legible=nombre_municipio.replace("_", " ")
            municipio=Municipio(nombre_legible)
            for loc in lista_localidades:
                localidad=Localidad(loc["localidad"], nombre_legible, loc["latitud"], loc["longitud"])
                municipio.agregar_localidad(localidad)
            self.municipios.append(municipio)

    def mostrar_reporte_de_carga(self):
        print("\n==Reporte de Carga de Datos==")

        for municipio in self.municipios:
            total = len(municipio.localidades())
            con_coords = len(municipio.localidades_con_coordendas())
            sin_coords = len(municipio.localidades_sin_coordenadas())
            porcentaje = (con_coords / total * 180) if total > 0 else 0

            print(f"\nMunicipio: {municipio.nombre}")
            print(f"Localidades cargadas: {total}")
            print(f"Con coordenadas geograficas: {con_coords}")
            print(f"Sin coordenadas geograficas: {sin_coords}")
            print(f"Porcentaje con coordenadas: {porcentaje:.2f}%")





    

        