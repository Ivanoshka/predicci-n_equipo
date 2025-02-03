import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.title("Interfaz con Listas Desplegables")
root.geometry("400x200")

# Etiqueta y primera lista desplegable
ttk.Label(root, text="Selecciona una opción:").pack(pady=5)
opciones1 = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
combo1 = ttk.Combobox(root, values=opciones1, state="readonly")
combo1.pack(pady=5)
combo1.current(0)  # Selecciona la primera opción por defecto

# Etiqueta y segunda lista desplegable
ttk.Label(root, text="Selecciona otra opción:").pack(pady=5)
opciones2 = ["Valor A", "Valor B", "Valor C", "Valor D"]
combo2 = ttk.Combobox(root, values=opciones2, state="readonly")
combo2.pack(pady=5)
combo2.current(0)  # Selecciona la primera opción por defecto

# Botón para mostrar selección
def mostrar_seleccion():
    seleccion1 = combo1.get()
    seleccion2 = combo2.get()
    label_resultado.config(text=f"Seleccionaste: {seleccion1} y {seleccion2}")

ttk.Button(root, text="Mostrar Selección", command=mostrar_seleccion).pack(pady=10)

# Etiqueta para mostrar la selección
label_resultado = ttk.Label(root, text="Selecciona opciones y presiona el botón")
label_resultado.pack(pady=5)

# Ejecutar aplicación
root.mainloop()
