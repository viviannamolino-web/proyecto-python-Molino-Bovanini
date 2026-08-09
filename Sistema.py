import json
from Localidad import Localidad
from Municipio import Municipio
from datetime import datetime
from ClimaAPI import ClimaAPI
from RegistroConsulta import RegistroConsulta
from HistoricoAPI import HistoricoAPI
from GraficoHistorico import GraficoHistorico

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
                self.consultar_por_municipio()
                print()

            elif menu=="3":
                self.buscar_por_nombre()
                print()

            elif menu=="4":
                self.mostrar_estadisticas()
                print()

            elif menu=="5":
                self.consultar_historico()
                print()

            elif menu=="6":
                print("\nHasta luego.")
                break

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


    def mostrar_reporte_carga(self):

        print("\n===Reporte de carga de datos===")

    def mostrar_reporte_de_carga(self):
        print("\n==Reporte de Carga de Datos==")

        for municipio in self.municipios:
            total = len(municipio.localidades)
            con_coords = len(municipio.localidades_con_coordenadas())
            sin_coords = len(municipio.localidades_sin_coordenadas())
            porcentaje = (con_coords / total * 100) if total > 0 else 0

            print(f"\nMunicipio: {municipio.nombre}")
            print(f"Localidades cargadas: {total}")
            print(f"Con coordenadas geograficas: {con_coords}")
            print(f"Sin coordenadas geograficas: {sin_coords}")
            print(f"Porcentaje con coordenadas: {porcentaje:.2f}%")

    def consultar_por_municipio(self):
        print("\nMunicipios disponibles:")
        for indice,municipio in enumerate(self.municipios, start=1):
            print(f"{indice}.{municipio.nombre}")

        opcion=input("Seleccione el numero del municipio: ")
        if not opcion.isdigit() or not (1<=int(opcion)<=len(self.municipios)):
            print("Opcion no valida")
            return

        if not localidades_validas:
            print("Este municipio no tiene localidades con coordenadas registradas.")
            return

        print(f"\nLocalidades de {municipio.nombre} con coordenadas:")
        for indice,localidad in enumerate(localidades_validas,start=1):
            print(f"{indice}.{localidad.nombre}")

        opcion_localidad=input("Seleccione el numero de la localidad: ")
        if not opcion_localidad.isdigit() or not (1<=int(opcion_localidad)<=len(localidades_validas)):
            print("Opcion no valida.")
            return

        localidad=localidades_vvalidas[int(opcion_localidad)-1]
        fecha_inicio=input("Ingrese la fecha de inicio (AAAA-MM-DD): ")
        fecha_fin=input("Ingrese la fecha de fin (AAAA-MM-DD): ")

        if not fecha_valida(fecha_inicio) or not self.fecha_valida(fecha_fin):
            print("Las fechas deben tener el formato AAAA-MM-DD.")
            return

        registros_mensuales=self.consultar_historico(localidad.latitud,localidad.longitud,fecha_inicio,fecha_fin)
      



    

        