from clases.camisa import Camisa
from clases.pantalon import Pantalon
from clases.zapato import Zapato
from clases.tienda import Tienda
from clases.carrito import Carrito
from clases.categoria import Categoria

if __name__ == "__main__":
    # Crear productos
    camisa1 = Camisa("Camisa de rayas", 25.99, "M", "Algodón")
    pantalon1 = Pantalon("Pantalón de mezclilla", 40.50, "L", "Mezclilla")
    zapato1 = Zapato("Zapato deportivo", 60.00, "42")

    # Crear categorías y agregar productos
    categoria_ropa = Categoria("Ropa")
    categoria_calzado = Categoria("Calzado")
    
    categoria_ropa.agregar_producto(camisa1)
    categoria_ropa.agregar_producto(pantalon1)
    categoria_calzado.agregar_producto(zapato1)

    # Crear tienda y agregar categorías
    tienda = Tienda()
    tienda.agregar_categoria(categoria_ropa)
    tienda.agregar_categoria(categoria_calzado)

    # Crear carrito
    carrito = Carrito()

    # Menú para interacción del usuario
    while True:
        print("\n1: Ver productos")
        print("2: Agregar producto al carrito")
        print("3: Ver carrito y finalizar compra")
        print("4: Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            tienda.mostrar_categorias()
        elif opcion == '2':
            nombre_producto = input("Ingresa el nombre del producto que deseas agregar al carrito: ")
            producto_encontrado = False

            # Buscar el producto en las categorías
            for categoria in tienda._categorias:
                for producto in categoria.get_productos():
                    if producto._nombre.lower() == nombre_producto.lower():
                        carrito.agregar_producto(producto)
                        print(f"{nombre_producto} agregado al carrito.")
                        producto_encontrado = True

            # Si no se encuentra el producto, lanzar un error
            if not producto_encontrado:
                print(f"Error: '{nombre_producto}' no se encuentra en el catálogo. Por favor, intenta nuevamente.")
                continue  # Redirige al menú

        elif opcion == '3':
            carrito.mostrar_carrito()
            break
        elif opcion == '4':
            print("Gracias por visitar nuestra tienda.")
            break
        else:
            print("Opción inválida.")