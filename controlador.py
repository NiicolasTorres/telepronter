
from modelo import Modelo
from vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(self)

    def iniciar_aplicacion(self):
        self.vista.ejecutar()
