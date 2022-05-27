import pandas as pd
from Clases.Ruta import Ruta
class ArcvhivoRuta:
    RutaArchivo:Ruta[5]
    def GenerarTXT (self):
        pd.DataFrame(Ruta).to_csv('RutaArchivo.csv')
