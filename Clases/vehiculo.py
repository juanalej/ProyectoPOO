from tempfile import TemporaryDirectory
from Clases.Historial import Historial
from Clases.novedad import Novedad
from ProyectoPOO.Clases.Conductor import Conductor
from ProyectoPOO.Clases.EmpresasDeTrasporte import EmpresasDeTransporte
from ProyectoPOO.Clases.Ruta import Ruta
from ProyectoPOO.Clases.Multas import Multas
from ProyectoPOO.Clases.Tiempo import Tiempo



class Vehiculos ():
    Lateral:str
    Placa:str
    Actividad: bool
    RutasVehiculo: Ruta[7]
    Empresas:EmpresasDeTransporte[4]
    ConductoresVehiculo:Conductor[8]
    MultasVehiculo: Multas[5]
    HistorialesVehiculo:Historial[5]
    NovedadesVehiculo:Novedad[5]
    def __init__(self,empresas:EmpresasDeTransporte[4]):
        EmpresasTransporte= empresas

    def CrearVehiculo (self,Lateral:str,Placa:str):
        pass
    def EliminarVehiculo (self,Lateral:str, Placa:str):
        pass
    def ModificarVehiculo (self,Lateral:str, Placa:str):
        pass
    def ModificarConductor (self,ConductorVehiculo:Conductor[4]):
        pass
    def MostrarConductor (self,ConductorVehiculo:Conductor[4]):
        pass
    def MostrarRuta (self,RutaVehiculo:Ruta):
        pass
    def MostrarTiempo (self,TiempoVehiculo:Tiempo):
        pass
          
