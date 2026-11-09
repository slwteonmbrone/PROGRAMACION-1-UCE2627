# Sistema de ventas con funciones
# Esta función pide un precio válido
def pedir_precio():
    while True:
        try:
            precio = float(input("Precio unitario: $"))
            if precio > 0:
                return precio
            print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Ingresa un precio numérico.")

# Esta función comprueba que la cantidad sea positiva
def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                return cantidad
            print("La cantidad debe ser un entero positivo.")
        except ValueError:
            print("Ingresa una cantidad entera.")

# Aquí guardamos los productos de la compra
productos = []
subtotal = 0
while True:
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        continue

    # Calculamos cuánto cuesta este producto en total
    precio = pedir_precio()
    cantidad = pedir_cantidad()
    importe = precio * cantidad
    productos.append((nombre, precio, cantidad, importe))
    subtotal += importe
    continuar = input("¿Agregar otro producto? (s/n): ").lower()
    if continuar != "s":
        break

# Aplicamos el descuento solo si la compra supera los 100 dólares
descuento = subtotal * 0.10 if subtotal > 100 else 0
total = subtotal - descuento

print("\n===== RESUMEN DE VENTA =====")

# Mostramos cada producto y el total a pagar
for nombre, precio, cantidad, importe in productos:
    print(nombre, "|", cantidad, "x $", f"{precio:.2f}", "= $", f"{importe:.2f}")
print("Subtotal: $", f"{subtotal:.2f}")
print("Descuento: $", f"{descuento:.2f}")
print("Total: $", f"{total:.2f}")
