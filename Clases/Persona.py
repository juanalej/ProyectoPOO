from Clases.novedad import Novedad


class Persona ():
    Nombre:str
    Correo:str
    Notificacion:Novedad[2]

    def __init__ (self,notificacion):
        Novedad=notificacion