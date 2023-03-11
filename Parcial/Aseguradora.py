lista_exp = []
exp_p = 0
exp_ec = 0
exp_c = 0
estados =("pendiente", "en curso", "Cerrado")
print("BIENVENIDO AL MENÚ PRINCIPAL\nAquí tendra las opciones de registrar los expedientes o poder ver la lista de los que ya existen. ")
def menu_cal():

    print ("\t\tQue desea hacer?")
    print ("1. Agregar Expediente.")
    print ("2. Expedientes pendientes.")
    print ("3. Expedientes en curso.")
    print ("4. Expedientes cerrados.")
    print("5. Ver expedientes")
    print("6. Configuración.")
    print("7. Salir.\nHecho por Abraham Btesh ;D")
    opcion = input("--->")
   
    return opcion


while True:
    op = menu_cal()
    

    if op == "1" :
        
        lista = []
        juzg = input("Ingrese el juzgado: ")
        lista.append(juzg)
        cond = input("Ingrese el nombre del cliente (apellido incluido por favor): ")
        lista.append(cond)
        aseg = input("Ingrese la aseguradora: ")
        lista.append(aseg)
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
            print("Juzgado: " ,exp[0])
            print("Cliente: ", exp[1])
            print("Aseguradora: ", exp[2])
            valor = exp[3] - 1 
            print("Tipo de expediente: ", estados[valor])
    elif op == "6":
        print("\t\t BIENVENIDO A CONFIGURACIONES\nAqui podra ver las aseguradoras, clientes y juzgados registrados.\n1.Aseguradora.\n2.Cliente\n3.Juzgado.\nHecho por Abraham Btesh.")
        sub = int(input("(ingrese el número de la opción que desea seleccionar.)--> "))
        if sub == 1:
            print("aseguradoras:")
            for exp in lista_exp: 
             print("-",exp[2])
        elif sub == 2:
            print("Clientes: ")
            for exp in lista_exp: 
             print( "-",exp[1])
        elif sub == 3:
            print ("Juzgados: ")
            for exp in lista_exp: 
             print("-",exp[0])
    elif op == "7": 
        salir = input("Si desea salir del programa escriba el número: 100\n(Escribirlo igual o el programa no lo va tomar en cuenta.)--->")
        if salir == "100":
            break

    

    seguir = input ("Desea seguir (s/n): ")
    if seguir == "n":
        break