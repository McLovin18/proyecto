# Jugador.py
from Carta import *

class Jugador:
    def __init__(self, nombre):
        self.set_puntos = 0
        self.nombre = nombre
        self.vida = 4000
        self.deck = []
        self.mano = []
        self.tablero_monstruos = [None, None, None]
        self.tablero_magicas_trampas = [None, None, None]
        self.tablero_trampas = []  # Lista para trampas


    

    def mostrar_mano(self):
        print(f"Mano de {self.nombre}:")
        for i, carta in enumerate(self.mano):
            print(f"[{i}] {carta.get_nombre()} - {carta.get_descripcion()}")

    def inicializar_mano(self):
        """Inicializa la mano del jugador, robando 5 cartas de su deck."""
        while len(self.mano) < 5 and len(self.deck) > 0:
            carta = self.deck.pop()  # Roba una carta del deck
            self.mano.append(carta)  # Añade la carta a la mano


    

    def get_nombre(self):
        return self.nombre

    def get_vida(self):
        return self.vida
    
    def set_vida(self, nueva_vida):
        self.vida = max(0,nueva_vida)


    def get_puntos(self):
        return self.puntos

    def get_deck(self):
        return self.deck

    def get_mano(self):
        return self.mano

    def get_tablero_monstruos(self):
        return self.tablero_monstruos

    
    def get_tablero_trampas(self):
        return self.tablero_trampas

    