from tempfile import TemporaryDirectory
from Clases.Historial import Historial
from Clases.novedad import Novedad
from ProyectoPOO.Clases.Conductor import Conductor
from ProyectoPOO.Clases.EmpresasDeTrasporte import EmpresasDeTransporte
from ProyectoPOO.Clases.Ruta import Ruta
from ProyectoPOO.Clases.Multas import Multas



class Vehiculo ():
    Lateral:str
    Placa:str
    Actividad: bool
    RutaVehiculo: Ruta[7]
    Empresa:EmpresasDeTransporte
    ConductorVehiculo:Conductor[8]
    MultaVehiculo: Multas[5]
    HistorialVehiculo:Historial[5]
    NovedadVehiculo:Novedad[5]
    def __init__(self,empresa):
        EmpresaDeTransporte= empresa
         
