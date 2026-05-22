import pprint  # ← Movido aquí arriba para quitar el aviso amarillo

# # Creación del diccionario con aprendices existentes
dicc = {
    101: {"nombre": "Ana Gomez", "edad": 19, "notas": [4.5, 3.8, 4.2], "ciudad": "Bogotá"},
    102: {"nombre": "Carlos Perez", "edad": 21, "notas": [2.5, 3.0, 2.8], "ciudad": "Medellín"}
}

# # Agrega un nuevo aprendiz al diccionario después de crearlo, usando una nueva clave de ficha
dicc[105] = {
    "nombre": "Carlos Ruiz",
    "edad": 21,
    "notas": [4.0, 3.8, 4.5, 4.2],
    "ciudad": "Barranquilla"
}

# # Luego actualiza la ciudad de uno de los aprendices existentes
dicc[102]['ciudad'] = 'Nueva Ciudad'

#AGREGA ESTO PARA MOSTRAR LOS RESULTADOS EN LA TERMINAL 
print("Diccionario actualizado:")
pprint.pprint(dicc)

