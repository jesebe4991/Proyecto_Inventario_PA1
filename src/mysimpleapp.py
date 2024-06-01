import tkinter as tk
from tkinter import ttk

def agregar_producto():
    # Código para agregar un nuevo producto
    pass

def eliminar_producto():
    # Código para eliminar un producto
    pass

def agregar_categoria():
    # Código para agregar una nueva categoría
    pass

def eliminar_categoria():
    # Código para eliminar una categoría
    pass

def agregar_stock():
    # Código para agregar stock
    pass

def eliminar_stock():
    # Código para eliminar stock
    pass

root = tk.Tk()
root.title("SOP INVENTARIOS")
root.minsize(width=600, height=400)

# Sección de Tabla Informativa
tabla_frame = tk.Frame(root)
tabla_frame.pack(pady=10)

columnas = ["Producto", "Categoría", "Stock", "Proveedor"]
tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
for columna in columnas:
    tabla.heading(columna, text=columna)

# Ejemplo de inserción de datos
tabla.insert("", tk.END, values=("Nevera", "Electrodomésticos", 10, "Proveedor 1"))
tabla.insert("", tk.END, values=("Smartphone", "Tecnología", 20, "Proveedor 2"))
tabla.insert("", tk.END, values=("Mesa", "Muebles", 15, "Proveedor 3"))

tabla.pack()

# Sección de Inputs y Botones
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Inputs
input_producto = tk.Entry(input_frame)
input_producto.grid(row=0, column=0, padx=5, pady=5)
input_categoria = tk.Entry(input_frame)
input_categoria.grid(row=0, column=1, padx=5, pady=5)
input_stock = tk.Entry(input_frame)
input_stock.grid(row=0, column=2, padx=5, pady=5)

# Botones
boton_frame = tk.Frame(root)
boton_frame.pack(pady=10)

boton_agregar_producto = tk.Button(boton_frame, text="Agregar Producto", command=agregar_producto)
boton_agregar_producto.grid(row=0, column=0, padx=5, pady=5)
boton_eliminar_producto = tk.Button(boton_frame, text="Eliminar Producto", command=eliminar_producto)
boton_eliminar_producto.grid(row=1, column=0, padx=5, pady=5)

boton_agregar_categoria = tk.Button(boton_frame, text="Agregar Categoría", command=agregar_categoria)
boton_agregar_categoria.grid(row=0, column=1, padx=5, pady=5)
boton_eliminar_categoria = tk.Button(boton_frame, text="Eliminar Categoría", command=eliminar_categoria)
boton_eliminar_categoria.grid(row=1, column=1, padx=5, pady=5)

boton_agregar_stock = tk.Button(boton_frame, text="Agregar Stock", command=agregar_stock)
boton_agregar_stock.grid(row=0, column=2, padx=5, pady=5)
boton_eliminar_stock = tk.Button(boton_frame, text="Eliminar Stock", command=eliminar_stock)
boton_eliminar_stock.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
