def agregar_producto_categoria(categoria, producto):
    categoria.productos.append(producto)

def eliminar_producto_categoria(categoria, producto):
    categoria.productos.remove(producto)

def agregar_producto_proveedor(proveedor, producto):
    proveedor.productos_suministrados.append(producto)

def eliminar_producto_proveedor(proveedor, producto):
    proveedor.productos_suministrados.remove(producto)

def agregar_producto_bodega(bodega, producto):
    if len(bodega.productos_almacenados) < bodega.capacidad_maxima:
        bodega.productos_almacenados.append(producto)
    else:
        print("La bodega está llena.")

#definción de la clase producto Bodega 3

def retirar_producto_bodega(bodega, producto, cantidad):
    if producto in bodega.productos_almacenados:
        if bodega.productos_almacenados.count(producto) >= cantidad:
            bodega.productos_almacenados.remove(producto)
        else:
            print("No hay suficiente stock en la bodega.")
    else:
        print("El producto no está en la bodega.")
