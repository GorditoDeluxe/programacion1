users = {'user1': 'password1'}

def login():
    while True:
        username = input('Ingresa tu nombre de usuario: ')
        password = input('Ingresa tu contraseña: ')
        
        if username in users and users[username] == password:
            print('Inicio de sesión exitoso')
            return username
        else:
            print('Credenciales incorrectas. Por favor, intenta de nuevo o regístrate.')
            choice = input('¿Deseas registrarte? (s/n): ')
            if choice.lower() == 's':
                register()
            else:
                continue

def register():
    while True:
        new_username = input('Ingresa un nombre de usuario: ')
        if new_username in users:
            print('Este usuario ya existe. Por favor, intenta de nuevo.')
            continue
        else:
            new_password = input('Ingresa una contraseña: ')
            users[new_username] = new_password
            print('Registro exitoso')
            login()
            return

username = login()

    
class Producto:
    def __init__(self, nombre, precio, cantidad, usuario):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.usuario = usuario

productos_en_venta = []

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = float(input("Ingrese la cantidad de productos en venta: "))
    usuario = input("Ingrese su nombre de usuario: ")
    producto = Producto(nombre, precio, cantidad, usuario)
    productos_en_venta.append(producto)
    print(f"Producto '{nombre}' agregado a la lista de venta.")
    
def modificar_producto():
    print("Lista de productos en venta:")
    for i, producto in enumerate(productos_en_venta):
        print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")
    opcion = int(input("Seleccione el número del producto a modificar: "))
    producto = productos_en_venta[opcion-1]
    print(f"Producto seleccionado: {producto.nombre} - Precio actual: {producto.precio} - Cantidad actual: {producto.cantidad}")
    opcion_modificar = int(input("Seleccione la opción a modificar:\n1. Precio\n2. Cantidad\n"))
    if opcion_modificar == 1:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        producto.precio = nuevo_precio
        print(f"Precio del producto '{producto.nombre}' modificado a {nuevo_precio}.")
    elif opcion_modificar == 2:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        producto.cantidad = nueva_cantidad
        print(f"Cantidad del producto '{producto.nombre}' modificada a {nueva_cantidad}.")
    else:
        print("Opción inválida.")
    
def eliminar_producto_en_venta():
    if len(productos_en_venta) == 0:
        print("No hay productos en la lista de venta.")
        return
    for i, producto in enumerate(productos_en_venta):
        print(f"{i+1}. {producto.nombre} ({producto.cantidad} disponibles) - ${producto.precio}")
    opcion = int(input("Seleccione el número del producto a eliminar de la lista: "))
    producto = productos_en_venta[opcion-1]
    del productos_en_venta[opcion-1]
    print(f"Producto '{producto.nombre}' eliminado de la lista de venta. Jo pa' diablo, no querei plata")
        
class Carrito:
    def __init__(self):
        self.items = []
    
    def agregar_producto(self, producto, cantidad):
        item = {"producto": producto, "cantidad": cantidad}
        self.items.append(item)
    
    def eliminar_producto(self, index):
        del self.items[index]
    
    def listar_carrito(self):
        total = 0
        print("Carrito de compra:")
        for i, item in enumerate(self.items):
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal = cantidad * producto.precio
            total += subtotal
            print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {cantidad} - Subtotal: {subtotal}")
        print(f"Total: {total}")
        if len(self.items) == 0:
            print("El carrito de compra está vacío.")

carrito = Carrito()

def listar_productos_venta():
    print("Productos en venta:")
    for i, producto in enumerate(productos_en_venta):
        print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad} - Vendedor: {producto.usuario}")
    if len(productos_en_venta) == 0:
        print("No hay productos en venta.")

def listar_productos_compra():
    print("Productos en venta:")
    for i, producto in enumerate(productos_en_venta):
        print(f"{i+1}. {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad} - Vendedor: {producto.usuario}")
    if len(productos_en_venta) == 0:
        print("No hay productos en venta. Mirá, la gente si es perezosa eto.")

def agregar_al_carrito():
    listar_productos_compra()
    opcion = int(input("Seleccione el número del producto a agregar al carrito: "))
    producto = productos_en_venta[opcion-1]
    cantidad = int(input("Ingrese la cantidad a agregar al carrito: "))
    if cantidad <= producto.cantidad:
        carrito.agregar_producto(producto, cantidad)
        print(f"{cantidad} '{producto.nombre}' agregados al carrito.")
        producto.cantidad -= cantidad
        if producto.cantidad == 0:
            productos_en_venta.remove(producto)
    else:
        print("La cantidad solicitada excede el stock disponible. (No sea lagartoo, los demás deben comer)")

