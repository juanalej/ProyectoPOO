import pandas as pd

from ProyectoPOO.Clases.Multas import Multas
class ArchivoMultas:
    Multa:Multas[3]
    def __init__(self,multa):
        Multas= multa
    def GenerarTXT(self):
        pd.DataFrame(Multas).to_csv('Multa.cvs')
