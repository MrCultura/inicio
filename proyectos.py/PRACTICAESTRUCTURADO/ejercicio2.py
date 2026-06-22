#Tu turno: Escribe un for que imprima solo los múltiplos de 3 entre 3 y 30 usando range()
#con los argumentos correctos. No uses if dentro del for para filtrar — usa el paso de range().

print ("cuenta regresiva")
for  i in range (3, 31, 3):
    print(i, end=" ")

#ejercicio

calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0]

print("calificaciones del grupo")
for calificacion in calificaciones:
    print(f" {calificacion:.1f}")

total =  0
aprobados = 0

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:
        aprobados = aprobados + 1

promedio = total / len(calificaciones)
reprobados  = len(calificaciones) - aprobados

print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

#Turno: encuentra e imprime la calificación más alta y la más baja.
#Necesitarás dos variables que guarden el máximo y el mínimo mientras recorres la lista.

calificaciones = [7.2, 8.5, 6.0, 9.3, 7.8, 5.5]

maximo = calificaciones[0]
minimo = calificaciones[0]

for nota in calificaciones:
    if nota > maximo:
        maximo = nota
    if nota < minimo:
        minimo = nota

print(f"La calificación más alta es: {maximo}")
print(f"La calificación más baja es: {minimo}")

#Turno: Agrega al ejercicio un resumen al final del reporte: promedio del grupo y cantidad de
#aprobados, calculados dentro del mismo for que genera el reporte.

calificaciones = [7.2, 8.5, 6.0, 9.3, 7.8, 5.5]

maximo = calificaciones[0]
minimo = calificaciones[0]
suma = 0
aprobados = 0

for nota in calificaciones:
    print(f"Calificación: {nota}")

    # Actualizar máximo y mínimo
    if nota > maximo:
        maximo = nota
    if nota < minimo:
        minimo = nota

    suma += nota

    if nota >= 6:
        aprobados += 1

promedio = suma / len(calificaciones)

# Resumen final
print("\n--- Resumen del grupo ---")
print(f"Calificación más alta: {maximo}")
print(f"Calificación más baja: {minimo}")
print(f"Promedio del grupo: {promedio:.2f}")
print(f"Cantidad de aprobados: {aprobados}")
