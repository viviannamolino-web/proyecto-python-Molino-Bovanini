class Municipio:

    def __init__(self, nombre):
        self.nombre=nombre
        self.localidades=[]

    def agregar_localidad (self,localidad):
        self.localidades.append(localidad)

    def obtener_total_localidades(self):
        return len(self.localidades)

    def obtener_con_coordenadas(self):
        return [loc for loc in self.localidades if loc.tiene_coordenadas()]

    def obtener_sin_coordenadas(self):
        return[loc for loc in self.localidades if not loc.tiene_coordenadas()]

    def porcentaje_con_coordenadas(self):
        total=self.obtener_total_localidades()
        if total==0:
            return 0.0
        return (len(self.obtener_con_coordenadas())/total)*100
    


