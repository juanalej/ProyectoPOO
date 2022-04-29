from Clases.Ruta import Ruta


class Historial ():
    RutaVehiculo:Ruta[2]
    TiempoRuta:Tiempo

    def __init__ (self,rutaVehiculo):
        Ruta=rutaVehiculo