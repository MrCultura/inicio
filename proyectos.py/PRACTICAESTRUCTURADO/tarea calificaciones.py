
MIN_APROBADO = 6.0
NUM_ESTUDIANTES = 3

#nombres y notas
nombres = []
notas = []

# Captura de datos
for i in range(NUM_ESTUDIANTES):
    nombre = input(f"Nombre del estudiante {i+1}: ")
    nota = float(input(f"Nota de {nombre}: "))
    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10")
        nota = float(input(f"Nota de {nombre}: "))
    nombres.append(nombre)
    notas.append(nota)

# cálculos
suma = 0
aprobados = 0
reprobados = 0
mejor_nota = notas[0]
peor_nota = notas[0]
mejor_nombre = nombres[0]
peor_nombre = nombres[0]

# lista y calculos
for i in range(NUM_ESTUDIANTES):
    nota = notas[i]
    suma += nota

    if nota >= MIN_APROBADO:
        aprobados += 1
    else:
        reprobados += 1

    if nota > mejor_nota:
        mejor_nota = nota
        mejor_nombre = nombres[i]
    if nota < peor_nota:
        peor_nota = nota
        peor_nombre = nombres[i]

# Promedio
promedio = suma / NUM_ESTUDIANTES
porcentaje = (aprobados / NUM_ESTUDIANTES) * 100

# Reporte final
print("\n=== Reporte Final ===")
for i in range(NUM_ESTUDIANTES):
    estado = "Aprobado" if notas[i] >= MIN_APROBADO else "Reprobado"
    # Asignar letra con if/elif/else
    if notas[i] >= 9.0:
        letra = "A"
    elif notas[i] >= 8.0:
        letra = "B"
    elif notas[i] >= 7.0:
        letra = "C"
    elif notas[i] >= 6.0:
        letra = "D"
    else:
        letra = "F"
    print(f"{nombres[i]} - {notas[i]} - {estado} - {letra}")

print("\n--- Resumen ---")
print(f"Promedio del grupo: {promedio:.2f}")
print(f"Aprobados: {aprobados} | Reprobados: {reprobados}")
print(f"Mejor calificación: {mejor_nombre} con {mejor_nota}")
print(f"Peor calificación: {peor_nombre} con {peor_nota}")
print(f"Porcentaje de aprobación: {porcentaje:.1f}%")
