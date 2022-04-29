from tempfile import TemporaryDirectory
from ProyectoPOO.Clases.Conductor import Conductor
from ProyectoPOO.Clases.EmpresasDeTrasporte import EmpresasDeTransporte
from ProyectoPOO.Clases.Ruta import Ruta
from ProyectoPOO.Clases.Multas import Multas



class Vehiculo ():
    lateral:str
    placa:str
    Actividad: bool
    RutaVehiculo: Ruta[7]
    Empresa:EmpresasDeTransporte
    ConductorVehiculo:Conductor[8]
    TiempoVehiculo: TemporaryDirectory
    MultaVehiculo: Multas
    def __init__(self,empresa):
        EmpresaDeTransporte= empresa
        
