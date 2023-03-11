
print("\t\tBienvenido a su calculadora de terreno.")
tierra = int(input("Como es el terreno?\n1.Cuadrado.\n2.Rectangular\n(Seleccione un número)---> "))
if tierra == 1:
    tierra = "Cuadrado"
elif tierra == 2:
    tierra = "Rectangular"
else:
    print("Seleccione una opción valida.")
metrosA = float(input("Cuantos metros de largo tiene el terreno? \n(Ingrese aquí la cantidad de metros en números)--->"))
metrosL = float(input("Cuantos metros de ancho tiene el terreno? \n(Ingrese aquí la cantidad de metros en números)--->"))
costo = float(input("A cuanto está el metro cuadrado en el area?\n--->"))
totalm = (metrosL * metrosA)
costfin = (totalm * costo)


print(f"\t\t RESULTADO FINAL\nLa tierra es: {tierra}.\ntiene {totalm} metros cuadrados.\nTiene un costo total de: {costfin}")