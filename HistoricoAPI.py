import requests
from RegistroMensual import RegistroMensual



def consultar_historico(latitud, longitud, fecha_inicio, fecha_fin):
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
