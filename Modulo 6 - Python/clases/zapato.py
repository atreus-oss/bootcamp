from .producto import Producto

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def mostrar_info(self):
        return f"Zapato: {self._nombre}, Precio: ${self._precio:.2f}, Talla: {self._talla}"
