Carrito = []
print("\t\tBIENVENIDO")
print()
def menu_cal():

    print ("Que desea hacer?")
    print ("1. Agregar artículo al carrito.")
    print("2. Eliminar artículo.")
    print("3. Ver carrito.\n(SELECCIONE UN NÚMERO)")
    opcion = int(input("--->"))
   
    return opcion


while True:
    op = menu_cal()
    

    if op == 1 :
        
        lista = []
        art = input("Ingrese el artículo que desea agregar: ").capitalize()
        if art in Carrito:
            print("Ese producto ya está en la lista.")
        else:
            lista.append(art)
        cost = float(input("Ingrese el precio: "))
        lista.append(cost)
        Carrito.append(lista)

    elif op == 2 :
        art = input("Ingrese el artículo que desea eliminar: ").capitalize()
        if art not in Carrito:
            print("Ese artículo no está en su lista.")
        else:
            Carrito.remove (art)
        
      

    elif op == 3:
        print("\t\t<><><><><><><><><><><><><><><>")
        print ("\t\t\t    CARRITO:")
        print("\t\t<><><><><><><><><><><><><><><>")
        for exp in Carrito: 
            print("\t\t-" ,exp[0])
            print("\t\tPrecio: ", exp[1])
            print("\t\t<><><><><><><><><><><><><><><>")
            
    
    else:
        print("Seleccione una opción correcta")
    
    
            
    
    seguir = input ("Desea seguir (s/n): ")
    if seguir == "n":
        break
    