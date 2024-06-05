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

# Funciones de actualización de tablas
def actualizar_tabla_categorias():
    for row in tabla_categorias.get_children():
        tabla_categorias.delete(row)
    for categoria in categorias:
        tabla_categorias.insert("", tk.END, values=(categoria.nombre))

def actualizar_tabla_productos():
    for row in tabla_productos.get_children():
        tabla_productos.delete(row)
    for producto in productos:
        tabla_productos.insert("", tk.END, values=(producto.nombre))

def actualizar_tabla_principal():
    categoria_nombre = input_categoria.get()
    for row in tabla.get_children():
        tabla.delete(row)
    for producto_tupla in bodega_central.productos_almacenados:
        producto, stock = producto_tupla 
        if producto is None:
            print("Producto no encontrado")
            continue  
        tabla.insert("", tk.END, values=(producto.nombre, categoria_nombre, stock, "Proveedor"))

# Funciones para botones
def agregar_categoria():
    nombre = input_categoria.get()
    categoria = Categoria(nombre)
    categorias.append(categoria)
    actualizar_tabla_categorias()

def eliminar_categoria():
    selected_item = tabla_categorias.selection()
    if selected_item:
        item = tabla_categorias.item(selected_item)
        categoria_nombre = item['values'][0]
        categoria = next((c for c in categorias if c.nombre == categoria_nombre), None)
        if categoria:
            categorias.remove(categoria)
            actualizar_tabla_categorias()

def agregar_producto():
    nombre = input_producto.get()
    categoria_nombre = input_categoria.get()

    # Busca la categoría
    categoria = next((c for c in categorias if c.nombre == categoria_nombre), None)
    if categoria:
        producto = Producto(nombre, categoria)
        productos.append(producto)
        actualizar_tabla_productos()
    else:
        print("Categoría no encontrada")

def eliminar_producto():
    selected_item = tabla_productos.selection()
    if selected_item:
        item = tabla_productos.item(selected_item)
        producto_nombre = item['values'][0]
        producto = next((p for p in productos if p.nombre == producto_nombre), None)
        if producto:
            productos.remove(producto)
            actualizar_tabla_productos()

def agregar_stock():
    producto_nombre = input_producto.get()
    stock = int(input_stock.get())
    producto = next((p for p in productos if p.nombre == producto_nombre), None)
    if producto:
        producto.stock += stock
        actualizar_tabla_principal()

def eliminar_stock():
    producto_nombre = input_producto.get()
    stock = int(input_stock.get())
    producto = next((p for p in productos if p.nombre == producto_nombre), None)
    if producto:
        producto.stock -= stock
        actualizar_tabla_principal()

def registrar():
    producto_nombre = input_producto.get()
    categoria_nombre = input_categoria.get()
    stock = int(input_stock.get())
    producto = next((p for p in productos if p.nombre == producto_nombre), None)
    categoria = next((c for c in categorias if c.nombre == categoria_nombre), None)
    if producto and categoria:
        bodega_central.agregar_producto(producto, stock)
        actualizar_tabla_principal()

def eliminar_registro():
    selected_item = tabla.selection()
    if selected_item:
        item = tabla.item(selected_item)
        producto_nombre = item['values'][0]

        producto_tupla = next((p for p in bodega_central.productos_almacenados if p[0].nombre == producto_nombre), None)
        if producto_tupla:
            producto = producto_tupla[0]
            bodega_central.eliminar_producto(producto)
            actualizar_tabla_principal()
        else:
            print("Producto no encontrado en la bodega central.")

def seleccionar_categoria(event):
    selected_item = tabla_categorias.selection()[0]
    categoria_nombre = tabla_categorias.item(selected_item)['values'][0]
    input_categoria.delete(0, tk.END)
    input_categoria.insert(0, categoria_nombre)

def seleccionar_producto(event):
    selected_item = tabla_productos.selection()[0]
    producto_nombre = tabla_productos.item(selected_item)['values'][0]
    input_producto.delete(0, tk.END)
    input_producto.insert(0, producto_nombre)

def seleccionar_registro(event):
    selected_item = tabla.selection()[0]
    producto_nombre = tabla.item(selected_item)['values'][0]
    input_producto.delete(0, tk.END)
    input_producto.insert(0, producto_nombre)
    input_categoria.delete(0, tk.END)
    input_categoria.insert(0, tabla.item(selected_item)['values'][1])
    input_stock.delete(0, tk.END)
    input_stock.insert(0, tabla.item(selected_item)['values'][2])

