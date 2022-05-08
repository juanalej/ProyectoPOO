import pandas as pd
from Clases.EmpresasDeTrasporte import EmpresasDeTransporte
class ArchivoEmpresa:
    Empresa:EmpresasDeTransporte[5]
    def GenerarTXT(self):
        pd.DataFrame(EmpresasDeTransporte).to_csv('Empresa.csv')
