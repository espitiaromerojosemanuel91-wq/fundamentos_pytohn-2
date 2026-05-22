# Función para calcular promedio

def calcular_promedio(notas):

    promedio = sum(notas) / len(notas)

    return promedio


# Ejemplo de reporte

notas = [4.0, 3.5, 4.2, 3.8]

promedio = calcular_promedio(notas)

print("Promedio:", round(promedio, 2))