# 1. Definición de los conjuntos de datos
python_students = {"Ana", "Carlos", "Luis", "María", "Pedro", "Elena"}
java_students = {"Carlos", "Luis", "Jorge", "Sofía", "Elena"}
bd_students = {"María", "Pedro", "Jorge", "Andrés", "Elena"}

# 2. Unión de todos los aprendices únicos
todos_los_aprendices = python_students | java_students | bd_students

# 3. Comprensión de diccionario para el conteo de programas
conteo_programas = {
    alumno: (alumno in python_students) + (alumno in java_students) + (alumno in bd_students)
    for alumno in todos_los_aprendices
}

# 4. Impresión del resultado en pantalla
print(conteo_programas)