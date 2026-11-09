# Tabla de multiplicar
try:
    numero = int(input("Ingresa un número: "))
    for multiplicador in range(1, 13):
        print(numero, "x", multiplicador, "=", numero * multiplicador)
except ValueError:
    print("Ingresa un número entero.")
