

class Modelo:
    def __init__(self):
        self.parrafos = []
        self.indice_parrafo_actual = 0

    def cargar_documento(self, ruta_archivo):
        with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
            self.parrafos = archivo.readlines()
        self.indice_parrafo_actual = 0

    def avanzar_parrafo(self):
        if self.indice_parrafo_actual < len(self.parrafos) - 1:
            self.indice_parrafo_actual += 1

    def retroceder_parrafo(self):
        if self.indice_parrafo_actual > 0:
            self.indice_parrafo_actual -= 1
