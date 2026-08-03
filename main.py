import json
from Municipio import Municipio
from Localidad import Localidad
from Sistema import Sistema

def main():

    sistema = Sistema("zonas_caracas.json")
    sistema.start()


main()




