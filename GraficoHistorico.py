import matplotlib.pyplot as plt

def graficar_evolucion_anual(registros_mensuales):
    """genera un grafico con 4 paneles que comparan año por año, la evolucion de la temperatura, humedad, precipitacion y el viento dentro del periodo consultado
    parametros:
    lista de objetos RegistroMensual del periodo consultado
    """

    datos_por_anio = {}

    for registro in registros_mensuales:
        if registro.anio not in datos_por_anio:
            datos_por_anio[registro.anio] = {
                "temperaturas": [],
                "humedades": [],
                "vientos": [],
                "precipitaciones": [],
            }

        datos_por_anio[registro.anio]["temperaturas"].append(registro.temperatura)
        datos_por_anio[registro.anio]["humedades"].append(registro.humedad)
        datos_por_anio[registro.anio]["vientos"].append(registro.viento)
        datos_por_anio[registro.anio]["precipitaciones"].append(registro.precipitacion)

    anios = sorted(datos_por_anio.keys())

    promedio_temp_anual = []
    promedio_humedad_anual = []
    promedio_viento_anual = []
    suma_precipitacion_anual = []

    for anio in anios:
        valores = datos_por_anio[anio]
        promedio_temp_anual.append(sum(valores["temperaturas"]) / len(valores["temperaturas"]))
        promedio_humedad_anual.append(sum(valores["humedades"]) / len(valores["humedades"]))
        promedio_viento_anual.append(sum(valores["vientos"]) / len(valores["vientos"]))
        suma_precipitacion_anual.append(sum(valores["precipitaciones"]))

    figura, graficos = plt.subplots(2,2, figsize=(10,7))

    graficos[0][0].plot(anios, promedio_temp_anual, marker="o", color = "tab:red")
    graficos[0][0].set_title("Temperatura promedio por año")
    graficos[0][0].set_xlabel("Año ")
    graficos[0][0].set_ylabel("°C")

    graficos[0][1].plot(anios, promedio_humedad_anual, marker = "o", color = "tab:blue")
    graficos[0][1].set_title("Humedad relativa promedio por año")
    graficos[0][1].set_xlabel("Año")
    graficos[0][1].set_ylabel("%")

    graficos[1][0].plot(anios, suma_precipitacion_anual, marker = "o", color = "tab:green")
    graficos[1][0].set_title("Precipitacion acumulada por año")
    graficos[1][0].set_xlabel("Año")
    graficos[1][0].set_ylabel("mm")

    graficos[1][1].plot(anios, promedio_viento_anual, marker = "o", color = "tab:orange")
    graficos[1][1].set_title("Velocidad promedio del viento por año")
    graficos[1][1].set_xlabel("Año")
    graficos[1][1].set_ylabel("km/h")

    figura.suptitle("Evolución del clima por año")
    figura.tight_layout()
    plt.show()

        




