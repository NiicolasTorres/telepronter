

# vista.py

from tkinter import *
from tkinter import filedialog

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.raiz = Tk()
        self.raiz.title("Teleprompter")
        self.raiz.geometry("800x600")
        self.raiz.config(bg="black")

        self.btn_cargar = Button(self.raiz, text="Cargar documento", command=self.cargar_documento)
        self.btn_cargar.pack(side=TOP)

        self.btn_retroceder = Button(self.raiz, text="Retroceder", command=self.retroceder_parrafo)
        self.btn_retroceder.pack(side=LEFT)

        self.btn_avanzar = Button(self.raiz, text="Avanzar", command=self.avanzar_parrafo)
        self.btn_avanzar.pack(side=RIGHT)

        self.texto_telepronter = Text(self.raiz, wrap=WORD, font=("Arial", 24))
        self.texto_telepronter.pack(expand=True, fill=BOTH)

        self.avance_automatico_activado = False

    def cargar_documento(self):
        ruta_archivo = filedialog.askopenfilename()
        try:
            self.controlador.modelo.cargar_documento(ruta_archivo)
            self.actualizar_telepronter()
            if not self.avance_automatico_activado:
                self.iniciar_avance_automatico()
        except FileNotFoundError:
            self.mostrar_error("¡Error: archivo no encontrado!")
        except Exception as e:
            self.mostrar_error(f"¡Error inesperado: {e}")

    def actualizar_telepronter(self):
        self.texto_telepronter.config(font=("Arial", 24))
        self.mostrar_parrafo()

    def mostrar_parrafo(self):
        self.texto_telepronter.delete('1.0', END)
        self.texto_telepronter.insert(END, self.controlador.modelo.parrafos[self.controlador.modelo.indice_parrafo_actual])

    def avanzar_parrafo(self):
        self.controlador.modelo.avanzar_parrafo()
        self.mostrar_parrafo()

    def retroceder_parrafo(self):
        self.controlador.modelo.retroceder_parrafo()
        self.mostrar_parrafo()

    def mostrar_error(self, mensaje):
        self.texto_telepronter.delete('1.0', END)
        self.texto_telepronter.insert(END, mensaje)

    def iniciar_avance_automatico(self):
        self.avance_automatico_activado = True
        self.avanzar_automaticamente()

    def detener_avance_automatico(self):
        self.avance_automatico_activado = False

    def avanzar_automaticamente(self):
        if self.avance_automatico_activado:
            self.avanzar_parrafo()  
            self.raiz.after(7000, self.avanzar_automaticamente)  

    def ejecutar(self):
        self.raiz.mainloop()
