import requests
from RegistroMensual import RegistroMensual



def consultar_historico(latitud, longitud, fecha_inicio, fecha_fin):
    """consulta la API historica de open-meteo para una coordenada y rango de fechas, y agrupa los resultados diarios en una lista de objetos RegistroMensual, uno por mes.
    parametros:
    latitud de la localidad (float)
    longitud de la localidad (float)
    fecha de inicio en formato AAAA-MM-DD
    fecha de fin en formato AAAA-MM-DD
    
    devuelve una lista de objetos RegistroMensual ordenados cronologicamente, o None si paso algun tipo de error"""
    url = "https://archive-api.open-meteo.com/v1/archive"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "start_date": fecha_inicio,
        "end_date": fecha_fin,
        "daily": "temperature_2m_mean,relative_humidity_2m_mean,wind_speed_10m_mean,precipitation_sum",
        "timezone": "America/Caracas",
    }

    try:
        respuesta = requests.get(url, params=parametros, timeout = 15)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException:
        print("No se pudo conectar con la API historica de Open-Meteo. Verifique su conexion a internet.")
        return None

    datos = respuesta.json()

    if "daily" not in datos:
        print("La API no devolvio datos historicos para el periodo indicado.")
        return None

    return agrupar_por_mes(datos["daily"])


def agrupar_por_mes(diario):
    """agrupa los datos diarios que entrega la API en una lista de objetos RegistroMensual, calcula el promedio mensual de la temperatura, humedad y viento, y la suma mensual de la precipitacion
    parametros:
    diccionario "daily" como lo devuelve la APi con listas de fechas y valores
    
    devuelve una lista de objetos de RegistroMensual, uno por cada mes presente en los datos ordenados cronologicamente"""

    grupos = {}

    for indice, fecha in enumerate(diario["time"]):
        anio_mes = fecha[:7]

        if anio_mes not in grupos:
            grupos[anio_mes] = {
                "temperaturas": [],
                "humedades": [],
                "vientos": [],
                "precipitaciones": [],
            }

        grupos[anio_mes]["temperaturas"].append(diario["temperature_2m_mean"][indice])
        grupos[anio_mes]["humedades"].append(diario["relative_humidity_2m_mean"][indice])
        grupos[anio_mes]["vientos"].append(diario["wind_speed_10m_mean"][indice])
        grupos[anio_mes]["precipitaciones"].append(diario["precipitation_sum"][indice])

    registros_mensuales = []
    for anio_mes in sorted(grupos.keys()):
        valores = grupos[anio_mes]
        anio = int(anio_mes[:4])
        mes = int(anio_mes[5:7])

        promedio_temp = sum(valores["temperaturas"]) / len(valores["temperaturas"])
        promedio_humedad = sum(valores["humedades"]) / len(valores["humedades"])
        promedio_viento = sum(valores["vientos"]) / len(valores["vientos"])
        suma_precipitacion = sum(valores["precipitaciones"])

        registro = RegistroMensual(anio, mes, promedio_temp, promedio_humedad, suma_precipitacion, promedio_viento)
        registros_mensuales.append(registro)

    return registros_mensuales






    

