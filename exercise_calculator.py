def calculator():
    """
    Ejercicio 7 - Calculadora Simple

    Leer dos números (pueden ser decimales) y una operación (+, -, *, /) mediante input().
    Realizar la operación correspondiente e imprimir el resultado.

    Validaciones:
    - Si la operación es inválida, imprimir "Operacion invalida"
    - Si es división y el divisor es cero, imprimir "Error: division por cero"

    Ejemplo:
        Para las entradas "10", "5" y "+", la salida esperada es:
        Resultado: 15.0

        Para las entradas "10", "2" y "/", la salida esperada es:
        Resultado: 5.0

        Para las entradas "10", "0" y "/", la salida esperada es:
        Error: division por cero

        Para las entradas "10", "5" y "x", la salida esperada es:
        Operacion invalida
    """
    numero_1 = float(input())
    numero_2 = float(input())
    operacion = input()

    if operacion == '+':
        print(f"Resultado: {numero_1 + numero_2}")
    elif operacion == '-':
        print(f"Resultado: {numero_1 - numero_2}")
    elif operacion == '*':
        print(f"Resultado: {numero_1 * numero_2}")
    elif operacion == '/' and numero_1 != 0 and numero_2 != 0:
        print(f"Resultado: {numero_1 / numero_2}")
    elif operacion == '/' and numero_1 == 0 or numero_2 == 0:
        print(f"Error: division por cero")
    else:
        print("Operacion invalida")

