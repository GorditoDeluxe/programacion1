print("\t\tBIENVENIDO A LA PLATAFORMA DE NOTAS")
nom = input("Ingrese el nombre del alumno: \n--->")
ape = input("Ingrese el apellido del alumno: \n--->")
n1 = float(input("Ingrese la calificacion 1.\n---> "))
n2 = float(input("Ingrese la calificacion 2.\n---> "))
n3 = float(input("Ingrese la calificacion 3.\n---> "))
n4 = float(input("Ingrese la calificacion 4.\n---> "))
prom = ((n1 + n2 + n3 + n4 )/4)


print("\t\tRESULTADO FINAL")
print(f"Nombre: {nom}\nApellido: {ape}\nCalificación 1: {n1}\nCalificación 2: {n2}\nCalificación 3: {n3}\nCalificación 4: {n4}\nResultado: {prom}")

if prom >= 71:
    print(f"El estudiante ha aprovado la materia con {prom: .2f}.")
else:
    print(f"El estudiante ha fracasado con {prom: .2f}.")
