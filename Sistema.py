import json
from Localidad import Localidad
from Municipio import Municipio
from datetime import datetime
from ClimaAPI import consultar_clima_actual
from RegistroConsulta import RegistroConsulta
from HistoricoAPI import consultar_historico
from GraficoHistorico import graficar_evolucion_anual

class Sistema:
    """Controla el flujo principal de MeteoCaracas: carga de datos, menu, clima, estadisticas e historicos"""
    def __init__(self, ruta_json):
        """Inicializa el sistema. Parametros: ruta_json (str): ruta del archivo JSON con la informacion de municipios y localidades."""

        self.ruta_json = ruta_json
        self.municipios = []
        self.consultas_realizadas = []

    def start(self):
        """Punto de entrada: carga los datos, muestra el reporte inicial y despliega el menu principal."""
        self.cargar_datos()
        self.mostrar_reporte_de_carga()

        while True:

            menu = input("Bienvenido a MeteoCaracas. Escoja una opcion:\n1. Reporte de carga de datos\n2. Clima por municipio y localidad\n3. Buscar localidad por nombre\n4. Estadisticas de la sesion\n5. Historico por periodo\n6. Salir\n-->")

            if menu == "1":
                self.mostrar_reporte_de_carga()
                print()

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
        """Lee el archivo JSON de municipios y localidades, y construye la lista de objetos Municipio, cada uno con su lista de objetos Localidad."""
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
        """Imprime en pantalla, por cada municipio, la cantidad de localidades cargadas, cuantas tienen coordenadas geograficas, cuantas no, y el porcentaje de localidades con coordenadas."""
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
        """Permite al usuario elegir un municipio y luego una de sus localidades con coordenadas validas, y muestra el clima actual de la localidad seleccionada."""
        print("\nMunicipios disponibles:")
        for indice,municipio in enumerate(self.municipios, start=1):
            print(f"{indice}.{municipio.nombre}")

        opcion=input("Seleccione el numero del municipio: ")
        if not opcion.isdigit() or not (1<=int(opcion)<=len(self.municipios)):
            print("Opcion no valida")
            return

        municipio=self.municipios[int(opcion)-1]
        localidades_validas=municipio.localidades_con_coordenadas()

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

        localidad=localidades_validas[int(opcion_localidad)-1]
        self.mostrar_clima_localidad(localidad)

    def buscar_por_nombre(self):
        """Permite al usuario buscar localidades por nombre (o parte del nombre) en todos los municipios, y muestra el clima actual de la localidad que seleccione."""

        texto=input("Ingrese el nombre (o parte del nombre) de la localidad a buscar: ")
        coincidencias=[]
        for municipio in self.municipios:
            for localidad in municipio.buscar_localidad_por_nombre(texto):
                if localidad.tiene_coordenadas():
                    coincidencias.append(localidad)

        if not coincidencias:
            print("No se encontraron localidades con ese nombre que tengan coordenadas registradas.")
            return

        opcion=print("\nCoincidencias encontradas:")
        for indice,localidad in enumerate(coincidencias,start=1):
            print(f"{indice}.{localidad.nombre} ({localidad.nombre_municipio})")

        opcion=input("Seleccione el numero de la localidad:")
        if not opcion.isdigit() or not (1<=(int(opcion))<=len(coincidencias)):
            print("Opcion no valida.")
            return

        localidad=coincidencias[int(opcion)-1]
        self.mostrar_clima_localidad(localidad)

    def mostrar_clima_localidad(self,localidad):
        """Consulta el clima actual de una localidad (via ClimaAPI) y lo muestra en pantalla junto con el municipio, la localidad y sus coordenadas. Guarda la consulta en el historial de la sesion. Parametros: localidad (Localidad): localidad de la cual se quiere consultar el clima."""

        clima=consultar_clima_actual(localidad.latitud,localidad.longitud)

        if clima is None:
            return

        print(f"Municipio: {localidad.nombre_municipio}")
        print(f"Localidad: {localidad.nombre}")
        print(f"Coordenadas: ({localidad.latitud},{localidad.longitud})")
        clima.show()

        self.consultas_realizadas.append(RegistroConsulta(localidad,clima))

    def mostrar_estadisticas(self):
        """Muestra el submenu de estadisticas y reportes: ranking, cobertura geografica y promedio general."""

        while True:
            opcion=input(
                "\n=== Estadisticas y Reportes===\n"
                "1. Ranking de temperatura (localidad mas calida y mas fria)\n"
                "2. Cobertura geogafica (localidades sin coordenadas)\n"
                "3. Promedio general de temperatura de lasesion\n"
                "4. Volver al menu principal\n"
                "-->"
            )

            if opcion=="1":
                self.mostrar_ranking_temperatura()

            elif opcion=="2":
                self.mostrar_cobertura_geografica()

            elif opcion=="3":
                self.mostrar_promedio_general()

            elif opcion=="4":
                break

            else:
                print("Opcion no valida.")

    def mostrar_ranking_temperatura(self):
        """Muestra la localidad mas calida y la mas fria segun las consultas realizadas en la sesion."""
        if not self.consultas_realizadas:
            print("Aun no se ha consultado el clima de ninguna localidad en esta sesion.")
            return

        mas_calida=self.consultas_realizadas[0]
        mas_fria=self.consultas_realizadas[0]

        for registro in self.consultas_realizadas:
            if registro.clima.temperatura>mas_calida.clima.temperatura:
                mas_calida=registro
            if registro.clima.temperatura<mas_fria.clima.temperatura:
                mas_fria=registro

        print("\n--Ranking de Temperatura (segun consultas dela sesion)--")
        print(
            f"Localidad mas calida: {mas_calida.localidad.nombre} "
            f"({mas_calida.localidad.nombre_municipio}) - {mas_calida.clima.temperatura} C"
        )

        print(
                    f"Localidad mas fria: {mas_fria.localidad.nombre} "
                    f"({mas_fria.localidad.nombre_municipio}) - {mas_fria.clima.temperatura} C"
                )

    def mostrar_cobertura_geografica(self):
        """Muestra, agrupadas por municipio, las localidades del archivo que no tienen coordenadas registradas."""
        print("\n--Cobertura Geografica: localidades sin coordenadas --")
        for municipio in self.municipios:
            sin_coords=municipio.localidades_sin_coordenadas()
            print(f"\nMunicipio: {municipio.nombre} ({len(sin_coords)} sin coordenadas)")
            for localidad in sin_coords:
                print(f" - {localidad.nombre}")


    def mostrar_promedio_general(self):
        """Calcula y muestra el promedio de temperatura de todas las localidades consultadas en la sesion."""
        if not self.consultas_realizadas:
            print("Aun no se ha consultados el clima de ninguna localidad en esta sesion.")
            return

        suma_temperaturas=0
        for registro in self.consultas_realizadas:
            suma_temperaturas+=registro.clima.temperatura

        promedio=suma_temperaturas/len(self.consultas_realizadas)
        print(
            f"\nPromedio de temperatura de las {len(self.consultas_realizadas)} "
            f"\nlocalidades consultadas: {promedio:.2f} C"
        )

    def fecha_valida(self,texto):
        """Verifica que un texto tenga el formato de fecha AAAA-MM-DD. 
        Parametros: 
        texto (str): texto a validar. 
        Retorna:
        bool: True si el texto tiene el formato de fecha correcto."""

        try:
            datetime.strptime(texto,"%Y-%m-%d")
            return True
        except ValueError:
            return False

    def consultar_historico(self):
        """Permite al usuario elegir una localidad con coordenadas validas y un rango de fechas, y muestra el historico climatico mensual, los promedios del periodo, los años destacados y un grafico comparativo de la evolucion anual."""
        print("\nMunicipios disponibles:")
        for indice,municipio in enumerate(self.municipios,start=1):
            print(f"{indice}.{municipio.nombre}")

        opcion=input("Seleccione el numero del municipio: ")
        if not opcion.isdigit() or not (1<=int(opcion)<=len(self.municipios)):
            print("Opcion no valida")
            return
        
        municipio=self.municipios[int(opcion)-1]
        localidades_validas=municipio.localidades_con_coordenadas()

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

        localidad=localidades_validas[int(opcion_localidad)-1]

        fecha_inicio=input("Ingrese la fecha de inicio (AAAA-MM-DD): ")
        fecha_fin=input("Ingrese la fecha de fin (AAAA-MM-DD): ")

        if not self.fecha_valida(fecha_inicio) or not self.fecha_valida(fecha_fin):
            print("Las fechas deben tener el formato AAAA-MM-DD.")
            return

        registros_mensuales=consultar_historico(localidad.latitud,localidad.longitud,fecha_inicio,fecha_fin)

        if not registros_mensuales:
            print(f"No se pudo obtener el historico para ese periodo.")
            return

        print(f"\n==Historico de {localidad.nombre} ({municipio.nombre})===")
        for registro in registros_mensuales:
            print()
            registro.show()

        self.mostrar_promedios_historico(registros_mensuales)
        self.mostrar_anios_extremos(registros_mensuales)
        graficar_evolucion_anual(registros_mensuales)

    def mostrar_promedios_historico(self, registros_mensuales):
        """Calcula y muestra el promedio de cada magnitud (temperatura, humedad, precipitacion y viento) a lo largo del periodo consultado.
        Parametros:
        registros_mensuales (list): lista de objetos RegistroMensual del periodo consultado."""
        suma_temp = 0
        suma_humedad = 0
        suma_viento = 0
        suma_precipitacion = 0

        for registro in registros_mensuales:
            suma_temp += registro.temperatura
            suma_humedad += registro.humedad
            suma_viento += registro.viento
            suma_precipitacion += registro.precipitacion

        cantidad = len(registros_mensuales)

        print("\n==Promedios del periodo consultado===")
        print(f"Temperatura promedio: {suma_temp / cantidad:.2f} C")
        print(f"Humedad relativa promedio: {suma_humedad / cantidad:.2f}%")
        print(f"Precipitacion promedio mensual: {suma_precipitacion / cantidad:.2f} mm")
        print(f"Velocidad del viento promedio: {suma_viento / cantidad:.2f} km/h")

    def mostrar_anios_extremos(self, registros_mensuales):
