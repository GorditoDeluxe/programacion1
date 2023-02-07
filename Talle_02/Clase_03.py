
print("Como desea expresar su edad?")
print("1.cadena \n2.meses \n3.años \n4.dias \n5.horas \nFavor introducir el número de su elección entre 1-5.")
op= int(input("Elección: "))

cad = ""
mes = 0
annos = 0.0
dias= 0
horas=0

if op == 1:
    print("Muy bien usted ha seleccionado introducir su edad en cadena, sus opciones son: \n-adulto \n-adolescente \n-niño \n-infante")
    cad= input("Favor escribir la opción que desea elegir, sin - PORFAVOR: ")
    cad_lower= cad.lower()
    if cad_lower == "adulto":
        print("Usted es un adulto, debe dormir 7 horas por noche o más.")
    elif cad_lower == "adolescente":
        print("Usted es un adolescente, los mismos cuentan con un rango de edad entre 13 a 18 años. \nSi su edad es de 13 a 18 años debe dormir entre 8 a 10 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif cad_lower == "niño": 
        print("Ha ingresado que es un niño, los mismos cuentan con un rango de edad entre 6 a 12 años. \nSi el menor entra en ese rango de edad debe dormir de 9 a 12 horas.")
    elif cad_lower == "infante":
         print("Ha introducido la opción infante. \nsi el menor tiene una edad de 1 a 2 años debe dormir de 11 a 14 horas. \nSi el menor tiene una edad de 3 a 5 años debe dormir de 10 a 13 horas. \nSi el infante es menor a 1 año debe dormir de 12 a 16 horas.")
    else:
        print("Introduzca una opción valida.")
elif op == 2:
    mes= int(input("Muy bien usted ha seleccionado introducir su edad en meses, cuantos meses tiene? : "))
    calc = mes/12
    if mes >=228:
        print(f"Usted es un adulto de {calc: .0f} años, debe dormir 7 horas por noche o más.")
    elif mes >=156 <228:
        print(f"Usted es un adolescente de {calc: .0f} años. \nSi su edad es de 13 a 18 años debe dormir entre 8 a 10 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif mes >=72 <156:
        print(f"Ha ingresado que es un niño de {calc: .0f} años. \nSi el menor entra en rango de edad de 6 a 12 años debe dormir de 9 a 12 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif mes >=12 <=24:
        print(f"Ha ingresado que es un infante de {calc: .0f} años. \nSi tiene 1 o 2 años debe dormir de 11 a 14 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif mes >=36 <72:
        print(f"Ha ingresado que es un niño de {calc: .0f} años. \nSi el menor entra en rango de edad de 3 a 5 años debe dormir de 10 a 13 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif mes < 12:
        print(f"Ha ingresado que es un infante de {mes} meses.\nSi tiene menos de 1 año debe dormir de 12 a 16 horas.\nSi no entra en ese rango favor vuelva al menu de opciones.")
elif op == 3:
    annos= float(input("Muy bien usted ha seleccionado introducir su edad en años, cuantos años tiene? :"))
    if annos >=19:
        print("Usted es un adulto, debe dormir 7 horas por noche o más.")
    elif annos >=13 <19:
        print("Usted es un adolescente.\nSi su edad es de 13 a 18 años debe dormir entre 8 a 10 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif annos >=6 <13:
        print("Ha ingresado que es un niño, los mismos cuentan con un rango de edad entre 6 a 12 años. \nSi el menor entra en ese rango de edad debe dormir de 9 a 12 horas.")
    elif annos >=1 <=2:
        print("debe dormir de 11 a 14 horas.")
    elif annos >=3 <6:
        print("debe dormir de 10 a 13 horas.")
    elif annos < 1:
        print("debe dormir de 12 a 16 horas.")
elif op == 4:
    dias= int(input("Muy bien usted ha seleccionado introducir su edad en días. \nRecuerde que un año en días son 365 días. \nporfavor ingrese el número sin puntos o comas. \nTeniendo eso en cuenta, cuantos días tiene? : "))
    calc = dias/365
    if dias >=6935:
        print(f"Usted es un adulto de {calc: .0f} años, debe dormir 7 horas por noche o más.")
    elif dias >=4745 <6935:
        print(f"Usted es un adolescente de {calc: .0f} años. \nSi su edad es de 13 a 18 años debe dormir entre 8 a 10 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif dias >=2190 <4745:
        print(f"Ha ingresado que es un niño de {calc: .0f} años. \nSi el menor entra en rango de edad de 6 a 12 años debe dormir de 9 a 12 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif dias >=365 <=730:
        print(f"Ha ingresado que es un infante de {calc: .0f} años. \nSi tiene 1 o 2 años debe dormir de 11 a 14 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif dias >=1095 <2190:
        print(f"Ha ingresado que es un niño de {calc: .0f} años. \nSi el menor entra en rango de edad de 3 a 5 años debe dormir de 10 a 13 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif dias < 365:
        print(f"Ha ingresado que es un infante de meses.\nSi tiene menos de 1 año debe dormir de 12 a 16 horas.\nSi no entra en ese rango favor vuelva al menu de opciones.")
elif op == 5:
    horas= int(input("Muy bien usted ha seleccionado introducir su edad en horas. \nRecuerde que un año en horas son 8760 horas.\nporfavor ingrese el número sin puntos o comas. \nTeniendo esto en cuenta, cuantas horas tiene? : "))
    calc = horas/8760
    if horas >=166440:
        print(f"Usted es un adulto de {calc: .0f} años, debe dormir 7 horas por noche o más.")
    elif horas >=113880 <166440:
        print(f"Usted es un adolescente de {calc: .0f} años. \nSi su edad es de 13 a 18 años debe dormir entre 8 a 10 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif horas >=52560 <113880:
        print(f"Ha ingresado que es un niño de {calc: .0f} años. \nSi el menor entra en rango de edad de 6 a 12 años debe dormir de 9 a 12 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif horas >=8760 <=17520:
        print(f"Ha ingresado que es un infante de {calc: .0f} años. \nSi tiene 1 o 2 años debe dormir de 11 a 14 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif horas >=26280 <52560:
        print(f"Ha ingresado que es un niño de {calc: .0f} años. \nSi el menor entra en rango de edad de 3 a 5 años debe dormir de 10 a 13 horas. \nSi no entra en ese rango favor vuelva al menu de opciones.")
    elif horas < 8760:
        print(f"Ha ingresado que es un infante de meses.\nSi tiene menos de 1 año debe dormir de 12 a 16 horas.\nSi no entra en ese rango favor vuelva al menu de opciones.")

      





























