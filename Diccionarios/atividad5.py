# 1. Asegúrate de tener la función y el diccionario definidos arriba
def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)

grupo = {
    "101": {"nombre": "Ana Gomez", "edad": 19, "notas": [4.5, 3.8, 4.2]},
    "102": {"nombre": "Carlos Perez", "edad": 21, "notas": [2.5, 3.0, 2.8]}
}

# # 5. Bonus: Ordenar e imprimir de mayor a menor promedio
print("=== APRENDICES ORDENADOS POR PROMEDIO ===")

# CORRECCIÓN: Se usa aprendiz[1]['notas'] porque .items() devuelve (clave, valor)
grupo_ordenado = sorted(
    grupo.items(),
    key=lambda aprendiz: calcular_promedio(aprendiz[1]['notas']),
    reverse=True
)

# Imprimir el resultado ordenado
for ficha, datos in grupo_ordenado:
    prom = calcular_promedio(datos['notas'])
    print(f"Promedio: {prom:.2f} -> Ficha: {ficha} | Nombre: {datos['nombre']}")
