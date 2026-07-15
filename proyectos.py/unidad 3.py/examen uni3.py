print("=== Ferreteria don julio ===")
REALIZAR_PRESTAMO = 1
HISTORIAL_DE_PRESTAMOS = 2
SALIR_DEL_SISTEMA = 3

def mostrar_menu():
    print("\n--- Menu principal ---")
    print("1. Realizar préstamo")
    print("2. Ver historial de préstamos")
    print("3. Salir del sistema")

def mostrar_historial(historial):
    print("\n=== Historial de préstamos ===")
    if not historial:
        print("No hay operaciones registradas aun.")
    else:
        print("Nombre         Herramienta      Dias   Total a pagar")
        for op in historial:
            print(f"{op['nombre']:<15}{op['herramienta']:<18}{op['dias']:<6}{op['total']}")
        print("\nTotal de operaciones realizadas:", len(historial))

historial = []

while True:
    mostrar_menu()
    opcion = int(input("Elige una opcion: "))

    if opcion == REALIZAR_PRESTAMO:
        nombre = input("Nombre: ")
        herramienta = input("Herramienta: ")
        dias = int(input("Dias: "))
        if dias < 0:
            print("Ingrese un numero valido de dias.")
        else:
            total = 50 * ((2**dias) - 1)
            print(f"Total a pagar: {total}")
            historial.append({
                "nombre": nombre,
                "herramienta": herramienta,
                "dias": dias,
                "total": total
            })

    elif opcion == HISTORIAL_DE_PRESTAMOS:
        mostrar_historial(historial)
    
    elif opcion == SALIR_DEL_SISTEMA:
        print("Buen dia, regrese pronto")
        break