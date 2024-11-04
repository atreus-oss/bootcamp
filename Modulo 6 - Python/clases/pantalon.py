from .ropa import Ropa

class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla, tipo_tela)

    def mostrar_info(self):
        return f"Pantalón: {self._nombre}, Precio: ${self._precio:.2f}, Talla: {self._talla}, Tela: {self._tipo_tela}"