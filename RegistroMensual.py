class RegistroMensual:

    NOMBRES_MES={
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
    }

    def __init__ (self,anio,mes,temperatura,humedad,precipitacion,viento):
        self.anio=anio
        self.mes=mes
        self.temperatura=temperatura
        self.humedad=humedad
        self.precipitacion=precipitacion
        self.viento=viento

    def nombre_mes(self):
        print(f"{self.nombre_mes()} {self.anio}")
        print(f"Temperatura promedio: {self.temperatura:.2f} C")
        print(f"Humedad relativa promedio: {self.humedad:2f}%")
        print(f"Precipitacion acumulada: {self.precipitacion:2f}mm")
        print(f"Velocidad del viento promedio: {self.viento:.2f}km/h")