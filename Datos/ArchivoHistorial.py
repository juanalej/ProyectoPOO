import pandas as pd
from Clases.Historial import Historial
class ArchivoHistorial:
    HistorialArchivo:Historial[5]
    def GenerarTXT (self):
        pd.DataFrame(Historial).to_csv('HistorialArchivo.csv')