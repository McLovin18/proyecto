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
        if self._deck:
            carta = self._deck.pop(0)
            self._cartas_en_mano.append(carta)
            return carta
        return None
    

    def colocar_carta_monstruo(self, carta, posicion, orientacion):
        if 0 <= posicion < 3 and self._tablero_monstruos[posicion] is None:
            carta._orientacion = orientacion
            carta._boca_arriba = orientacion == "ATAQUE"
            self._tablero_monstruos[posicion] = carta

    

    def colocar_carta_magia_trampa(self, carta, posicion):
        if 0 <= posicion < 3 and self._tablero_magicas_trampa[posicion] is None:
            self._tablero_magicas_trampa[posicion] = carta

    def get_puntos_vida(self):
        return self._vida

    def modificar_puntos_vida(self, cantidad):
        self._vida += cantidad

    def __str__(self):
        mano = ", ".join([str(carta) for carta in self._mano])
        monstruos = ", ".join([str(c) if c else "[Vacío]" for c in self._tablero_monstruos])
        magias_trampas = ", ".join([str(c) if c else "[Vacío]" for c in self._tablero_magicas_trampa])
        return (
            f"Jugador: {self._nombre} (Puntos de vida: {self._vida})\n"
            f"Mano: {mano}\n"
            f"Tablero Monstruos: {monstruos}\n"
            f"Tablero Magia/Trampa: {magias_trampas}"
        )
