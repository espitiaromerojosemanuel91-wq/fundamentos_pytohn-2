# EJERCICIO 1:
from math import e

nombre = input("Introduce tu nombre: ")
valor_producto = float(input("Introduce el valor del producto: "))
promedio = float(input("Introduce tu promedio: "))
print(f"Hola {nombre}, el valor del producto es {valor_producto} y tu promedio es {promedio}.")


# EJERCICIO 2: 
entero1 = int(input("Introduce el primer entero: "))
entero2 = int(input("Introduce el segundo entero: "))
valor_float = float(input("Introduce un número float: "))
texto1 = input("Introduce la primera cadena: ")
texto2 = input("Introduce la segunda cadena: ")

# Suma
suma_numeros = entero1 + entero2 + valor_float
print("Suma de los tres números:", suma_numeros)

# Comparación
entero_mayor = entero1 if entero1 > entero2 else entero2
print("El entero mayor es:", entero_mayor)

# Operaciones combinadas (Resto y División)
resto_enteros = entero1 % entero2 if entero2 != 0 else None
if resto_enteros is None:
    print("No se puede calcular el resto: el segundo entero es 0.")
else:
    resultado_division = valor_float / resto_enteros if resto_enteros != 0 else None
    if resultado_division is None:
        print("No se puede dividir el float por el resto porque el resto es 0.")
    else:
        print("Resultado de dividir el float entre el resto de los dos enteros:", resultado_division)

# Concatenación
concatenacion = texto1 + texto2
print("Concatenación de las dos cadenas:", concatenacion)


# EJERCICIO 3: 
Base = int(input("Introduce la base: "))
Exponente = int(input("Introduce el exponente: "))
potencia = Base ** Exponente
print(f"La potencia de {Base} elevado a {Exponente} es {potencia}")


# EJERCICIO 4: 
numeros = [2, 8, 9, 27, 28, 55, 121]
for numero in numeros:
    raiz_cuadrada = numero ** 0.5
    print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}.")


#  EJERCICIO 5:
nombre_estudiante = input("Introduce el nombre del estudiante: ")
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))
nota4 = float(input("Introduce la cuarta nota: "))
nota5 = float(input("Introduce la quinta nota: "))
promedio_final = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f"El promedio final de {nombre_estudiante} es {promedio_final}.")


#EJERCICIO 6: 
numeroUno = 8
numeroDos = 2
print(f"Antes del intercambio: numeroUno = {numeroUno}, numeroDos = {numeroDos}")

auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = auxiliar
print(f"Después del intercambio: numeroUno = {numeroUno}, numeroDos = {numeroDos}")


#EJERCICIO 7: 
Estado = (5 == 2) or (2 > 1)
print(f"El resultado de la variable Estado es: {Estado}")


# EJERCICIO 8:
resultado = (18 + 6) * 3 / 8 ** 4 + (25 // 4) % 2 - (6 * 0.9)
print(f"El resultado de la operación compleja es: {resultado}")


# EJERCICIO 9: 

# Cuadrado
ladoCuadrado = 8
area_cuadrado = ladoCuadrado ** 2
perimetro_cuadrado = 4 * ladoCuadrado
print(f"Cuadrado -> Área: {area_cuadrado}, Perímetro: {perimetro_cuadrado}")

# Triángulo
baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8
area_triangulo = (baseTriangulo * alturaTriangulo) / 2
perimetro_triangulo = baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo
print(f"Triángulo -> Área: {area_triangulo}, Perímetro: {perimetro_triangulo}")

# Rectángulo
baseRectangulo = 8
alturaRectangulo = 6
area_rectangulo = baseRectangulo * alturaRectangulo
perimetro_rectangulo = 2 * (baseRectangulo + alturaRectangulo)
print(f"Rectángulo -> Área: {area_rectangulo}, Perímetro: {perimetro_rectangulo}")


# EJERCICIO 10:
try:
    edad = int(input("Introduce la edad de la persona: "))
    
    if 0 <= edad <= 5:
        categoria = "Infante"
    elif 6 <= edad <= 10:
        categoria = "Niño"
    elif 11 <= edad <= 15:
        categoria = "Pre adolescente"
    elif 16 <= edad <= 18:
        categoria = "Adolescente"
    elif 19 <= edad <= 25:
        categoria = "Pre adulto"
    elif 26 <= edad <= 40:
        categoria = "Adulto"
    elif 41 <= edad <= 55:
        categoria = "Pre anciano"
    elif edad >= 56:
        categoria = "Anciano"
    else:
        categoria = "Edad no válida (negativa)"

    print(f"Categoría: {categoria}")

except ValueError:
    print("Por favor, introduce un número entero válido.")