# operradores de arismeticos
a= 10
b= 5

# suma 
suma = a + b
print(f"la summa de a y b es: {suma}")

# resta
resta = a - b   
print(f"la resta de a y b es: {resta}")

# multiplicacion
multiplicacion = a * b
print(f"la multiplicacion de a y b es: {multiplicacion}")

# division
division = a / b     
print(f"la division de a y b es: {division}")


# modulo o residuo
residuo = a % b
print(f"el residuo de a y b es: {residuo}")

# portencia o exponenciacion
portencia = a ** b
print(f"la portencia de a y b es: {portencia}")
# precedencia de operadores
resultado = a + b * 2
print(f"el resultado de a + b * 2 es: {resultado}")

resultado2 = (a * b) / 2
print(f"el resultado de (a * b) / 2 es: {resultado2}")

resultado3 = (a + b) // 2
print(f"el resultado de (a + b) // 2 es: {resultado3}")

resultado4 = ((a + b) + (a - b)*(a * b) % 2)
print(f"el resultado de (a + b) + (a - b)*(a * b) % 2 es: {resultado4}")

# libreria de matematicas 
import math
print(math.pi)
print(math.e)
print(math.sqrt(16))                                                     
 
import random
print(random.random())
numero_aletorio = random .randint(1, 100)
print(numero_aletorio)
