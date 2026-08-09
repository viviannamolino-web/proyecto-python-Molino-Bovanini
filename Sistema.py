import json
from Localidad import Localidad
from Municipio import Municipio
from datetime import datetime
from ClimaAPI import consultar_clima_actual
from RegistroConsulta import RegistroConsulta
from HistoricoAPI import consultar_historico
from GraficoHistorico import graficar_evolucion_anual

class Sistema:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.municipios = []
        self.consultas_realizadas = []

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

        municipio = self.municipios[int(opcion) - 1]
        localidades_validas = municipio.localidades_con_coordenadas()

        if not localidades_validas:
            print("Este municipio no tiene localidades con coordenadas registradas.")
            return

        print(f"Localidades de {municipio.nombre} con coordenadas")
        for indice, localidad in enumerate(localidades_validas, start=1):
            print(f"{indice}. {localidad.nombre}")

        opcion_localidad = input("Seleccione el numero de la localidad: ")
        if not opcion_localidad.isdigit() or not (1 <= int(opcion_localidad) <= len(localidades_validas)):
            print("Opcion no valida.")
            return

        localidad = localidades_validas[int(opcion_localidad) - 1]
        self.mostrar_clima_localidad(localidad)

    def mostrar_clima_localidad(self, localidad):
        clima = consultar_clima_actual(localidad.latitud, localidad.longitud)
        if clima is None:
            return

        print(f"\nMunicipio: {localidad.nombre_municipio}")
        print(f"Localidad: {localidad.nombre}")
        print(f"Coordenadas: ({localidad.latitud}, {localidad.longitud})")
        clima.show()

        self.consultas_realizadas.append(RegistroConsulta(localidad, clima))

    def buscar_por_nombre(self):
        texto = input("Ingrese el nombre (o parte del nombre) de la localidad a buscar: ")

        coincidencias = []
        for municipio in self.municipios:
            for localidad in municipio.buscar_localidad_por_nombre(texto):
                if localidad.tiene_coordenadas():
                    coincidencias.append(localidad)

        if not coincidencias:
            print("No se encontraron las localidades con ese nombre que tengan coordenandas registradas.")
            return

        print("\nCoincidencias encontradas:")
        for indice, localidad in enumerate(coincidencias, start = 1):
            print(f"{indice}. {localidad.nombre} ({localidad.nombre_municipio})")

        opcion = input("Seleccione el numero de la localidad: ")
        if not opcion.isdigit() or not (1 <= int(opcion) <= len(coincidencias)):
            print("Opcion no valida.")
            return

        localidad  = coincidencias[int(opcion) - 1]
        self.mostrar_clima_localidad(localidad)

        


            






    

        