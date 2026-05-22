# actividad2_diccionarios.py

# Diccionario de aprendices

grupo = {

    101: {
        "nombre": "Carlos",
        "edad": 20,
        "notas": [4.0, 3.5, 4.2, 3.8],
        "ciudad": "Bogotá"
    },

    102: {
        "nombre": "Ana",
        "edad": 19,
        "notas": [3.2, 3.8, 4.0, 3.5],
        "ciudad": "Medellín"
    },

    103: {
        "nombre": "Luis",
        "edad": 22,
        "notas": [4.5, 4.7, 4.8, 5.0],
        "ciudad": "Cali"
    },

    104: {
        "nombre": "Sofía",
        "edad": 21,
        "notas": [3.0, 3.4, 3.6, 3.9],
        "ciudad": "Tunja"
    }

}

# Mostrar información del grupo

for ficha, datos in grupo.items():

    print("\nFicha:", ficha)
    print("Nombre:", datos["nombre"])
    print("Edad:", datos["edad"])
    print("Notas:", datos["notas"])
    print("Ciudad:", datos["ciudad"])