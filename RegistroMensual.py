class RegistroMensual:
    """representa el resumen del clima de un mes: temperatura, humedad, precipitacion y viento"""

    NOMBRES_MES={
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
    }

    def __init__ (self,anio,mes,temperatura,humedad,precipitacion,viento):
        """inicia un registro mensual de clima
        parametros:
        año del registro 
        mes del registro (1-12)
        temperatura promedio del mes en grados celsius
        humedad relativa promedio del mes en porcentaje
        precipitacion del mes acumulada en mm
        velocidad promedio del viento del mes en km/h"""
        self.anio=anio
        self.mes=mes
        self.temperatura=temperatura
        self.humedad=humedad
        self.precipitacion=precipitacion
        self.viento=viento

    def nombre_mes(self):
        """retorna el nombre del mes en español"""

        return self.NOMBRES_MES.get(self.mes, str(self.mes))

    def show(self):
        """imprime en pantalla los datos climaticos de este mes"""

        print(f"{self.nombre_mes()} {self.anio}")
        print(f"Temperatura promedio: {self.temperatura:.2f} C")
        print(f"Humedad relativa promedio: {self.humedad:2f}%")
        print(f"Precipitacion acumulada: {self.precipitacion:2f}mm")
        print(f"Velocidad del viento promedio: {self.viento:.2f}km/h")