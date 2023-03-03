lista_exp = []
exp_p = 0
exp_ec = 0
exp_c = 0
estados =("pendiente", "en curso", "Cerrado")
print("Bienvenido")
def menu_cal():

    print ("Que desea hacer?")
    print ("1. Agregar Expediente.")
    print ("2. Expedientes pendientes.")
    print ("3. Expedientes en curso.")
    print ("4. Expedientes cerrados.")
    print("5. expedientes")
    opcion = input("--->")
   
    return opcion


while True:
    op = menu_cal()
    

    if op == "1" :
        
        lista = []
        id = input("Ingrese ID del expediente: ")
        lista.append(id)
        cond = input("Ingrese el conductor: ")
        lista.append(cond)
        aseg = input("Ingrese la aseguradora: ")
        lista.append(aseg)
        num_case = input("Ingrese el número de caso: ")
        lista.append(num_case)
        est = int(input("Ingrese el tipo de proceso:\n1. Pendiente.\n2. En curso. \n3. Cerrados.\n---> "))
        if est == 1:
            exp_p = (exp_p +1)
        elif est == 2:
            exp_ec = (exp_ec +1)
        elif est == 3:
            exp_c = (exp_c +1)
        lista.append(est)
        lista_exp.append(lista)
        
      

    elif op == "2" :
        print(f"{exp_p}")
    elif op == "3" :
        print(f"{exp_ec}")
    elif op == "4" :
        print(f"{exp_c}")
    elif op == "5":
        print ("Expedientes:" ,lista_exp)
        for exp in lista_exp: 
            print("\t\tExpediente #: " ,exp[0])
            print("Conductor: ", exp[1])
            print("Aseguradora: ", exp[2])
            print("Número de caso: ", exp[3])
            valor = exp[4] - 1 
            print("Tipo de expediente: ", estados[valor])

    


    seguir = input ("Desea seguir (s/n): ")
    if seguir == "n":
        break