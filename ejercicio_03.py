# Tabla de multiplicar
try:
    numero = int(input("Ingresa un número: "))
    # Repetimos la multiplicación desde el 1 hasta el 12
    for multiplicador in range(1, 13):
        print(numero, "x", multiplicador, "=", numero * multiplicador)
except ValueError:
    print("Ingresa un número entero.")
