# Registro de cinco calificaciones
# Guardamos las cinco calificaciones en una lista
notas = []
# Seguimos pidiendo notas hasta completar los cinco estudiantes
while len(notas) < 5:
    try:
        nota = float(input("Nota del estudiante " + str(len(notas) + 1) + ": "))
        # Solo aceptamos notas entre 0 y 20
        if 0 <= nota <= 20:
            notas.append(nota)
        else:
            print("La nota debe estar entre 0 y 20.")
    except ValueError:
        print("Escribe una nota numérica.")

acumulado = 0
aprobados = 0
# Calculamos la suma y contamos las notas aprobatorias
for nota in notas:
    acumulado += nota
    if nota >= 14:
        aprobados += 1

# Mostramos los resultados finales
print("Promedio:", round(acumulado / len(notas), 2))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Estudiantes aprobados:", aprobados)
