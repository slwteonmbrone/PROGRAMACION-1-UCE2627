# Cajero automático sencillo
saldo = 500.0
opcion = ""
while opcion != "4":
    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1. Consultar saldo\n2. Depositar dinero\n3. Retirar dinero\n4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Saldo disponible: $", round(saldo, 2))
    elif opcion == "2" or opcion == "3":
        try:
            monto = float(input("Ingrese el monto: "))
            if monto <= 0:
                print("El monto debe ser mayor que cero.")
            elif opcion == "2":
                saldo += monto
                print("Depósito realizado. Saldo: $", round(saldo, 2))
            elif monto > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= monto
                print("Retiro realizado. Saldo: $", round(saldo, 2))
        except ValueError:
            print("Ingresa un monto válido.")
    elif opcion == "4":
        print("Gracias por usar el cajero.")
    else:
        print("Opción incorrecta.")
