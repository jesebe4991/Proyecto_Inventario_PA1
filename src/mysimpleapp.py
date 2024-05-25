import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SOP INVENTARIOS")
root.minsize(width=600, height=400)

label = tk.Label(root, text="SISTEMA DE INVENTARIOS")
label.pack()

separador = tk.Frame(root, height=20) 
separador.pack()

columnas = ["Categoría", "Producto"]

tabla = ttk.Treeview(root, columns=columnas, show="headings")
tabla.heading("Categoría", text="Categoría")
tabla.heading("Producto", text="Producto")
tabla.pack()

# Ejemplo de inserción de datos
tabla.insert("", tk.END, values=("Electrodomésticos", "Nevera", "Lavadora"))
tabla.insert("", tk.END, values=("Tecnología", "Smartphone", "Tablet"))
tabla.insert("", tk.END, values=("Muebles", "Mesa", "Silla"))

def agregar_categoria():
    # Código para agregar una nueva categoría de producto
    pass

separador = tk.Frame(root, height=20) 
separador.pack()
button = tk.Button(root, text="Agregar Producto", command=lambda: print("Producto agregado"))

entrada_nombre = tk.Entry(root)
entrada_nombre.pack()


separador = tk.Frame(root, height=20) 
separador.pack()

boton_categoria = tk.Button(root, text="Agregar Categoría", command=agregar_categoria)
boton_categoria.pack(side=tk.LEFT)

separador = tk.Frame(root, height=20) 
separador.pack()
entrada_nombre = tk.Entry(root)
entrada_nombre.pack()
button.pack(side=tk.RIGHT)

root.mainloop()