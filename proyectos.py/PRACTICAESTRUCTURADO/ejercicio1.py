# Python usa la sangría (espacios al inicio de la línea) para delimitar bloques de código.{}, Python usa 4 espacios por nivel. Esta es la diferencia visual más importante entre python y otros lenguajes.

#if condicion:
#   instruccion1
#else:
#    instruccion2

#Toda estructura de control termina su primera línea con dos puntos ":". Los dos puntos le dicen Python: el bloque de esta estructura comienza en la siguiente línea. Si se omiten, Python genera SyntaxError: expected ':'

#= asignar un valor
#== comparar dos valores Igual que
#!= Diferente de
#> Mayor que / >= Mayor o igual
#< Menor que / <= Menor o igual
# and Ambas condiciones True / or Al menos una es true / not Negación lógica
#IF ejecuta un bloque únicamente si la condición es True. Si la condición es False, el bloque se salta por completo y el programa continúa. Solo tiene una rama posible.

#SI condicion ENTONCES
#   Instrucción
#FIN SI
    #SI FALSE -> Se omite el bloque

#nota = 8.5

#if nota >=6.0:
    #print("El alumno aprobo")

#print("Fin del programa")

#CONDICION DOBLE-if/else
#el else garantiza que siempre se ejecuta algo.

#ejercicio 2

#CALIFICACION_MINIMA =7.0

#nota  = float(input("Ingresa tu calificacion"))

#if nota >= CALIFICACION_MINIMA:
    #print(f"Aprobado con {nota:.1f}")
#else:
   # print(f"Reprobado con {nota:.1f}")
    #faltaron = CALIFICACION_MINIMA - nota
    #print(f"Te faltaron {faltaron:.1}  puntos para aprobar")
    
#Crea una condición que verifique si un año es bisiesto.
#Un año es bisiesto si es divisible entre 4, Y si es divisible entre 100, también
#debe ser divisible entre 400.
#Pista: usa el operador % (módulo).

#año = int(input("Ingresa un año: "))

#if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    #print(f"{año} es un año bisiesto")
#else:
    #print(f"{año} no es un año bisiesto")


#Tu turno: Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra.
#Por ejemplo, si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.

# Programa para mostrar letra y puntos faltantes

calificacion = float(input("Ingresa tu calificación"))

if calificacion >= 9:
    letra = "A"
    faltan = 0
elif calificacion >= 8:
    letra = "B"
    faltan = 9 - calificacion
elif calificacion >= 7:
    letra = "C"
    faltan = 8 - calificacion
elif calificacion >= 6:
    letra = "D"
    faltan = 7 - calificacion
else:
    letra = "F"
    faltan = 6 - calificacion

print(f"Tu calificación es {calificacion} = {letra}")

if letra != "A":  # Solo mostrar si no es la máxima
    print(f"Necesitas {faltan:.1f} puntos para subir a la siguiente letra")
