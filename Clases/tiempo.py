from ProyectoPOO.Clases.Ruta import Ruta
from ProyectoPOO.Clases.vehiculo import Vehiculos


class Tiempo ():
    HoraSalida: float
    HoraLlegada:float
    Vehiculo: Vehiculos[6]
    Rutas: Ruta[6]
    def __init__(self,vehiculo:Vehiculos[6],rutas:Ruta[6]):
        TiempoVehiculos=vehiculo
        TiempoRuta=rutas 

    def IngresarTiempo (self,HoraSalida:int,HoraLlegada:int):
        pass
    def CalcularTiempo (self,HoraSalida:int,HoraLlegada:int):
        pass
    def CalcularPromedioTiempo (self,HoraSalida:int,HoraLlegada:int):
        pass
    def EnviarPromedioTiempo (self,HoraSalida:int,HoraLlegada:int):
        pass
    def MostrarPromedioTiempo (self,HoraSalida:int,HoraLlegada:int):
        pass
    def ModificarPromedioTiempo (self,HoraSalida:int,HoraLlegada:int):
        pass
    def ModificarTiempoRuta (self,Ruta:Ruta[6],Vehiculo:Vehiculos[6],HoraSalida:int,HoraLlegada:int):
        pass
    def EliminarTiempoRuta (self,Ruta:Ruta[6],Vehiculo:Vehiculos[6],HoraSalida:int,HoraLlegada:int):
        pass
    def MostrarTiempoRuta (self,Ruta:Ruta[6],Vehiculo:Vehiculos[6],HoraSalida:int,HoraLlegada:int):
        pass
    def CrearTiempoRuta (self,Ruta:Ruta[6],Vehiculo:Vehiculos[6],HoraSalida:int,HoraLlegada:int):
        pass