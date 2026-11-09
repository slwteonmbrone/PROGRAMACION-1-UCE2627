# Calculadora de cuatro operaciones

# Pedimos los dos números para hacer la operación
numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
print("1. Sumar  2. Restar  3. Multiplicar  4. Dividir")
opcion = input("Elige una opción: ")

# Revisamos qué operación eligió el usuario
if opcion == "1":
        print("Resultado:", numero1 + numero2)
elif opcion == "2":
        print("Resultado:", numero1 - numero2)
elif opcion == "3":
        print("Resultado:", numero1 * numero2)
elif opcion == "4":
    # Comprobamos que el divisor no sea cero
    if numero2 != 0:
            print("Resultado:", numero1 / numero2)
    else:
            print("No se puede dividir entre cero.")
else:
        print("La opción no existe.")
