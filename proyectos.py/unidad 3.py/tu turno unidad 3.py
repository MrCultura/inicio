#Tu turno: Modifica la función para que reciba 4 calificaciones en lugar de 3, y ajusta el cálculo del promedio correctamente.

def calcular_promedio(nota1, nota2, nota3, nota4):
    suma = nota1 + nota2 + nota3 + nota4            
    promedio = suma / 4
    return promedio

resultado = calcular_promedio(8.0, 9.0, 7.0, 10.0)
print(f"Promedio: {resultado:.2f}")

#Tu turno: Escribe una función calcular_descuento(precio, porcentaje=10)
#que calcule el precio final con descuento. Pruébala una vez sin especificar el porcentaje y otra vez con un porcentaje distinto.

def calcular_descuento(precio, porcentaje=10): 
    descuento = precio * (porcentaje / 100)     
    precio_final = precio - descuento            
    return precio_final

#sin porcentaje
resultado1 = calcular_descuento(1000)
print(f"Precio final (10%): {resultado1:.2f}")

#con porcentaje
resultado2 = calcular_descuento(1000, 25)
print(f"Precio final (25%): {resultado2:.2f}")