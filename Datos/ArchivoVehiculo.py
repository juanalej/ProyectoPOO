import pandas as pd
from ProyectoPOO.Clases.vehiculo import Vehiculo
class ArchivoVehiculo:
    Vehiculos:Vehiculo[3]
    def GenerarTXT(self):
        pd.DataFrame(Vehiculo).to_csv('Vehiculos.cvs')
