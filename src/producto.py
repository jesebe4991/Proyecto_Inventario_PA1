class Producto:
    def __init__(self, nombre=None,  stok_inicial=0, categoria=None):
        self.nombre = nombre
        self.stock = stok_inicial
        self.categoria = categoria