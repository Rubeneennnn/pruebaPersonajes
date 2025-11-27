import tkinter as tk
import random
from tkinter import messagebox

from cases.Personaje import Personaje
from cases.guerrero import Guerrero
from cases.mago import Mago

# Lista donde guardaremos los personajes
lista_objetos = []

# Creamos la interfaz gráfica usando tkinter
ventana = tk.Tk()
ventana.title("Juego de personajes con POO")
ventana.geometry("800x600")

frameControl = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frameControl.pack(fill=tk.X)

tk.Label(frameControl, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
inputName = tk.Entry(frameControl)
inputName.pack(side=tk.LEFT, padx=5)

escenario_canvas = tk.Canvas(ventana, width=800, height=500, bg="#2c3e50")
escenario_canvas.pack(fill=tk.BOTH, expand=True)


# ------------------------
# FUNCIONES CORREGIDAS
# ------------------------

def obtener_posicion_random():
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    return x, y


def crear_guerrero():
    nombre = inputName.get() or "Guerrero Anónimo"
    x, y = obtener_posicion_random()

    nuevo_guerrero = Guerrero(escenario_canvas, nombre, x, y)
    nuevo_guerrero.dibujar()

    lista_objetos.append(nuevo_guerrero)


def crear_mago():
    nombre = inputName.get() or "Mago Anónimo"
    x, y = obtener_posicion_random()

    nuevo_mago = Mago(escenario_canvas, nombre, x, y)
    nuevo_mago.dibujar()

    lista_objetos.append(nuevo_mago)


def todos_actuan():
    if not lista_objetos:
        messagebox.showinfo("Info", "¡Primero crea algunos personajes!")
        return

    logs = [p.realizar_accion() for p in lista_objetos]

    messagebox.showinfo("Acciones", " | ".join(logs))


# ------------------------
# BOTONES
# ------------------------

tk.Button(frameControl, text="Crear Guerrero", bg="#e74c3c", fg="white",
          command=crear_guerrero).pack(side=tk.LEFT, padx=5)

tk.Button(frameControl, text="Crear Mago", bg="#3498db", fg="white",
          command=crear_mago).pack(side=tk.LEFT, padx=5)

tk.Button(frameControl, text="¡TODOS ACTUAR!", bg="#2c3e50", fg="white",
          command=todos_actuan).pack(side=tk.RIGHT, padx=10)


# Iniciar ventana
ventana.mainloop()