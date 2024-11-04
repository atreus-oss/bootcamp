from .producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return f"{self.__class__.__name__}: {self._nombre}, Precio: ${self._precio:.2f}, Talla: {self._talla}, Tela: {self._tipo_tela}"
