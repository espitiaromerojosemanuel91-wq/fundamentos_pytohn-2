# Diccionario grupo

grupo = {

    101: {
        "nombre": "Aprendiz 1",
        "edad": 20,
        "notas": [4.0, 3.5, 4.2, 3.8],
        "ciudad": "Bogotá"
    },

    102: {
        "nombre": "Aprendiz 2",
        "edad": 19,
        "notas": [3.0, 3.2, 3.5, 3.8],
        "ciudad": "Cali"
    }

}

# Agregar nuevo aprendiz

grupo[103] = {
    "nombre": "Aprendiz 3",
    "edad": 21,
    "notas": [4.5, 4.6, 4.8, 5.0],
    "ciudad": "Medellín"
}

# Actualizar ciudad

grupo[102]["ciudad"] = "Nueva Ciudad"

# Mostrar información

for ficha, datos in grupo.items():

    print("\nFicha:", ficha)
    print("Nombre:", datos["nombre"])
    print("Ciudad:", datos["ciudad"])