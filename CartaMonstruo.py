from Carta import Carta
class CartaMonstruo(Carta):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo, atributo):
        super().__init__(nombre, descripcion, "Monstruo")
        self._ataque = ataque  
        self._defensa = defensa 
        self._tipo = tipo
        self._atributo = atributo
        self._posicion = "Ataque"

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
