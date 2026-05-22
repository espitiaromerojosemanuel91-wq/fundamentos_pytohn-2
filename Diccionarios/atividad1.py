# 1. Creación del diccionario 'grupo' con al menos 4 aprendices
grupo = {
    101: {
        "nombre": "Ana Gomez",
        "edad": 20,
        "notas": [4.5, 3.8, 4.2, 4.0],
        "ciudad": "Bogota"
    },
    102: {
        "nombre": "Luis Perez",
        "edad": 22,
        "notas": [2.5, 3.0, 2.8, 3.2],
        "ciudad": "Medellin"
    },
    103: {
        "nombre": "Maria Silva",
        "edad": 19,
        "notas": [4.8, 4.9, 4.7, 5.0],
        "ciudad": "Cali"
    },
    104: {
        "nombre": "Carlos Mendoza",
        "edad": 21,
        "notas": [2.0, 3.5, 2.2, 1.8],
        "ciudad": "Bucaramanga"
    }
}

# 2. Función para calcular el promedio de una lista de notas
def calcular_promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)

# 4. Agregar un nuevo aprendiz usando una nueva clave de ficha
grupo[105] = {
    "nombre": "Elena Rojas",
    "edad": 23,
    "notas": [4.0, 4.1, 3.9, 4.3],
    "ciudad": "Cartagena"
}

# 4. Actualizar la ciudad de uno de los aprendices existentes
grupo[101]['ciudad'] = 'Nueva Ciudad'


# 3. Función para imprimir el reporte estándar usando .items() y un ciclo for
def mostrar_reporte(diccionario_grupo):
    print(" REPORTE DE APRENDICES ")
    for ficha, datos in diccionario_grupo.items():
        promedio = calcular_promedio(datos["notas"])
        # Se eliminó la variable 'estado' y su validación
        print(f"Ficha: {ficha} | Nombre: {datos['nombre']} | Edad: {datos['edad']} | Promedio: {promedio:.2f}")
    print("-" * 30)

# 5. BONUS: Función para ordenar de mayor a menor promedio usando sorted() con key=
def mostrar_reporte_ordenado(diccionario_grupo):
    print("\n REPORTE ORDENADO POR PROMEDIO (MAYOR A MENOR) ")
    
    # Ordenar los elementos por el promedio calculado dentro de los datos
    grupo_ordenado = sorted(
        diccionario_grupo.items(), 
        key=lambda item: calcular_promedio(item[1]["notas"]), 
        reverse=True
    )
    
    for ficha, datos in grupo_ordenado:
        promedio = calcular_promedio(datos["notas"])
        # Se eliminó la variable 'estado' y su validación
        print(f"Ficha: {ficha} | Nombre: {datos['nombre']} | Promedio: {promedio:.2f}")
    print("-" * 30)


# Ejecución de las funciones para mostrar los resultados en consola
mostrar_reporte(grupo)
mostrar_reporte_ordenado(grupo)
