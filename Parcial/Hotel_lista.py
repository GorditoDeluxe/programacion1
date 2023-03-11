lista_hotel = []

habi=("none","Basica", "Doble", "Suite", "Doble con vista al mar ", "Presidencial")
print("BIENVENIDO AL HOTEL GUAMÚCHIL")
def menu_cal():

    print ("En que le podemos ayudar?")
    print ("1. Ingresar información de huesped.")
    print ("2. Consultar información de huesped.")
    print ("3. salir del sistema.")

    opcion = input("--->")
   
    return opcion


while True:
    op = menu_cal()
    

    if op == "1" :
        
        lista = []
        nom = input("Ingrese Nombre del huesped: ")
        lista.append(nom)
        ape = input("Ingrese el apellido del huesped: ")
        lista.append(ape)
        edad = input("Ingrese la edad del huesped: ")
        lista.append(edad)
        dias = int(input("Ingrese la cantidad de días: "))
        lista.append(dias)
        hab = int(input("Ingrese el tipo de habitación que desea:\n1. Basica.\n2. Doble. \n3. Suite.\n4.Doble con vista al mar.\n5.Presidencial\n---> "))
        if hab == 1:
            cost= 120.00
            costfin = (cost * dias )
            print(f"Usted desea se desea hospedar en la habitación basica la cual tiene un costo de {cost: .2f} por noche.")
            if dias >5 <11: 
                desc= (costfin - (costfin * 0.10))
                pago = desc
                print(f"Por hospedarse más de 5 días recibe un descuento del 10% y el total le quedaría en: {pago: .2f}")
            elif dias >10 <16: 
                desc= (costfin - (costfin * 0.15)) 
                pago = desc
                print(f"Por hospedarse más de 10 días recibe un descuento del 15% y el total le quedaría en: {pago: .2f}")
            elif dias >15: 
                desc= (costfin - (costfin * 0.20)) 
                pago = desc
                print(f"Por hospedarse más de 15 días recibe un descuento del 20% y el total le quedaría en: {pago: .2f}")
            else:
                pago = costfin
                print(f"Usted se hospedara {dias} días, el total a pagar es de: {pago}")

        elif hab == 2:
            cost= 155.00
            costfin = (cost * dias )
            print(f"Usted desea se desea hospedar en la habitación doble la cual tiene un costo de {cost: .2f} por noche.")
            if dias >5 <11: 
                desc= (costfin - (costfin * 0.10)) 
                pago = desc
                print(f"Por hospedarse más de 5 días recibe un descuento del 10% y el total le quedaría en: {pago: .2f}")
            elif dias >10 <16: 
                desc= (costfin - (costfin * 0.15))
                pago = desc
                print(f"Por hospedarse más de 10 días recibe un descuento del 15% y el total le quedaría en: {pago: .2f}")
            elif dias >15: 
                desc= (costfin - (costfin * 0.20))
                pago = desc
                print(f"Por hospedarse más de 15 días recibe un descuento del 20% y el total le quedaría en: {pago: .2f}")
            else:
                pago = costfin
                print(f"Usted se hospedara {dias} días, el total a pagar es de: {pago}")

        elif hab == 3:
            cost= 210.00
            costfin = (cost * dias )
            print(f"Usted desea se desea hospedar en la Suite la cual tiene un costo de {cost: .2f} por noche.")
            if dias >5 <11: 
                desc = (costfin - (costfin * 0.10)) 
                pago = desc
                print(f"Por hospedarse más de 5 días recibe un descuento del 10% y el total le quedaría en: {pago: .2f}")
            elif dias >10 <16: 
                desc= (costfin - (costfin * 0.15)) 
                pago = desc
                print(f"Por hospedarse más de 10 días recibe un descuento del 15% y el total le quedaría en: {pago: .2f}")
            elif dias >15: 
                desc= (costfin - (costfin * 0.20)) 
                pago = desc
                print(f"Por hospedarse más de 15 días recibe un descuento del 20% y el total le quedaría en: {pago: .2f}")
            else:
                pago = costfin
                print(f"Usted se hospedara {dias} días, el total a pagar es de: {pago}")
            
        elif hab == 4:
            cost= 185.00
            costfin = (cost * dias )
            print(f"Usted desea se desea hospedar en la habitación doble con vista al mar la cual tiene un costo de {cost: .2f} por noche.")
            if dias >5 <11: 
                desc= (costfin - (costfin * 0.10)) 
                pago = desc
                print(f"Por hospedarse más de 5 días recibe un descuento del 10% y el total le quedaría en: {pago: .2f}")
            elif dias >10 <16: 
                desc= (costfin - (costfin * 0.15)) 
                pago = desc
                print(f"Por hospedarse más de 10 días recibe un descuento del 15% y el total le quedaría en: {pago: .2f}")
            elif dias >15: 
                desc= (costfin - (costfin * 0.20))
                pago = desc
                print(f"Por hospedarse más de 15 días recibe un descuento del 20% y el total le quedaría en: {pago: .2f}")
            else:
                pago = costfin
                print(f"Usted se hospedara {dias} días, el total a pagar es de: {pago}")

        elif hab == 5:
            cost= 400.00
            costfin = float((cost * dias))
            print(f"Usted desea se desea hospedar en la habitación presidencial la cual tiene un costo de {cost: .2f} por noche.")
            if dias >5 <11: 
                desc= (costfin - (costfin * 0.10)) 
                pago = desc
                print(f"Por hospedarse más de 5 días recibe un descuento del 10% y el total le quedaría en: {pago: .2f}")
            elif dias >10 <16: 
                desc= (costfin - (costfin * 0.15)) 
                pago = desc
                print(f"Por hospedarse más de 10 días recibe un descuento del 15% y el total le quedaría en: {pago: .2f}")
            elif dias >15: 
                desc= (costfin - (costfin * 0.20))
                pago = desc
                print(f"Por hospedarse más de 15 días recibe un descuento del 20% y el total le quedaría en: {pago: .2f}")
                
            else:
                pago = costfin
                print(f"Usted se hospedara {dias} días, el total a pagar es de: {pago}")
                
        lista.append(hab)
        lista_hotel.append(lista)
        
      

   
    elif op == "2":
        print ("Datos:" ,lista_hotel)
        for hotel in lista_hotel: 
            print("\t\tHUESPED ")
            print("Nombre: ", hotel[0])
            print("Apellido: ", hotel[1])
            print("Edad: ", hotel[2])
            print("Cantidad de días: ", hotel[3])
            valor = hotel[4]
            print("Tipo de habitación: ", habi[valor])
            print(f"el costo por noche es de: {cost}")
            print(f"El subtotal es de: {costfin}")
            print(f"El total a pagar es de: {pago} ")

    

    elif op == "3":
        salir = input("Si desea salir del programa escriba: parcial#1. \n(escribir tal cual se ve o no funcionara la opción)---> ")
        if salir == "parcial#1": 
            break
    
    seguir = input ("Desea seguir (s/n): ")
    if seguir == "n":
        break