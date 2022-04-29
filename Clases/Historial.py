from Clases.Ruta import Ruta
from Clases.tiempo import Tiempo


class Historial ():
    RutaVehiculo:Ruta[2]
    TiempoRuta:Tiempo

    def __init__ (self,rutaVehiculo):
        Ruta=rutaVehiculo