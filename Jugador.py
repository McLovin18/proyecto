import random
from Carta import Carta
from CartaMonstruo import CartaMonstruo
from CartaMagica import CartaMagica
from CartaTrampa import CartaTrampa


class Jugador:
    def __init__(self, nombre):
        self._nombre = nombre
        self._vida = 4000
        self._deck = self.generar_deck()
        self._cartas_en_mano = []
        self._tablero_monstruos = [None] * 3
        self._tablero_magicas_trampa = [None] * 3

    @property
    def nombre(self):
        return self._nombre

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        self._vida = value

    @property
    def deck(self):
        return self._deck

    @property
    def cartas_en_mano(self):
        return self._cartas_en_mano

    @property
    def tablero_monstruos(self):
        return self._tablero_monstruos

    @property
    def tablero_magicas_trampa(self):
        return self._tablero_magicas_trampa


    def robar_carta(self):
        return("")
