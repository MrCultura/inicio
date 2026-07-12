#sintaxis de una funcion

#encabezado - def nombre_funcion (parametros): - define elnombre y que recibe.abs

#cuerpo - las lineas de codigo indentadas que ejecutan la logica de la funcion.abs

#parametros - los datos que lafuncion recibe para trabajo (pueden ser cero, uno o varios)

#retorno - la setencia return valor que entrega el resultado de vuelta

def calcular_promedio(nota1, nota2, nota3): #encabezado de mi funcion
    suma = nota1 + nota2 + nota3 #cuerpo
    promedio = suma / 3
    return promedio

resultado = calcular_promedio(8.0,9.0,7.0)
print(f"Promedio: {resultado.:.2f}")