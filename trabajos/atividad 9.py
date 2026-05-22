# Conjuntos de aprendices

python_curso = {
    'Ana',
    'Luis',
    'Marta',
    'Carlos',
    'Sofia',
    'Pedro'
}

java_curso = {
    'Luis',
    'Carlos',
    'Pedro',
    'Laura',
    'Diego'
}

bd_curso = {
    'Marta',
    'Sofia',
    'Laura',
    'Ana',
    'Miguel'
}

# Unión de todos los aprendices

union_total = python_curso | java_curso | bd_curso


# Diccionario de conteo usando comprensión

conteo_programas = {

    aprendiz:
    (aprendiz in python_curso)
    + (aprendiz in java_curso)
    + (aprendiz in bd_curso)

    for aprendiz in union_total
}

# Mostrar resultados

print("Conteo de programas por aprendiz:")

for aprendiz, cantidad in conteo_programas.items():

    print(aprendiz, "->", cantidad)