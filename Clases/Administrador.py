from Clases.EmpresasDeTrasporte import EmpresasDeTransporte
from Clases.Persona import Persona


class Administrador (Persona):
    Empresas:EmpresasDeTransporte[5]

    def __init__(self,empresa:EmpresasDeTransporte[5]):
        Empresas=empresa
    
    def Administrar (self,Empresas:EmpresasDeTransporte[5]):
        pass

