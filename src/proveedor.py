class Proveedor:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)