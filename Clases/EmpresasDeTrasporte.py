from Clases.Conductor import Conductor
from Clases.Ruta import Ruta


class EmpresasDeTransporte ():
    Nombre:str
    Contactos:Contacto[2]
    Actividad:bool
    Tarifa:float
    RutaEmpresa:Ruta[3]
    Notificacion:Novedad[2]
    Conductores:Conductor[2]

    def __init__(self,rutaEmpresa,conductores,notificacion,contactos):
        Ruta=rutaEmpresa
        Conductor=conductores
        Novedad=notificacion
        Contacto=contactos
