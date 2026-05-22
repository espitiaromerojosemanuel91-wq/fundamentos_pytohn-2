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


# Reporte

for ficha, datos in grupo.items():

    promedio = calcular_promedio(datos["notas"])

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print("\nFicha:", ficha)
    print("Nombre:", datos["nombre"])
    print("Edad:", datos["edad"])
    print("Promedio:", round(promedio, 2))
    print("Estado:", estado)