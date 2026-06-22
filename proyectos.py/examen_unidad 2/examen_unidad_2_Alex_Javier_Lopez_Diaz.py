print("=== Sistema de ventas ===")
NUMERO_DE_VENTAS = int(input("¿Cuántas ventas vas a registrar? "))

# Listas
nombres = []
ventas = []

# Captura de datos
for i in range(NUMERO_DE_VENTAS):
    print("\n--- Venta", i+1, "---")
    nombre = input("Nombre del vendedor: ")
    monto = float(input("Monto de la venta de " + nombre + ": $"))
    while monto <= 0:  # Validación
        print("El monto debe ser mayor a 0")
        monto = float(input("Monto de la venta de " + nombre + ": $"))
    nombres.append(nombre)
    ventas.append(monto)

# Cálculos
total_ventas = 0
total_comisiones = 0
mejor_venta = ventas[0]
mejor_nombre = nombres[0]

print("\n=== Reporte de Comisiones ===")
print("Vendedor - Monto - Comisión % - Comisión $")

for i in range(NUMERO_DE_VENTAS):
    monto = ventas[i]
    # Tabla de comisiones
    if monto < 500:
        porcentaje = 0.03
    elif monto <= 1499.99:
        porcentaje = 0.05
    elif monto <= 4999.99:
        porcentaje = 0.08
    else:
        porcentaje = 0.12

    comision = monto * porcentaje
    print(nombres[i], "----", "$", monto, "----", int(porcentaje*100), "%", "----", "$", comision)

    total_ventas += monto
    total_comisiones += comision

    if monto > mejor_venta:
        mejor_venta = monto
        mejor_nombre = nombres[i]

# Resumen
print("\n--- Resumen ---")
print("Total de ventas:", "$", total_ventas)
print("Total de comisiones:", "$", total_comisiones)
print("Mejor vendedor del día:", mejor_nombre, "con $", mejor_venta)

