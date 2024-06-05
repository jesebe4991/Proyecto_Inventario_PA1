class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_max):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_max = capacidad_max
        self.productos_almacenados = []

    def agregar_producto(self, producto, stock):
        if len(self.productos_almacenados) < self.capacidad_max:
            self.productos_almacenados.append((producto, stock))
        else:
            print("La bodega está llena")

    def retirar_producto(self, producto):
        if producto in self.productos_almacenados:
            self.productos_almacenados.remove(producto)
        else:
            print("El producto no está en la bodega")

    def consultar_disponibilidad(self, producto):
        if producto in self.productos_almacenados:
            return True
        else:
            return False

    def calcular_valor_stock(self):
        valor_total = 0
        for producto in self.productos_almacenados:
            valor_total += producto.precio * producto.stok_inicial
        return valor_total
    
    def eliminar_producto(self, producto):
        print(self.productos_almacenados)
        for i, tupla in enumerate(self.productos_almacenados):
            if tupla[0] == producto: 
                del self.productos_almacenados[i]
                print(f"Producto {producto.nombre} eliminado de la bodega.")
                break 
        else:
            print("El producto no está en la bodega.")