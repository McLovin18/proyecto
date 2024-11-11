from Carta import Carta
class CartaMonstruo(Carta):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo, atributo):
        super().__init__(nombre, descripcion, "Monstruo")
        self._ataque = ataque  # Privada
        self._defensa = defensa  # Privada
        self._tipo = tipo  # Privada
        self._atributo = atributo  # Privada
        self._posicion = "Ataque"  # Por defecto se pone en posición de ataque

    @property
    def ataque(self):
        return self._ataque

    @property
    def defensa(self):
        return self._defensa

    @property
    def tipo(self):
        return self._tipo

    @property
    def atributo(self):
        return self._atributo

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, value):
        if value in ["Ataque", "Defensa"]:
            self._posicion = value
        else:
            raise ValueError("Posición inválida")
