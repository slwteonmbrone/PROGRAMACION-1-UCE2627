# Suma de números desde 1 hasta N
try:
    limite = int(input("Ingresa un entero positivo: "))
    if limite > 0:
        acumulado = 0
        for numero in range(1, limite + 1):
            acumulado += numero
        print("La suma desde 1 hasta", limite, "es", acumulado)
    else:
        print("El número debe ser mayor que cero.")
except ValueError:
    print("Ingresa un número entero.")
