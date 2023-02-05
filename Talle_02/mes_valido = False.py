#num = [1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.]
#mes= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


#print(f"1.{p1} \n2.{p2} \n3.{p3}")
mes_valido = False
while not mes_valido : 
    try:
        il = int(input ("Ingrese el mes que inicio a trabajar [1-12]: "))
        pb = int(input("Cada cuanto se paga el bono: "))
        p1 = (pb) + il
        p2 = (pb*2) + il
        p3=  (pb*3) + il

        if p1 >144:
            p1= int(p1-144)
        elif p1 >132 <=144:
            p1=int(p1-132)
        elif p1 >120 <=132:
            p1=int(p1-120)
        elif p1 >108 <=120:
            p1=int(p1-108)
        elif p1 >96 <=108:
            p1=int(p1-96)
        elif p1 >84 <=96:
            p1=int(p1-84)
        elif p1 >72 <=84:
            p1=int(p1-72)
        elif p1 >60 <=72:
            p1=int(p1-60)
        elif p1 >48 <=60:
            p1=int(p1-48)
        elif p1 >36 <=48:
            p1=int(p1-36)
        elif p1 >24 <=36:
            p1=int(p1-24)
        elif p1 >12 <=24:
            p1 =int(p1-12)

        if p2 >144:
            p2= int(p2-144)
        elif p2 >132 <=144:
            p2=int(p2-132)
        elif p2 >120 <=132:
            p2=int(p2-120)
        elif p2 >108 <=120:
            p2=int(p2-108)
        elif p2 >96 <=108:
            p2=int(p2-96)
        elif p2 >84 <=96:
            p2=int(p2-84)
        elif p2 >72 <=84:
            p2=int(p2-72)
        elif p2 >60 <=72:
            p2=int(p2-60)
        elif p2 >48 <=60:
            p2=int(p2-48)
        elif p2 >36 <=48:
            p2=int(p2-36)
        elif p2 >24 <=36:
            p2=int(p2-24)
        elif p2 >12 <=24:
            p2 =int(p2-12)

        if p3 >144:
            p3= int(p3-144)
        elif p3 >132 <=144:
            p3=int(p3-132)
        elif p3 >120 <=132:
            p3=int(p3-120)
        elif p3 >108 <=120:
            p3=int(p3-108)
        elif p3 >96 <=108:
            p3=int(p3-96)
        elif p3 >84 <=96:
            p3=int(p3-84)
        elif p3 >72 <=84:
            p3=int(p3-72)
        elif p3 >60 <=72:
            p3=int(p3-60)
        elif p3 >48 <=60:
            p3=int(p3-48)
        elif p3 >36 <=48:
            p3=int(p3-36)
        elif p3 >24 <=36:
            p3=int(p3-24)
        elif p3 >12 <=24:
            p3 =int(p3-12)
        
        if il >= 1 <=12 :
            mes_valido = True
            
            if p1 == 1: 
                    p1=("Enero")
            elif p1 == 2: 
                    p1=("Febrero")
            elif p1 == 3: 
                    p1=("Marzo")
            elif p1 == 4:
                    p1=("Abril")
            elif p1 == 5:
                    p1=("Mayo")
            elif p1 == 6:
                    p1=("Junio")
            elif p1== 7: 
                    p1=("Julio")
            elif p1 ==8:
                    p1=("Agosto")
            elif p1 ==9:
                    p1=("Septiembre")
            elif p1 ==10:
                    p1=("Octubre")
            elif p1 ==11:
                    p1=("Noviembre")
            elif p1 == 12:
                    p1=("Diciembre")

            if p2 == 1: 
                    p2=("Enero")
            elif p2 == 2: 
                    p2=("Febrero")
            elif p2 == 3: 
                    p2=("Marzo")
            elif p2 == 4:
                    p2=("Abril")
            elif p2 == 5:
                    p2=("Mayo")
            elif p2 == 6:
                    p2=("Junio")
            elif p2 == 7: 
                    p2=("Julio")
            elif p2 ==8:
                    p2=("Agosto")
            elif p2 ==9:
                    p2=("Septiembre")
            elif p2 ==10:
                    p2=("Octubre")
            elif p2 ==11:
                    p2=("Noviembre")
            elif p2 == 12:
                    p2=("Diciembre")

            if p3 == 1: 
                    p3=("Enero")
            elif p3 == 2: 
                    p3=("Febrero")
            elif p3 == 3: 
                    p3=("Marzo")
            elif p3 == 4:
                    p3=("Abril")
            elif p3 == 5:
                    p3=("Mayo")
            elif p3 == 6:
                    p3=("Junio")
            elif p3 == 7: 
                    p3=("Julio")
            elif p3 ==8:
                    p3=("Agosto")
            elif p3 ==9:
                    p3=("Septiembre")
            elif p3 ==10:
                    p3=("Octubre")
            elif p3 ==11:
                    p3=("Noviembre")
            elif p3 == 12:
                    p3=("Diciembre")

        if il == 1: 
            print(f"Usted inicio a trabajar en Enero. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 2: 
            print(f"Usted inicio a trabajar en Febrero. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 3: 
            print(f"Usted inicio a trabajar en Marzo. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 4:
            print(f"Usted inicio a trabajar en Abril. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 5:
            print(f"Usted inicio a trabajar en Mayo. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 6:
            print(f"Usted inicio a trabajar en Junio. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il== 7: 
            print(f"Usted inicio a trabajar en Julio. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==8:
            print(f"Usted inicio a trabajar en Agosto. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==9:
            print(f"Usted inicio a trabajar en Septiembre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==10:
            print(f"Usted inicio a trabajar en Octubre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==11:
            print(f"Usted inicio a trabajar en Noviembre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il== 12:
            print(f"Usted inicio a trabajar en Diciembre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        else: 
            print("Introduzca un número valido.")
    except ValueError: 
        print("ERROR: El mes ingresado debe ser un enetero entre 1-12.")

"""
mes_valido = False
while not mes_valido : 
    try:
        il = int(input ("Ingrese el mes que inicio a trabajar [1-12]: "))
        pb = int(input("Cada cuantos meses se paga el bono: "))
        p1 = (pb) + il
        p2 = (pb*2) + il
        p3=  (pb*3) + il
        
        if p1 >12 :
                p1= int(p1 - 12)
        if p2 >12 :
                p2= int(p2 - 12)
        if p3 >12 :
                p3= int(p3 - 12)
      

        if il >= 1 <=12 :
            mes_valido = True
            
            if p1 == 1: 
                    p1=("Enero")
            elif p1 == 2: 
                    p1=("Febrero")
            elif p1 == 3: 
                    p1=("Marzo")
            elif p1 == 4:
                    p1=("Abril")
            elif p1 == 5:
                    p1=("Mayo")
            elif p1 == 6:
                    p1=("Junio")
            elif p1== 7: 
                    p1=("Julio")
            elif p1 ==8:
                    p1=("Agosto")
            elif p1 ==9:
                    p1=("Septiembre")
            elif p1 ==10:
                    p1=("Octubre")
            elif p1 ==11:
                    p1=("Noviembre")
            elif p1 == 12:
                    p1=("Diciembre")

            if p2 == 1: 
                    p2=("Enero")
            elif p2 == 2: 
                    p2=("Febrero")
            elif p2 == 3: 
                    p2=("Marzo")
            elif p2 == 4:
                    p2=("Abril")
            elif p2 == 5:
                    p2=("Mayo")
            elif p2 == 6:
                    p2=("Junio")
            elif p2 == 7: 
                    p2=("Julio")
            elif p2 ==8:
                    p2=("Agosto")
            elif p2 ==9:
                    p2=("Septiembre")
            elif p2 ==10:
                    p2=("Octubre")
            elif p2 ==11:
                    p2=("Noviembre")
            elif p2 == 12:
                    p2=("Diciembre")

            if p3 == 1: 
                    p3=("Enero")
            elif p3 == 2: 
                    p3=("Febrero")
            elif p3 == 3: 
                    p3=("Marzo")
            elif p3 == 4:
                    p3=("Abril")
            elif p3 == 5:
                    p3=("Mayo")
            elif p3 == 6:
                    p3=("Junio")
            elif p3 == 7: 
                    p3=("Julio")
            elif p3 ==8:
                    p3=("Agosto")
            elif p3 ==9:
                    p3=("Septiembre")
            elif p3 ==10:
                    p3=("Octubre")
            elif p3 ==11:
                    p3=("Noviembre")
            elif p3 == 12:
                    p3=("Diciembre")

        if il == 1: 
            print(f"Usted inicio a trabajar en Enero. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 2: 
            print(f"Usted inicio a trabajar en Febrero. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 3: 
            print(f"Usted inicio a trabajar en Marzo. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 4:
            print(f"Usted inicio a trabajar en Abril. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 5:
            print(f"Usted inicio a trabajar en Mayo. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il == 6:
            print(f"Usted inicio a trabajar en Junio. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il== 7: 
            print(f"Usted inicio a trabajar en Julio. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==8:
            print(f"Usted inicio a trabajar en Agosto. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==9:
            print(f"Usted inicio a trabajar en Septiembre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==10:
            print(f"Usted inicio a trabajar en Octubre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il==11:
            print(f"Usted inicio a trabajar en Noviembre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        elif il== 12:
            print(f"Usted inicio a trabajar en Diciembre. \nEl bono se le pagara en {p1}, {p2}, {p3}")
        else: 
            print("Introduzca un número valido.")
    except ValueError: 
        print("ERROR: El mes ingresado debe ser un enetero entre 1-12.")
    """
