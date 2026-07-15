print("=== Academia de Matemáticas ===")

OPCION_POTENCIA = 1
OPCION_SUMA = 2
OPCION_FACTORIAL = 3
OPCION_REPORTE = 4
OPCION_SALIR = 5

# Funciones recursivas
def potencia(base, exp):
    """Calcula la potencia de un número usando recursividad"""
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

def suma_acumulada(n):
    """Calcula la suma acumulada de 1 hasta n usando recursividad"""
    if n == 1:
        return 1
    return n + suma_acumulada(n - 1)

def factorial(n):
    """Calcula el factorial de un número usando recursividad"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Procedimientos
def mostrar_menu():
    """Muestra el menú principal"""
    print("\n--- Menú principal ---")
    print("1. Calcular potencia")
    print("2. Calcular suma acumulada")
    print("3. Calcular factorial")
    print("4. Ver reporte de la sesión")
    print("5. Salir")

def mostrar_reporte(historial):
    """Muestra el reporte de la sesión"""
    print("\n=== Reporte de la sesión ===")
    if not historial:
        print("No hay operaciones registradas aún.")
    else:
        print("No.  Operación        Datos              Resultado")
        for i, op in enumerate(historial, start=1):
            print(f"{i:<4}{op['tipo']:<15}{op['datos']:<18}{op['resultado']}")
        print("\nTotal de operaciones realizadas:", len(historial))

# Programa principal
historial = []

while True:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))

    if opcion == OPCION_POTENCIA:
        base = int(input("Base: "))
        exp = int(input("Exponente: "))
        if exp < 0:
            print("El exponente no puede ser negativo.")
        else:
            resultado = potencia(base, exp)
            print(f"Resultado: {base}^{exp} = {resultado}")
            historial.append({"tipo": "Potencia", "datos": f"base={base}, exp={exp}", "resultado": resultado})

    elif opcion == OPCION_SUMA:
        n = int(input("Número: "))
        if n <= 0:
            print("El número debe ser mayor a 0.")
        else:
            resultado = suma_acumulada(n)
            print(f"Resultado: suma(1..{n}) = {resultado}")
            historial.append({"tipo": "Suma acumulada", "datos": f"n={n}", "resultado": resultado})

    elif opcion == OPCION_FACTORIAL:
        n = int(input("Número: "))
        if n < 0:
            print("El número debe ser mayor o igual a 0.")
        else:
            resultado = factorial(n)
            print(f"Resultado: {n}! = {resultado}")
            historial.append({"tipo": "Factorial", "datos": f"n={n}", "resultado": resultado})

    elif opcion == OPCION_REPORTE:
        mostrar_reporte(historial)

    elif opcion == OPCION_SALIR:
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")