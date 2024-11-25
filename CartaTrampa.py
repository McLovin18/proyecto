from Carta import Carta

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, atributo_objetivo):
        super().__init__(nombre, descripcion, "Trampa")
        self._atributo_objetivo = atributo_objetivo

    @property
    def atributo_objetivo(self):
        return self._atributo_objetivo