ldc = []
cost= {}
print("\t\tBIENVENIDO")
print()
def menu_cal():

    print ("Que desea hacer?")
    print ("1. Agregar artículo a la lista.")
    print("2. Eliminar artículo.")
    print("3. Ver Lista.\n(SELECCIONE UN NÚMERO)")
    opcion = int(input("--->"))
   
    return opcion


while True:
    op = menu_cal()
    

    if op == 1 :
        
        lista = []
        art = input("Ingrese el artículo que desea agregar: ").capitalize()
        if art in ldc:
            print("Ese producto ya está en la lista.")
        else:
            lista.append(art)
        ldc.append(lista)

    elif op == 2 :
        art = input("Ingrese el artículo que desea eliminar: ").capitalize()
        if art not in ldc:
            print("Ese artículo no está en su lista.")
        else:
            ldc.remove (art)
        
      

    elif op == 3:
        print("\t\t<><><><><><><><><><><><><><><>")
        print ("\t\t\tLista de compras:")
        print("\t\t<><><><><><><><><><><><><><><>")
        for exp in ldc: 
            print("\t\t-" ,exp[0])
            print("\t\t<><><><><><><><><><><><><><><>")
            
    
    else:
        print("Seleccione una opción correcta")
    
    
            
    
    seguir = input ("Desea seguir (s/n): ")
    if seguir == "n":
        break