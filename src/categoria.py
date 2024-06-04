class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        # self.descripcion = descripcion

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)