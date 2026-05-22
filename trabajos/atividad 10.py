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

# Aprendices matriculados en los tres programas

tres_programas = python_curso & java_curso & bd_curso

# Mostrar resultados

print("Aprendices en los tres programas:")
print(tres_programas)