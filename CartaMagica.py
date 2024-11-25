from Carta import Carta
class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incremento, tipo_objetivo):
        super().__init__(nombre, descripcion)
        self._incremento = incremento
        self._tipo_objetivo = tipo_objetivo

    @property
    def incremento(self):
        return self._incremento

    @property
    def tipo_objetivo(self):
        return self._tipo_objetivo


    def cambiarPosicion():
        return("")