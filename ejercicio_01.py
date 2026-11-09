# Calculadora de cuatro operaciones

numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
print("1. Sumar  2. Restar  3. Multiplicar  4. Dividir")
opcion = input("Elige una opción: ")
if opcion == "1":
        print("Resultado:", numero1 + numero2)
elif opcion == "2":
        print("Resultado:", numero1 - numero2)
elif opcion == "3":
        print("Resultado:", numero1 * numero2)
elif opcion == "4":
    if numero2 != 0:
            print("Resultado:", numero1 / numero2)
    else:
            print("No se puede dividir entre cero.")
else:
        print("La opción no existe.")
