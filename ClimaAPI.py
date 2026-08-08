import requests
from Clima import Clima

url = "https://api.open-meteo.com/v1/forecast"

parametros={
    "latitude": latitud,
    "longitude": longitud,
    "current":
    "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
}

try:
    respuesta=requests.get(url,params=parametros,timeout=10)
    respuesta.raise_for_status()
except requests.exceptions.RequestException:
    print("No se pudo conectar con la API de Open-Meteo. Verifique su conexion a internet.")
    return None

datos = respuesta.json()
actual = datos["current"]

return Clima(
    actual["temperature_2m"],
    actual["relative_humidity_2m"],
    actual["wind_speed_10m"],
    actual["weather_code"],
    actual["time"],
)

