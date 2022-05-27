from Clases.Conductor import Conductor
from Clases.Ruta import Ruta
from Clases.contacto import Contacto
from Clases.novedad import Novedad


class EmpresasDeTransporte ():
    Nombre:str
    ContactosEmpresa:Contacto[2]
    Actividad:bool
    Tarifa:float
    RutasEmpresas:Ruta[3]
    Notificaciones:Novedad[2]
    Conductores:Conductor[2]

    def __init__(self,rutas:Ruta[3],contactos:Contacto[2]):
        RutaEmpresas=rutas
        ContactosEmpresa=contactos
    def CrearEmpresa (self,Nombre:str):
        pass
    def EliminarEmpresa (self,Nombre:str):
        pass
    def ModificarEmpresa (self,Nombre:str):
        pass
    def MostrarTarifa (self,Tarifa:float):
        pass
    def CalculaTarifa (self,Tarifa:float):
        pass
    def MostrarEstado (self,Actividad:bool):
        pass
    def RecibirNotificaciones (self,Notificacion:Novedad[5]):
        pass
