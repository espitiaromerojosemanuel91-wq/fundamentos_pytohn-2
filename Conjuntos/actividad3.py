# 1. Definición de la lista original con duplicados
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']

# 2. Conversión a conjunto para filtrar elementos únicos
aprendices_unicos = set(inscripciones)

# 3. Cálculo de la cantidad total de elementos únicos
total_unicos = len(aprendices_unicos)

# 4. Impresión de resultados
print(f"Total de aprendices únicos inscritos: {total_unicos}")
print(f"¿Quiénes son?: {aprendices_unicos}")
