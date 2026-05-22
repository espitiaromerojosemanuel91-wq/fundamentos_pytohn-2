# 1. Definición de conjuntos de aprendices por programa
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}
java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}
bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

# 2. Operaciones de conjuntos
todos_aprendices = python_curso | java_curso | bd_curso

# Cursan Python Y Java simultáneamente (Intersección)
python_y_java = python_curso & java_curso

# Solo están en Python (Diferencia)
solo_python = python_curso - java_curso - bd_curso

# Están en exactamente dos programas
interseccion_triple = python_curso & java_curso & bd_curso
exactamente_dos = (
    ((python_curso & java_curso) | (python_curso & bd_curso) | (java_curso & bd_curso)) 
    - interseccion_triple
)

print("2. RESULTADOS DE OPERACIONES DE CONJUNTOS:")
print(f"   Total de aprendices únicos: {todos_aprendices}")
print(f"   Cursan Python y Java: {python_y_java}")
print(f"   Solo están en Python: {solo_python}")
print(f"   En exactamente dos programas: {exactamente_dos}\n")

# 3. Eliminar duplicados con conjuntos
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']
aprendices_unicos = set(inscripciones)

# 4. Diccionario conteo_programas usando comprensión de diccionarios
conteo_programas = {
    alumno: (1 if alumno in python_curso else 0) + 
            (1 if alumno in java_curso else 0) + 
            (1 if alumno in bd_curso else 0)
    for alumno in todos_aprendices
}

