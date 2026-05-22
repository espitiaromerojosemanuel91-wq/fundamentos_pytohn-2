#ejercios : creativos
#ejercicio 1: Tiempo Libre
import re 

def limpiar_entrada(texto):
    # Busca números (incluso con decimales como 1.5)
    numeros = re.findall(r"[-+]?\d*\.\d+|\d+", texto)
    if numeros:
        return float(numeros[0])
    return None

# CONFIGURACIÓN 
actividades = ["🎮Jugar Videojuegos","💼Trabajo", "📚Estudio", "📺ver Televisión", "😴Dormir", "🍽️Comer", "💪Hacer Ejercicio", "📝Actividades o tareas"]
resultados = {}
total_horas = 0

print("--- ORGANIZADOR DE TIEMPO INTELIGENTE ---")
print("Puedes escribir '1', '1 hora' o '1h'.\n")

# --- RECOLECCIÓN DE DATOS ---
for act in actividades:
    while True:
        disponible = 24 - total_horas
        entrada = input(f"¿Horas para {act}? (Quedan {disponible:.1f}h): ")
        horas = limpiar_entrada(entrada)
        
        if horas is None:
            print(f"Error: Escribe un número.")
            continue
        if total_horas + horas > 24:
            print(f"¡Error! Te pasas de las 24h (Solo quedan {disponible:.1f}h).")
            continue
            
        total_horas += horas
        resultados[act] = horas
        break

# ESTO ES LO QUE FALTABA: EL RESUMEN FINAL 
print("\n" + "="*50)
print("             RESUMEN DE TU TIEMPO")
print("="*50)

for act, h in resultados.items():
    if h > 0: # Solo mostramos lo que haces más de 0 horas
        minutos = h * 60
        porcentaje = (h / 24) * 100
        dias_al_anio = (h * 365) / 24
        
        print(f"\n>> {act.upper()}")
        print(f"   • Tiempo diario: {h}h ({minutos:.0f} min)")
        print(f"   • Representa el: {porcentaje:.1f}% de tu día")
        print(f"   • Al año le dedicas: {dias_al_anio:.1f} días completos")

print("\n" + "="*50)
libre = 24 - total_horas
if libre > 0:
    print(f"Te sobran {libre:.1f} horas de 'Tiempo Libre' extra.")
else:
    print("Has ocupado las 24 horas exactas del día.")
