wl = []
print("\t\tBIENVENIDO")
print()
def menu_cal():

    print ("Que desea hacer?")
    print ("1. Agregar artículo a la lista de deseos.")
    print("2. Eliminar artículo.")
    print("3. Ver WishList.\n(SELECCIONE UN NÚMERO)")
    opcion = int(input("--->"))
   
    return opcion


while True:
    op = menu_cal()
    

    if op == 1 :
        
        lista = []
        art = input("Ingrese el artículo que desea agregar: ").capitalize()
        if art in wl:
            print("Ese producto ya está en la lista.")
        else:
            lista.append(art)
        cost = float(input("Ingrese el precio: "))
        lista.append(cost)
        wl.append(lista)

    elif op == 2 :
        art = input("Ingrese el artículo que desea eliminar: ").capitalize()
        if art not in wl:
            print("Ese artículo no está en su lista.")
        else:
            wl.remove (art)
        
      

    elif op == 3:
        print("\t\t<><><><><><><><><><><><><><><>")
        print ("\t\t\t  WISHLIST:")
        print("\t\t<><><><><><><><><><><><><><><>")
        for exp in wl: 
            print("\t\tArtículo: " ,exp[0])
            print("\t\tPrecio: ", exp[1])
            print("\t\t<><><><><><><><><><><><><><><>")
            
    
    else:
        print("Seleccione una opción correcta")
    
    
            
    
    seguir = input ("Desea seguir (s/n): ")
    if seguir == "n":
        break