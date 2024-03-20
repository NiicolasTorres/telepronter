from tkinter import *
from tkinter import filedialog


parrafos = []

indice_parrafo_actual = 0

def cargar_documento():
    ruta_archivo = filedialog.askopenfilename()
    try:
        leer_archivo(ruta_archivo)
        actualizar_telepronter()
    except FileNotFoundError:
        mostrar_error("¡Error: archivo no encontrado!")
    except Exception as e:
        mostrar_error(f"¡Error inesperado: {e}")

def leer_archivo(ruta_archivo):
    global parrafos
    with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
        parrafos = archivo.readlines()
    global indice_parrafo_actual
    indice_parrafo_actual = 0

def actualizar_telepronter():
    texto_telepronter.config(font=("Arial", 24))
    mostrar_parrafo()

def mostrar_parrafo():
    texto_telepronter.delete('1.0', END)
    texto_telepronter.insert(END, parrafos[indice_parrafo_actual])

def avanzar_parrafo():
    global indice_parrafo_actual
    if indice_parrafo_actual < len(parrafos) - 1:
        indice_parrafo_actual += 1
        mostrar_parrafo()

def retroceder_parrafo():
    global indice_parrafo_actual
    if indice_parrafo_actual > 0:
        indice_parrafo_actual -= 1
        mostrar_parrafo()

def mostrar_error(mensaje):
    texto_telepronter.delete('1.0', END)
    texto_telepronter.insert(END, mensaje)

raiz = Tk()
raiz.title("Teleprompter")
raiz.geometry("800x600")
raiz.config(bg="black")

btn_cargar = Button(raiz, text="Cargar documento", command=cargar_documento)
btn_cargar.pack(side=TOP)

btn_retroceder = Button(raiz, text="Retroceder", command=retroceder_parrafo)
btn_retroceder.pack(side=LEFT)

btn_avanzar = Button(raiz, text="Avanzar", command=avanzar_parrafo)
btn_avanzar.pack(side=RIGHT)

texto_telepronter = Text(raiz, wrap=WORD, font=("Arial", 24))
texto_telepronter.pack(expand=True, fill=BOTH)

def avanzar_automaticamente():
    avanzar_parrafo()
    raiz.after(8000, avanzar_automaticamente)

avanzar_automaticamente()

raiz.mainloop()
