# Función para calcular promedio

def calcular_promedio(notas):

    return sum(notas) / len(notas)


# Diccionario grupo

grupo = {

    101: {
        "nombre": "Aprendiz 1",
        "edad": 20,
        "notas": [4.0, 3.5, 4.2, 3.8]
    },

    102: {
        "nombre": "Aprendiz 2",
        "edad": 19,
        "notas": [2.5, 2.8, 3.0, 2.9]
    },

    103: {
        "nombre": "Aprendiz 3",
        "edad": 21,
        "notas": [4.5, 4.7, 4.8, 5.0]
    },

    104: {
        "nombre": "Aprendiz 4",
        "edad": 22,
        "notas": [3.0, 3.2, 3.5, 3.8]
    }

}


# Ordenar de mayor a menor promedio

ordenados = sorted(

    grupo.items(),

    key=lambda item: calcular_promedio(item[1]["notas"]),

    reverse=True

)


# Mostrar resultados

print("=== APRENDICES ORDENADOS POR PROMEDIO ===")

for ficha, datos in ordenados:

    promedio = calcular_promedio(datos["notas"])

    print("\nFicha:", ficha)
    print("Nombre:", datos["nombre"])
    print("Promedio:", round(promedio, 2))