def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)

# Uso de la función al mostrar el reporte
grupo = {
    101: {
        "notas": [4.5, 3.8, 4.2]
    }
}

# 1. Calculas el promedio usando la función y los datos del diccionario
promedio_grupo = calcular_promedio(grupo[101]["notas"])

# 2. Imprimes el resultado general sin nombres de personas
print(f"El promedio del grupo es: {promedio_grupo:.2f}")

