# 2. Función para calcular el promedio de una lista de notas
def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)

# Estructura del diccionario 'grupo' con los datos requeridos por tu reporte
grupo = {
    "101": {"nombre": "Ana Gomez", "edad": 19, "notas": [4.5, 3.8, 4.2]},
    "102": {"nombre": "Carlos Perez", "edad": 21, "notas": [2.5, 3.0, 2.8]}
}

# 3. Impresión del reporte usando .items() y ciclo for
print("REPORTE DE APRENDICES ")

for ficha, datos in grupo.items():
    # Se calcula el promedio usando la función del punto 2
    promedio = calcular_promedio(datos['notas'])
    
    # Se determina el estado según la condición establecida
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    
    # Impresión del reporte formateado
    print(f"Ficha: {ficha:<5} | Nombre: {datos['nombre']:<15} | Edad: {datos['edad']:<3} | "
          f"Promedio: {promedio:.2f} | Estado: {estado}")



