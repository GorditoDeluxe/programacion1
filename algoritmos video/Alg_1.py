"""Que puedes inventar?
necesitas 5 problemas relacionados al video, de que trataba el video?
sobre como amazon recopila y almacena información de todo lo que buscamos 
y vemos dentro de la pagina
nombre:
has comprado? : si o no
si: categorias 
    recomendarias nuestra sección de "cat"? si o no
        que tal fue tu experiencia con nosotros? buena: le gustaria detallar?, mala: le gustaria detallar? 

no: xq
"""

nom= input("Hola! como te llamas?: ")
sex= input("Cual es tu genero: ")
edad= input("Cuantos años tienes? \n(Favor expresar su edad en números): ")

if edad == int:
    edad = edad
elif edad != int:
    edad = print("Usted no ha expresado su edad en números.")
    
print(f"\n{nom}, que te gustaria hacer?")
sele= int(input("1. Dejar un comentario. \n2. Saber sobre nosotros. \n3. Cupones de descuento. \n(SElELECCIONE EL NÚMERO): "))


if sele == 1:
    comp= int(input("\nHas comprado aquí alguna vez? \n1. Primera vez.\n2. Si.\n3. No. \n(SElELECCIONE EL NÚMERO): "))

    if comp == 2: 

        rec: int(input("\nQue bueno, recomendarias nuestros servicios? \n1. Si. \n2. No.  \n(SElELECCIONE EL NÚMERO): "))
        if rec == 1: 

            op1= int(input("\nNos alegra saber eso, nos gustaría que dejaras tu opinión? \n1. Si.\n2. No. \n(SElELECCIONE EL NÚMERO): "))
            if op1 == 2:
                print(f"Entendido, {nom} muchas gracias por tener en mente recomendarnos.")
            else: 
                input("(Escriba aqui): ")
                print(f"{nom}, muchas gracias por dejar tu comentario, esto nos ayuda\na poder mejorar constantemente.")

        elif rec == 2: 
           
            op2= int(input("Nos sentimos mal al escuchar eso, te gustaría\ndejar un comentario para ayudarnos a mejorar? \n1. Si. \n 2. No. \n(SElELECCIONE EL NÚMERO): "))
            if op2 == 2:
               print(f"Lamentamos mucho eso {nom}")
            else:
                input("(Escriba aqui): ")
                print(f"{nom}, muchas gracias por dejar tu comentario, esto nos ayuda\na poder mejorar constantemente y lamentamos el inconveniente.")
               

    elif comp == 3:
        print(f"Sobre nosotros: https://www.amazon.es/Acerca-Amazon-Descubre-Nuestra-Empresa-Nuestra-Tecnologia/b?ie=UTF8&node=1323175031 \n{nom}, te invitamos a visitar el enlace para tener un poco más de información sobre nuestra empresa.")
        

    elif comp == 1:

        exp= int(input(f"Gracias {nom} por confiar en nosotros, nos gustaria saber que tal fue tu experiencia en tu priemra compra: \n1. Buena\n2. Mala \n(SELECCIONE EL NÚMERO): "))
        if exp == 1:
           
            be= int(input(f"Excelente!, {nom} te gustaría relatarnos tu experiencia?\n1.Si\n2.No\n(SELECCIONE EL NÚMERO): "))
            if be == 1:
                input("(escriba aquí): ")
                print("Nos alegra que tu primera compra fuera buena,vuelve a visitarnos pronto\ny recomiendanos con tus amigos. \npor ser la primera compra tendras un descuento del 10% en la siguiente\ny por cada amigo que se registre recibirás un premio :D.")
            elif be == 2:
                print(f"{nom}, para nosotros es muy importante la opinión de nuestros clientes y nos alegra\nsaber que tu experiencia fue buena,vuelve a visitarnos pronto y recomiendanos con tus amigos. \npor ser la primera compra tendras un descuento del 10% en la siguiente\ny por cada amigo que se registre recibirás un premio :D.") 
        
        elif exp == 2:   
           
            me= int(input("Rayos!, Lamentamos que tu primera compra no saliera como esperabas,\nnos ayudaria mucho saber como podemos solucionar eso. \nTe gustaría relatar porque tuviste una mala experiencia en tu primera compra?: \n1. Si.\n2. No.  "))
            if me == 1:
                input("(Favor explique acontinuación): ")
                print(f"{nom}, para nosotros es muy importante la opinión de nuestros clientes y lamentamos \nsu disgusto, haremos lo posible para solucionarlo cuanto antes.")
            elif me ==2: 
                print(f"{nom} lamentamos su disgusto, por ser la primera vez tedrá un descuento del 20%\nen su siguiente compra, le pedimos una segunda oportunidad.\nNo lo vamos a defraudar ;D")

elif sele == 2:
    print(f"Sobre nosotros: https://www.amazon.es/Acerca-Amazon-Descubre-Nuestra-Empresa-Nuestra-Tecnologia/b?ie=UTF8&node=1323175031 \n{nom}, te invitamos a visitar el enlace para tener un poco más de información sobre nuestra empresa.")

elif sele == 3:
    cat= int(input("Que categoria tienes?\n1. Comprador primerizo.\n2. comprador frecuente.\n--->"))
    if cat == 1:
        reg= int(input("Cuantos amigos se han registrado: "))
        print(f"se han registrado {reg} amigos, cada amigo te da un 5% de descuento, por lo tanto\ntienes {reg * 4}% de descuento para un artículo de tu preferencia.")
    elif cat == 2:
        reg= int(input("Cuantos amigos se han registrado: "))
        print(f"Se han registrado {reg} amigos, cada amigo te da un 3% de descuento, por lo tanto\ntienes {reg * 5}% de descuento para un artículo de tu preferencia.")



db =input(f"\nMuy bien, para finalizar {nom}, nos gustaria saber si quieres dejar registrada la siguiente información: \n-Nombre del cliente: {nom}.\n-Edad: {edad}.\n-Categoria: {sele}.\n-Genero: {sex}.\n\n1. Si. \n2. No\n(SELECCIONE UN NÚMERO): ")
if db == 1:
    print(f"Excelente, vuelve a visitarnos pronto {nom}. ;)")
if db == 2: 
    print("Entendido, los datos serán borrados.")

    
