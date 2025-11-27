import tkinter as tk
import random
from tkinter import messagebox

from cases.Personaje import Personaje
from cases.guerrero import Guerrero
from cases.mago import Mago

personajeGuerrero = Guerrero("canvas", "Juan", 5, 7)
print(personajeGuerrero.realizar_accion())
personajeMago = Mago("canvas", "Carlos", 2,1)
print(personajeMago.realizar_accion())
personajePrueba = Personaje("canvas", "Pepe", 3, 4)
print(personajePrueba.realizar_accion())

#Creamos la interfaz gráfica usando la librería tkinter
ventana = tk.Tk()
#A la ventana le ponemos el título
ventana.title("Juego de personajes con POO")
#Le damos un tamaño
ventana.geometry("800x600")
#
frameControl = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frameControl.pack(fill=tk.X)
tk.Label(frameControl, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
inputName = (tk.Entry(frameControl))
inputName.pack(side=tk.LEFT, padx=5)
#Creamos una variable tipo canvas para poder dibujar sobre ella
escenario_canvas = tk.Canvas(ventana, width=800, height=500, bg="#2c3e50")
escenario_canvas.pack(fill=tk.BOTH, expand=True) # expand=True permite que crezca si la ventana cambia de tamaño

def obtener_posicion_random(self):
    """Genera coordenadas aleatorias dentro del canvas."""
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    return x, y

def crear_guerrero(self):
    nombre = inputName.get() or "Guerrero Anónimo"
    x, y = self.obtener_posicion_random(ventana)

    # INSTANCIACIÓN: Aquí nace el objeto
    nuevo_guerrero = Guerrero(self.canvas, nombre, x, y)
    nuevo_guerrero.dibujar()

def crear_mago(self):
    nombre = self.entry_nombre.get() or "Mago Anónimo"
    x, y = self.obtener_posicion_random(ventana)

    # INSTANCIACIÓN: Aquí nace el objeto
    nuevo_mago = Mago(self.canvas, nombre, x, y)
    nuevo_mago.dibujar()

    self.lista_objetos.append(nuevo_mago)
    self.log_label.config(text=f"Se ha instanciado un objeto Clase Mago: {nombre}")

def todos_actuan(self):
    """Demostración de Polimorfismo: Iteramos la lista y todos responden distinto."""
    if not self.lista_objetos:
        messagebox.showinfo("Info", "¡Primero crea algunos personajes!")
        return

    logs = []
    for personaje in self.lista_objetos:
        # Llamamos al MISMO método, pero cada uno hace algo distinto
        logs.append(personaje.realizar_accion())

    mensaje_final = " | ".join(logs)
    self.log_label.config(text=mensaje_final)

tk.Button(frameControl, text="Crear Guerrero", bg="#e74c3c", fg="white",
    command=crear_guerrero).pack(side=tk.LEFT, padx=5)

tk.Button(frameControl, text="Crear Mago", bg="#3498db", fg="white",
    command=crear_mago).pack(side=tk.LEFT, padx=5)

tk.Button(frameControl, text="¡TODOS ACTUAR!", bg="#2c3e50", fg="white",
    command=todos_actuan).pack(side=tk.RIGHT, padx=10)

#Para que no se cierre la ventana
ventana.mainloop()