from Carta import Carta
class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incremento, tipo_monstruo):
        super().__init__(nombre, descripcion, "Mágica")
        self._incremento = incremento
        self._tipo_monstruo = tipo_monstruo 

    @property
    def incremento(self):
        return self._incremento

    @property
    def tipo_monstruo(self):
        return self._tipo_monstruo


    def cambiarPosicion():
        return("")