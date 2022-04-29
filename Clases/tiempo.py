from ProyectoPOO.Clases.Ruta import Ruta
from ProyectoPOO.Clases.Vehiculo import Vehiculo


class Tiempo ():
    HoraSalida: float
    HoraLlegada:float
    Vehiculos: Vehiculo[6]
    Rutas: Ruta[6]
    def __init__(self,vehiculos,rutas):
        Vehiculo=vehiculos 
        Ruta=rutas