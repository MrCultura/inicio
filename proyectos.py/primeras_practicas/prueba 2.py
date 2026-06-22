resultado = 5 + 2.0
print(type(resultado))

#Emplicita str a int
texto_numero = '42'
numero_real = int(texto_numero)
print(numero_real + 8)

#Explicita:int  a str para concatenar

edad =  28
mensaje = 'hola, soy alex,y mi edad es' + str(edad)
print(mensaje)

#fload a int
precio = 9.99
print  (int(precio))

numero = 7.99
redondeado = round(numero)
print(redondeado)

# simularemos input con variables fijas
dato_usuario  ='25'
print(type(dato_usuario))
#print(dato_usuario + 5)

edad_correcta = int(dato_usuario)
print(edad_correcta +  5)

#patron correcto para entrada de datos:
#edad = int(input('ingresa tu edad'))

#Escriba un programa que pida al usuario  su nombre (str) y su año de nacimiento (int). calcula e imprime su edad aproximada restando al año actual (2026)
nombre = str(input('ingresa tu nombre'))
año_de_nacimiento = int(input('ingresa tu año de nacimiento'))
print(2026 - (año_de_nacimiento))