# Registro de cinco calificaciones
notas = []
while len(notas) < 5:
    try:
        nota = float(input("Nota del estudiante " + str(len(notas) + 1) + ": "))
        if 0 <= nota <= 20:
            notas.append(nota)
        else:
            print("La nota debe estar entre 0 y 20.")
    except ValueError:
        print("Escribe una nota numérica.")

acumulado = 0
aprobados = 0
for nota in notas:
    acumulado += nota
    if nota >= 14:
        aprobados += 1

print("Promedio:", round(acumulado / len(notas), 2))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Estudiantes aprobados:", aprobados)
