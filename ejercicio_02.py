# Clasificación de edades
try:
    edad = int(input("Ingresa tu edad: "))
    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad < 12:
        print("Categoría: niño")
    elif edad <= 17:
        print("Categoría: adolescente")
    elif edad <= 64:
        print("Categoría: adulto")
    else:
        print("Categoría: adulto mayor")
except ValueError:
    print("Escribe una edad en números enteros.")
