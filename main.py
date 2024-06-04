from categoria import Categoria
from producto import Producto
from proveedor import Proveedor
from bodega import Bodega

# Crear categorías
categoria_electronica = Categoria("Electrónica", "Productos electrónicos")
categoria_juguetes = Categoria("Juguetes", "Juguetes para niños")

# Crear productos
producto_tv = Producto("TV LED", "Smart TV de 50 pulgadas", 500000, 10, categoria_electronica)
producto_celular = Producto("Celular", "Smartphone de última generación", 1000000, 5, categoria_electronica)
producto_muneca = Producto("Muñeca", "Muñeca Barbie", 20000, 20, categoria_juguetes)
producto_carro = Producto("Carro", "Carro de juguete a control remoto", 50000, 15, categoria_juguetes)

# Crear proveedores
proveedor_tecno = Proveedor("TecnoMundo", 123456789, "Calle 10 # 20-30")
proveedor_juguetes = Proveedor("Juguetería Fantasía", 987654321, "Avenida El Dorado # 50-60")

# Crear bodegas
bodega_central = Bodega("Bodega Central", "Carrera 15 # 70-80", 1000)
bodega_norte = Bodega("Bodega Norte", "Avenida Boyacá # 100-110", 500)

# Agregar productos a las bodegas
bodega_central.agregar_producto(producto_tv)
bodega_central.agregar_producto(producto_celular)
bodega_norte.agregar_producto(producto_muneca)
bodega_norte.agregar_producto(producto_carro)

# Consultar disponibilidad de productos
if bodega_central.consultar_disponibilidad(producto_tv):
    print(f"El producto {producto_tv.nombre} está disponible en la bodega central")
else:
    print(f"El producto {producto_tv.nombre} no está disponible en la bodega central")

