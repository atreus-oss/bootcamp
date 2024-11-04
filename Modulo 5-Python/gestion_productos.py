productos = []


def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")

    if precio or cantidad:
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            print("Por favor, ingrese valores numéricos para el precio y la cantidad.")
            return
    else:
        return

    producto = {
        'nombre': nombre,
        'precio': float(precio),
        'cantidad': int(cantidad)
    }

    productos.append(producto)
    print(f"El producto '{nombre}' se añadió con éxito.")



def ver_productos():
    if not productos:
        print("No hay productos en la lista.")
        return

    print("Lista de productos:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")


def actualizar_producto():
    ver_productos()
    if not productos:
        return

    indice = int(input("Introduce el número del producto a actualizar: ")) - 1
    if 0 <= indice < len(productos):
        print("(Si no desea cambiar algún campo, déjelo en blanco)")
        nombre = input("Ingrese el nuevo nombre del producto: ")
        precio = input("Ingrese el nuevo precio del producto: ")
        cantidad = input("Ingrese la nueva cantidad del producto: ")

        try:
            if precio or cantidad:
                precio = float(precio)
                cantidad = int(cantidad)
        except ValueError:
            print("Por favor, ingrese valores numéricos para el precio y la cantidad.")
            return

        if nombre:
            productos[indice]['nombre'] = nombre
        if precio:
            productos[indice]['precio'] = precio
        if cantidad:
            productos[indice]['cantidad'] = cantidad

        print("Producto actualizado con éxito.")
    else:
        print("Índice no válido.")



def eliminar_producto():
    ver_productos()
    if not productos:
        return

    indice = int(input("Introduce el número del producto a eliminar: ")) - 1
    if 0 <= indice < len(productos):
        eliminado = productos.pop(indice)
        print(f"Producto '{eliminado['nombre']}' eliminado con éxito.")
    else:
        print("Índice no válido.")


def guardar_datos():
    with open("productos.txt", 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados con éxito.")


def cargar_datos():
    try:
        with open("productos.txt", 'r') as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Comenzando con una lista vacía.")


def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()