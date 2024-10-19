'''def puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()

        if point.isdecimal():
            point = int(point)

            if point <= 0 or point > 5:  # Expresión condicional que verifica si es menor que 0 o mayor que 5
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{post} \n')
                file_pc.close()
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def resultados():
    print('Resultados hasta la fecha.')
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()

def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                puntuacion_y_comentario()

            if num == 2:
                resultados()

            if num == 3:
                print('Finalizando')
                break  # Sentencia para finalizar el procesamiento

            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

main()'''

productos = []


def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")

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

        if nombre:
            productos[indice]['nombre'] = nombre
        if precio:
            productos[indice]['precio'] = float(precio)
        if cantidad:
            productos[indice]['cantidad'] = int(cantidad)

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
    cargar_datos()  # Cargar datos al iniciar el programa
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