from Carta import Carta

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, atributo_bloqueo):
        super().__init__(nombre, descripcion, "Trampa")
        self._atributo_bloqueo = atributo_bloqueo  # Privada

    @property
    def atributo_bloqueo(self):
        return self._atributo_bloqueo