# actividad4_sets.py

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


# 1. Unión triple

union_total = python_curso | java_curso | bd_curso

print("Total de aprendices únicos:")
print(union_total)


# 2. Python y Java simultáneamente

python_java = python_curso & java_curso

print("\nAprendices en Python y Java:")
print(python_java)


# 3. Solo en Python

solo_python = python_curso - java_curso - bd_curso

print("\nAprendices solo en Python:")
print(solo_python)


# 4. Exactamente en dos programas

dos_programas = (
    (python_curso & java_curso)
    |
    (python_curso & bd_curso)
    |
    (java_curso & bd_curso)
)

tres_programas = python_curso & java_curso & bd_curso

dos_programas = dos_programas - tres_programas

print("\nAprendices en exactamente dos programas:")
print(dos_programas)