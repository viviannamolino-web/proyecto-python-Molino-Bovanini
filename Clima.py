
class Clima:

    codigos_tiempo = {
        0: "Despejado",
        1: "Mayormente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna intensa",
        56: "Llovizna helada",
        57: "Llovizna helada intensa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia intensa",
        66: "Lluvia helada",
        67: "Lluvia helada intensa",
        71: "Nieve ligera",
        73: "Nieve moderada",
        75: "Nieve intensa",
        77: "Granizo pequeño",
        80: "Chubascos ligeros",
        81: "Chubascos moderados",
        82: "Chubascos violentos",
        85: "Chubascos de nieve ligeros",
        86: "Chubascos de nieve intensos",
        95: "Tormenta electrica",
        96: "Tormenta electrica con granizo ligero",
        99: "Tormenta electrica con granizo intenso",
    }

    def __init__(self,temperatura, humedad, viento, codigo_tiempo, fecha_hora):
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.codigo_tiempo = codigo_tiempo
        self.fecha_hora = fecha_hora


    def descripcion_tiempo(self):
        return self.codigos_tiempo.get(self.codigo_tiempo, "Desconocido")


    def show(self):
        print(f"Fecha y hora de la consulta: {self.fecha_hora}")
        print(f"Temperatura actual: {self.temperatura} C")
        print(f"Humedad relativa: {self.humedad}%")
        print(f"Velocidad del viento: {self.viento} km/h")
        print(f"Estado del tiempo: {self.descripcion_tiempo()}")