def modificar_carrito():
    carrito.listar_carrito()
    opcion = int(input("Seleccione el número del producto a modificar: "))
    item = carrito.items[opcion-1]
    producto = item["producto"]
    cantidad_actual = item["cantidad"]
    cantidad_nueva = int(input(f"Ingrese la nueva cantidad para '{producto.nombre}' (actual: {cantidad_actual}): "))
    if cantidad_nueva <= producto.cantidad + cantidad_actual:
        cantidad_agregada = cantidad_nueva - cantidad_actual
        if cantidad_agregada > 0:
            if cantidad_agregada <= producto.cantidad:
                item["cantidad"] = cantidad_nueva
                producto.cantidad += cantidad_actual - cantidad_nueva
                print(f"{cantidad_agregada} '{producto.nombre}' agregados al carrito.")
            else:
                print("La cantidad solicitada excede el stock disponible. (No sea lagartoo, los demás deben comer)")
        elif cantidad_agregada < 0:
            item["cantidad"] = cantidad_nueva
            producto.cantidad += cantidad_actual - cantidad_nueva
            print(f"{-cantidad_agregada} '{producto.nombre}' eliminados del carrito.")
        else:
            print(f"No se realizaron cambios para '{producto.nombre}'.")
    else:
        print("La cantidad solicitada excede el stock disponible.")

def eliminar_del_carrito():
    carrito.listar_carrito()
    opcion = int(input("Seleccione el número del producto a eliminar del carrito: "))
    item = carrito.items[opcion-1]
    producto = item["producto"]
    cantidad = item["cantidad"]
    producto.cantidad += cantidad
    carrito.eliminar_producto(opcion-1)
    print(f"{cantidad} '{producto.nombre}' eliminados del carrito.")

def realizar_compra():
    carrito.listar_carrito()
    confirmacion = input("¿Desea confirmar la compra? (S/N)").upper()
    if confirmacion == "S":
        print("Compra realizada exitosamente. Usted si sabe meeto, ojuaa vuelva pronto")
        carrito.items = []
    else:
        print("Compra cancelada.  No solo de pan vive eL hombre. Compre legumbres mano.")

def ingresar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    email = input("Ingrese su correo electrónico: ")
    datos_usuario = {"nombre": nombre, "edad": edad, "email": email}
    return datos_usuario
usuarios = []
usuarios.append(ingresar_datos())

while True:
    print("----- MENÚ PRINCIPAL -----")
    
    print("1. Ventas")
    print("2. Compras")
    print("3. carrito")
    print("4. imprimir perfil")
    print("5. Sobre nosotros")
    print("6. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        op = int(input("\t\tModulo de venta\nopciones:\n1. Agregar producto\n2. Lista de productos.\n3. Eliminar producto.\n4. Modificar producto.\nSeleccione un número --> "))
        if op ==1:
            agregar_producto()
        elif op == 2:
            listar_productos_venta()
        elif op == 3:
            eliminar_producto_en_venta()
        elif op == 4:
            modificar_producto()
        else:
            print("La cabeza no es solo pal' sombrero, lea bien.")
    
    elif opcion == 2:
        op = int(input("\t\tModulo de compra\nopciones:\n1. Agregar producto al carrito. \n2. Lista de compra.\n3. Modificar carrito.\n4. eliminar producto del carrito.\nSeleccione un número --> "))
        if op ==1:
            agregar_al_carrito()
        elif op == 2:
            carrito.listar_carrito()
        elif op == 3:
            modificar_carrito()
        elif op == 4:
            eliminar_del_carrito()
        else:
            print("La cabeza no es solo pal' sombrero, lea bien.")
    
    elif opcion == 3:
        op= int(input("\t\tCarrito de compras\nOpciones:\n1. Pagar.\nSeleccione un número -->"))
        if op == 1:
            realizar_compra()
        else:
            print("La cabeza no es solo pal' sombrero, lea bien.")
        
    elif opcion ==4:
        for usuario in usuarios:
            print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Email: {usuario['email']}")
    
    elif opcion == 5:
        print("\t\t\tFarmFinder\nFarmFinder es una aplicación diseñada para facilitar la compra y venta al por mayor de productos agrícolas,\ntales como frutas, legumbres, entre otros. La aplicación tiene como objetivo principal\npromover la producción nacional y disminuir la compra de productos extranjeros\nen los supermercados y mercados, ofreciendo una plataforma para que los agricultores y proveedores\nde alimentos puedan conectarse directamente con los compradores al por mayor.\nEsto permite que los agricultores obtengan mejores precios para sus productos y\nque los compradores al por mayor obtengan productos frescos y de alta calidad directamente del campo.\nEn resumen, FarmFinder busca mejorar la cadena de suministro de productos agrícolas en el país y apoyar la producción nacional.")
        
    elif opcion == 6:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.(La cabeza no es solo pal' sombrero, lea bien.)")
