print("=== Academia de Matemáticas ===")
NUMERO_DE_OPS = int(input("¿Cuántas operaciones vas a registrar? "))

# Listas
tipos = []
datos = []
resultados = []

# Funciones recursivas
def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

def suma_acumulada(n):
    if n == 1:
        return 1
    return n + suma_acumulada(n - 1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Datos
for i in range(NUMERO_DE_OPS):
    print("\n--- Operación", i+1, "---")
    print("1. Potencia\n2. Suma acumulada\n3. Factorial")
    opcion = int(input("Elige tipo de operación: "))

    if opcion == 1:
        base = int(input("Base: "))
        exp = int(input("Exponente: "))
        if exp < 0:
            print("El exponente no puede ser negativo.")
            tipos += ["Potencia"]
            datos += [f"base={base}, exp={exp}"]
            resultados += ["Inválido"]
        else:
            r = potencia(base, exp)
            print(f"Resultado: {base}^{exp} = {r}")
            tipos += ["Potencia"]
            datos += [f"base={base}, exp={exp}"]
            resultados += [r]

    elif opcion == 2:
        n = int(input("Número: "))
        if n <= 0:
            print("El número debe ser mayor a 0.")
            tipos += ["Suma acumulada"]
            datos += [f"n={n}"]
            resultados += ["Inválido"]
        else:
            r = suma_acumulada(n)
            print(f"Resultado: suma(1..{n}) = {r}")
            tipos += ["Suma acumulada"]
            datos += [f"n={n}"]
            resultados += [r]

    elif opcion == 3:
        n = int(input("Número: "))
        if n < 0:
            print("El número debe ser mayor o igual a 0.")
            tipos += ["Factorial"]
            datos += [f"n={n}"]
            resultados += ["Inválido"]
        else:
            r = factorial(n)
            print(f"Resultado: {n}! = {r}")
            tipos += ["Factorial"]
            datos += [f"n={n}"]
            resultados += [r]

    else:
        print("Opción inválida.")
        tipos += ["Error"]
        datos += ["opción inválida"]
        resultados += ["Inválido"]

# Reporte
print("\n=== Reporte de la sesión ===")
print("No.  Operación        Datos              Resultado")
for i in range(NUMERO_DE_OPS):
    print(f"{i+1:<4}{tipos[i]:<15}{datos[i]:<18}{resultados[i]}")
print("\nTotal de operaciones realizadas:", NUMERO_DE_OPS)