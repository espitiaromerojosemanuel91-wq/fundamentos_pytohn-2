# Lista con duplicados

inscripciones = [
    'Ana',
    'Luis',
    'Ana',
    'Marta',
    'Carlos',
    'Luis',
    'Sofia',
    'Pedro',
    'Ana'
]

# Convertir la lista en conjunto

aprendices_unicos = set(inscripciones)

# Mostrar resultados

print("Cantidad de aprendices únicos:")
print(len(aprendices_unicos))

print("\nAprendices únicos:")
print(aprendices_unicos)