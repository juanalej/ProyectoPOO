import pandas as pd

from ProyectoPOO.Clases.Tiempo import Tiempo
class ArchivoTiempo:
    Tiempos:Tiempo[3]
    def GenerarTXT(self):
        pd.DataFrame(Tiempo).to_csv('Tiempos.cvs')