import tkinter as tk
from tkinter import ttk
from categoria import Categoria
from producto import Producto
from proveedor import Proveedor
from bodega import Bodega

# Inicializar listas para las entidades
categorias = []
productos = []
proveedores = []
bodegas = []

# Crear una bodega por defecto
bodega_central = Bodega("Bodega Central", "Carrera 15 # 70-80", 1000)
bodegas.append(bodega_central)

def agregar_producto():
    nombre = input_producto.get()
    categoria_nombre = input_categoria.get()
    stock = int(input_stock.get())
    # Busca la categoría
    categoria = next((c for c in categorias if c.nombre == categoria_nombre), None)
    if categoria:
        producto = Producto(nombre, "", 0, stock, categoria)  # Descripción y precio por defecto
        productos.append(producto)
        bodega_central.agregar_producto(producto)
        actualizar_tabla()
    else:
        print("Categoría no encontrada")

def eliminar_producto():
    nombre = input_producto.get()
    producto = next((p for p in productos if p.nombre == nombre), None)
    if producto:
        productos.remove(producto)
        bodega_central.retirar_producto(producto)
        actualizar_tabla()
    else:
        print("Producto no encontrado")

def agregar_categoria():
    nombre = input_categoria.get()
    categoria = Categoria(nombre, "")
    categorias.append(categoria)
    actualizar_tabla()

def eliminar_categoria():
    nombre = input_categoria.get()
    categoria = next((c for c in categorias if c.nombre == nombre), None)
    if categoria:
        categorias.remove(categoria)
        actualizar_tabla()
    else:
        print("Categoría no encontrada")

def agregar_stock():
    nombre = input_producto.get()
    stock = int(input_stock.get())
    producto = next((p for p in productos if p.nombre == nombre), None)
    if producto:
        producto.stok_inicial += stock
        actualizar_tabla()
    else:
        print("Producto no encontrado")

def eliminar_stock():
    nombre = input_producto.get()
    stock = int(input_stock.get())
    producto = next((p for p in productos if p.nombre == nombre), None)
    if producto:
        if producto.stok_inicial >= stock:
            producto.stok_inicial -= stock
        else:
            print("No hay suficiente stock para eliminar")
        actualizar_tabla()
    else:
        print("Producto no encontrado")

def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    for producto in productos:
        tabla.insert("", tk.END, values=(producto.nombre, producto.categoria.nombre, producto.stok_inicial, "Proveedor"))

root = tk.Tk()
root.title("SOP INVENTARIOS")
root.minsize(width=700, height=400)

# Sección de Tabla Informativa
tabla_frame = tk.Frame(root)
tabla_frame.pack(pady=10)

columnas = ["Producto", "Categoría", "Stock", "Proveedor"]
tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
for columna in columnas:
    tabla.heading(columna, text=columna)

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
