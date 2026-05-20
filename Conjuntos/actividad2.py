# 1. Definición de los conjuntos de aprendices por programa (Datos de prueba)
python_students = {"Ana", "Carlos", "Luis", "María", "Pedro", "Elena"}
java_students = {"Carlos", "Luis", "Jorge", "Sofía", "Elena"}
bd_students = {"María", "Pedro", "Jorge", "Andrés", "Elena"}

# 2. Total de aprendices únicos en los tres programas (Unión triple)
union_triple = python_students | java_students | bd_students

# 3. Aprendices que cursan Python Y Java simultáneamente (Intersección)
python_y_java = python_students & java_students

# 4. Aprendices que solo están en Python (No en Java ni en BD)
solo_python = python_students - (java_students | bd_students)

# 5. Aprendices que están en exactamente dos programas (Ni en uno solo ni en los tres)
p_j = python_students & java_students
j_b = java_students & bd_students
p_b = python_students & bd_students
# b. Intersección triple (los que están en los tres programas)
triple_interseccion = python_students & java_students & bd_students
# c. Unión de las intersecciones dobles menos la intersección triple
exactamente_dos = (p_j | j_b | p_b) - triple_interseccion

# 6. Impresión de resultados organizados
print("RESULTADOS DE OPERACIONES DE CONJUNTOS ")
print(f"Total de aprendices únicos (Unión triple): {len(union_triple)}")
print(f"-> Listado: {union_triple}\n")

print(f"Aprendices en Python Y Java simultáneamente: {len(python_y_java)}")
print(f"-> Listado: {python_y_java}\n")

print(f"Aprendices que SOLO están en Python: {len(solo_python)}")
print(f"-> Listado: {solo_python}\n")

print(f"Aprendices en exactamente DOS programas: {len(exactamente_dos)}")
print(f"-> Listado: {exactamente_dos}")

