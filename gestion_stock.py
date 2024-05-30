def agregar_stock(producto, cantidad):
    producto.stock_inicial += cantidad

def retirar_stock(producto, cantidad):
    if producto.stock_inicial >= cantidad:
        producto.stock_inicial -= cantidad
    else:
        print("No hay suficiente stock.")

def calcular_valor_total_stock():
    return sum([producto.precio * producto.stock_inicial for producto in Productos])
