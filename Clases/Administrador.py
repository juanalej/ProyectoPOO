from Clases.EmpresasDeTrasporte import EmpresasDeTransporte
from Clases.Persona import Persona


class administrador (Persona):
    Empresas:EmpresaDeTransporte[5]

    def __init__(self,empresaDetrasporte):
        EmpresasDeTransporte=empresaDetrasporte
        self.miDato:str