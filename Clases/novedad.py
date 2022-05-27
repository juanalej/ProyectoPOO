from xmlrpc.client import boolean
from ProyectoPOO.Clases.Ruta import Ruta


class Novedad ():
    RutaPrincipal: Ruta[4]
    RutaAlterna: Ruta[4]
    RetrazoEnLaRuta: bool
    def __init__ (self,rutaPrincipal,rutaAlterna):
        Ruta=rutaPrincipal
        Ruta=rutaAlterna
    def CrearNovedades (self,RutaPrincipal:Ruta[4],RutaAlterna:Ruta[4]):
        pass
    def EliminarNovedades (self,RutaPrincipal:Ruta[4],RutaAlterna:Ruta[4]):
        pass
    def ModificarNovedades (self,RutaPrincipal:Ruta[4],RutaAlterna:Ruta[4]):
        pass
    def EnviarNovedades (self,ReatrazoEnLaRuta:bool,RutaPrincipal:Ruta[4],RutaAlterna:Ruta[4]):
        pass