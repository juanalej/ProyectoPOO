from xmlrpc.client import boolean

from ProyectoPOO.Clases.Ruta import Ruta


class Novedad ():
    RutaPrincipal: Ruta
    RutaAlterna: Ruta
    RetrazoEnLaRuta: bool
    def __init__ (self,rutaPrincipal,rutaAlterna):
        Ruta=rutaPrincipal
        Ruta=rutaAlterna