# Configuración de la ventana principal
root = tk.Tk()
root.title("SOP INVENTARIOS")
root.minsize(width=800, height=600)

tabla_frame = tk.Frame(root)
tabla_frame.pack(pady=10)

columnas = ["Producto", "Categoría", "Stock", "Proveedor"]
tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
for columna in columnas:
    tabla.heading(columna, text=columna)

tabla.pack()
tabla.bind("<ButtonRelease-1>", seleccionar_registro)

# **Sección de tablas de productos y categorías**
productos_categorias_frame = tk.Frame(root)
productos_categorias_frame.pack(pady=10)

# Tabla para listar productos
tabla_productos_frame = tk.Frame(productos_categorias_frame)
tabla_productos_frame.grid(row=0, column=0)

columnas_productos = ["Productos"]
tabla_productos = ttk.Treeview(tabla_productos_frame, columns=columnas_productos, show="headings")
for columna in columnas_productos:
    tabla_productos.heading(columna, text=columna)

tabla_productos.pack()
tabla_productos.bind("<ButtonRelease-1>", seleccionar_producto)

# Tabla para listar categorías
tabla_categorias_frame = tk.Frame(productos_categorias_frame)
tabla_categorias_frame.grid(row=0, column=1)

columnas_categorias = ["Categorias"]
tabla_categorias = ttk.Treeview(tabla_categorias_frame, columns=columnas_categorias, show="headings")
for columna in columnas_categorias:
    tabla_categorias.heading(columna, text=columna)

tabla_categorias.pack()
tabla_categorias.bind("<ButtonRelease-1>", seleccionar_categoria)
# Sección de Inputs y Botones
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Inputs y botones para categorías
categoria_frame = tk.Frame(input_frame)
categoria_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Label(categoria_frame, text="Categoría:").pack(side=tk.LEFT)
input_categoria = tk.Entry(categoria_frame)
input_categoria.pack(side=tk.LEFT)
boton_agregar_categoria = tk.Button(categoria_frame, text="Agregar Categoría", command=agregar_categoria)
boton_agregar_categoria.pack(side=tk.LEFT)
boton_eliminar_categoria = tk.Button(categoria_frame, text="Eliminar Categoría", command=eliminar_categoria)
boton_eliminar_categoria.pack(side=tk.LEFT)

# Inputs y botones para productos
producto_frame = tk.Frame(input_frame)
producto_frame.grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Label(producto_frame, text="Producto:").pack(side=tk.LEFT)
input_producto = tk.Entry(producto_frame)
input_producto.pack(side=tk.LEFT)
boton_agregar_producto = tk.Button(producto_frame, text="Agregar Producto", command=agregar_producto)
boton_agregar_producto.pack(side=tk.LEFT)
boton_eliminar_producto = tk.Button(producto_frame, text="Eliminar Producto", command=eliminar_producto)
boton_eliminar_producto.pack(side=tk.LEFT)

# Inputs y botones para stock
stock_frame = tk.Frame(input_frame)
stock_frame.grid(row=2, column=0, padx=5, pady=5, sticky="w")
tk.Label(stock_frame, text="Stock:").pack(side=tk.LEFT)
input_stock = tk.Entry(stock_frame)
input_stock.pack(side=tk.LEFT)
boton_agregar_stock = tk.Button(stock_frame, text="Agregar Stock", command=agregar_stock)
boton_agregar_stock.pack(side=tk.LEFT)
boton_eliminar_stock = tk.Button(stock_frame, text="Eliminar Stock", command=eliminar_stock)
boton_eliminar_stock.pack(side=tk.LEFT)

# Botones para registrar y eliminar registro
boton_frame = tk.Frame(input_frame)
boton_frame.grid(row=3, column=0, columnspan=4, pady=10, sticky="we")

boton_registrar = tk.Button(boton_frame, text="Registrar", command=registrar)
boton_registrar.grid(row=0, column=0, sticky="we")

boton_eliminar_registro = tk.Button(boton_frame, text="Eliminar Registro", command=eliminar_registro)
boton_eliminar_registro.grid(row=0, column=1, sticky="we")


root.mainloop()
