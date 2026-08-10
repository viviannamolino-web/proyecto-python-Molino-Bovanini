import json
from Municipio import Municipio
from Localidad import Localidad
from Sistema import Sistema

def main():
    """Punto de entrada del programa MeteoCaracas."""

    sistema = Sistema("zonas_caracas.json")
    sistema.start()


main()




