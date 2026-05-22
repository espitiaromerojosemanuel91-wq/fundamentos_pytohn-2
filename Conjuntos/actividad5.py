# TALLER DE PYTHON: OPERACIONES DE CONJUNTOS Y DICCIONARIOS
# 1. Definición de los conjuntos de datos iniciales
python_students = {"Ana", "Carlos", "Luis", "María", "Pedro", "Elena"}
java_students = {"Carlos", "Luis", "Jorge", "Sofía", "Elena"}
bd_students = {"María", "Pedro", "Jorge", "Andrés", "Elena"}

# PUNTO 2: Operaciones avanzadas de conjuntos
print("PUNTO 2 ")

# El total de aprendices únicos en los tres programas (Unión triple)
union_triple = python_students | java_students | bd_students
print(f"Total de aprendices únicos: {len(union_triple)}")
print(f"-> Listado: {union_triple}\n")

# Los aprendices que cursan Python Y Java simultáneamente (Intersección)
python_y_java = python_students & java_students
print(f"Aprendices en Python Y Java: {len(python_y_java)}")
print(f"-> Listado: {python_y_java}\n")

# Los aprendices que solo están en Python (No en Java ni en BD)
solo_python = python_students - (java_students | bd_students)
print(f"Aprendices SOLO en Python: {len(solo_python)}")
print(f"-> Listado: {solo_python}\n")

# Los aprendices que están en exactamente dos programas
p_j = python_students & java_students
j_b = java_students & bd_students
p_b = python_students & bd_students
triple_interseccion = python_students & java_students & bd_students
exactamente_dos = (p_j | j_b | p_b) - triple_interseccion

print(f"Aprendices en exactamente DOS programas: {len(exactamente_dos)}")
print(f"-> Listado: {exactamente_dos}\n")


# PUNTO 3: Filtrar duplicados de una lista usando conjuntos

print(" PUNTO 3 ")
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']

# Conversión a conjunto para eliminar duplicados de forma automática
aprendices_unicos = set(inscripciones)

print(f"Cantidad de inscritos únicos: {len(aprendices_unicos)}")
print(f"¿Quiénes son?: {aprendices_unicos}\n")



# PUNTO 4: Conteo de programas usando comprensión de diccionarios

print(" PUNTO 4")

conteo_programas = {
    alumno: (alumno in python_students) + (alumno in java_students) + (alumno in bd_students)
    for alumno in union_triple
}

print("Diccionario de conteo por aprendiz:")
print(conteo_programas, "\n")


# PUNTO 5 (BONUS): Identificar quién está en los tres programas a la vez

print(" PUNTO 5 ")

matriculados_en_tres = python_students & java_students & bd_students

if matriculados_en_tres:
    # Formato limpio usando .join() para no mostrar las llaves {} del conjunto
    nombres_limpios = ", ".join(matriculados_en_tres)
    print(f"Aprendices matriculados en los tres programas: {nombres_limpios}")
else:
    print("No hay ningún aprendiz matriculado en los tres programas a la vez.")


