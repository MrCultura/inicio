# Datos del cliente y compra
nombre = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el producto: ")

# Conversión directa con int y float
cantidad = int(input("Ingrese la cantidad: "))
precio = float(input("Ingrese el precio unitario: "))

# Cálculo del total
subtotal = cantidad * precio
descuento = subtotal * 0.10
iva = (subtotal - descuento) * 0.16
total = subtotal - descuento + iva

# Impresión del recibo
print("=== RECIBO ===")
print("Cliente:", nombre)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario: $", precio)
print("Subtotal: $", subtotal)
print("Descuento: $", descuento)
print("IVA: $", iva)
print("Total: $", total)
print("===========================")
print("¡Gracias por su compra!")
