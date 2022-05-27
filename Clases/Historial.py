from Clases.Ruta import Ruta
from Clases.tiempo import Tiempo


class Historial ():
    RutasVehiculo:Ruta[2]
    TiempoRuta:Tiempo

    def __init__ (self,rutas:Ruta[2],tiempo:Tiempo):
        RutasVehiculos=rutas
        TiempoRuta=tiempo
    def Listar (RutasVehiculo:Ruta[2],TiempoRuta:Tiempo):
        pass
    def AgregarHistorial (RutasVehiculo:Ruta[2],TiempoRuta:Tiempo):
        pass
    def VaciarHistorial (RutasVehiculo:Ruta[2],TiempoRuta:Tiempo):
        pass
        