<<<<<<< HEAD
        """Agrupa los registros mensuales por año y determina el año mas caluroso, el mas
fresco, el de mayor precipitacion acumulada y el de mayor humedad relativa.
Parametros:
registros_mensuales (list): lista de objetos RegistroMensual del periodo consultado."""
=======
        """agrupa los registros mensuales por año y determina el año mas caluroso, fresco, humedo y con mayor precipitacion
        parametros:
        lista de objetos RegistroMensual del periodo consultado"""
>>>>>>> 5f029cc04b4426caa0ed0d2d56f183ec66b6ae95

        datos_por_anio = {}
        for registro in registros_mensuales:
            if registro.anio not in datos_por_anio:
                datos_por_anio[registro.anio] = []
            datos_por_anio[registro.anio].append(registro)

        anio_mas_caluroso = None
        temp_mas_alta = None
        anio_mas_fresco = None
        temp_mas_baja = None
        anio_mas_lluvioso = None
        precipitacion_mas_alta = None
        anio_mas_humedo = None
        humedad_mas_alta = None

        for anio in datos_por_anio:
            registros_del_anio = datos_por_anio[anio]

            suma_temp = 0
            suma_humedad = 0
            suma_precipitacion = 0 

            for registro in registros_del_anio:
                suma_temp += registro.temperatura
                suma_humedad += registro.humedad
                suma_precipitacion += registro.precipitacion

            promedio_temp_anio = suma_temp / len(registros_del_anio)
            promedio_humedad_anio = suma_humedad / len(registros_del_anio)

            if temp_mas_alta is None or promedio_temp_anio > temp_mas_alta:
                temp_mas_alta = promedio_temp_anio
                anio_mas_caluroso = anio

            if temp_mas_baja is None or promedio_temp_anio < temp_mas_baja:
                temp_mas_baja = promedio_temp_anio
                anio_mas_fresco = anio

            if precipitacion_mas_alta is None or suma_precipitacion > precipitacion_mas_alta:
                precipitacion_mas_alta = suma_precipitacion
                anio_mas_lluvioso = anio

            if humedad_mas_alta is None or promedio_humedad_anio > humedad_mas_alta:
                humedad_mas_alta = promedio_humedad_anio
                anio_mas_humedo = anio

        print("\n===Años destacados del periodo===")
        print(f"Año mas caluroso: {anio_mas_caluroso} ({temp_mas_alta:.2f} C promedio)")
        print(f"Año mas fresco: {anio_mas_fresco} ({temp_mas_baja:.2f} C promedio)")
        print(f"Año con mayor precipitacion: {anio_mas_lluvioso} ({precipitacion_mas_alta:.2f} mm acumulados)")
        print(f"Año con mayor humedad: {anio_mas_humedo} ({humedad_mas_alta:.2f}% promedio)")



      



    

        