# Ejercicio: calculadora de notas
def pedir_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 1 <= nota <= 5:
                return nota
            else:
                print("Error: La calificación debe estar entre 1 y 5.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

nota1 = pedir_nota("Ingrese la primera calificación (1-5): ")
nota2 = pedir_nota("Ingrese la segunda calificación (1-5): ")
nota3 = pedir_nota("Ingrese la tercera calificación (1-5): ")

promedio = (nota1 + nota2 + nota3) / 3

puntos_faltantes = 5.0 - promedio

aprueba = promedio >= 3.0


print("\n" + "="*40)
print("RESULTADOS DEL ESTUDIANTE")
print("="*40)
print(f"Calificación 1: {nota1}")
print(f"Calificación 2: {nota2}")
print(f"Calificación 3: {nota3}")
print(f"\nPromedio: {round(promedio, 2)}")
print(f"Puntos faltantes para 5.0: {round(puntos_faltantes, 2)}")
print(f"\nEstado: {' APROBADO' if aprueba else ' REPROBADO'}")
print("="*40)
