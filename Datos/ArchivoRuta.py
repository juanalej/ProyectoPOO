import pandas as pd
from Clases.Ruta import Ruta
class ArcvhivoRuta:
    RutaArchivo:Ruta[5]
    def __init__(self,rutaArchivo):
        Ruta=rutaArchivo
    def GenerarTXT (self):
        pd.DataFrame(Ruta).to_csv('RutaArchivo.csv')
