def calculadora():
    print("--- Calculadora Básica ---")
    print("Operaciones: + , - , * , /")
    
    while True:
        num1 = float(input("Primer número: "))
        operacion = input("Operación (+, -, *, /) o 's' para salir: ")
        
        if operacion.lower() == 's':
            break
            
        num2 = float(input("Segundo número: "))

        if operacion == '+':
            print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
            print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
            print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Operación no válida.")
        
        print("-" * 20)

calculadora()