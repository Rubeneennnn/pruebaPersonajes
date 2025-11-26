import tkinter as tk

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
tk.Entry(frameControl).pack

tk.Button(frameControl, text="Crear Guerrero", bg="#e74c3c", fg="white",
          command=self.crear_guerrero).pack(side=tk.LEFT, padx=5)

tk.Button(frameControl, text="Crear Mago", bg="#3498db", fg="white",
          command=self.crear_mago).pack(side=tk.LEFT, padx=5)

tk.Button(frameControl, text="¡TODOS ACTUAR!", bg="#2c3e50", fg="white",
          command=self.todos_actuan).pack(side=tk.RIGHT, padx=10)

#Para que no se cierre la ventana
ventana.mainloop()
