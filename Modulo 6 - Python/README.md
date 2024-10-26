# Tienda_Ropa_POOBootcamp

## Descripción
Este proyecto es un sistema de compras de ropa implementado en Python, usando Programación Orientada a Objetos (POO). La aplicación permite a los usuarios seleccionar productos de una tienda de ropa y realizar una compra.

## Estructura de Clases
- **Producto**: Clase base que representa un producto general.
- **Ropa**: Clase que hereda de `Producto` y añade características específicas de la ropa.
- **Clases Derivadas de Ropa**: Clases `Camisa`, `Pantalon` y `Zapato`, que heredan de `Ropa`.
- **Tienda**: Clase que maneja los productos disponibles y las compras.
- **Carrito**: Clase que almacena los productos seleccionados y calcula el total a pagar.
- **Categoría**: Clase que agrupa productos por tipo.

## Principios de POO Implementados
- **Encapsulamiento**: Los atributos están encapsulados y se accede a ellos mediante métodos.
- **Herencia**: `Ropa` hereda de `Producto`, y las clases específicas de ropa heredan de `Ropa`.
- **Polimorfismo**: Método `mostrar_info()` sobrescrito en cada clase para mostrar información específica.
- **Abstracción**: Los detalles de la compra están ocultos; el usuario solo interactúa con la selección y visualización de productos.

## Instrucciones
Ejecuta el archivo `main.py` para iniciar la aplicación de la tienda. Sigue las instrucciones para seleccionar productos y realizar la compra.