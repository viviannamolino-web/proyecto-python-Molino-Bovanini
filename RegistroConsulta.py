class RegistroConsulta:
    """une la localidad consultada con el resultado de Clima obtenido para las estadisticas de la sesion"""

    def __init__(self,localidad,clima):
        """inicia un registro de consulta
        parametros:
        localidad que fue consultada
        resultado de clima que fue obtenido para esa localidad"""

        self.localidad=localidad
        self.clima=clima
        