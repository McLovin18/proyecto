import random
from Jugador import Jugador
from Carta import CartaMonstruo, CartaMagica, CartaTrampa

class Juego:
    def __init__(self, jugador, maquina):
        self._jugador = jugador
        self._maquina = maquina

    def iniciar(self):
        turno_jugador = random.choice([True, False])
        print("¡Bienvenido al juego de cartas!")
        print(f"{self._jugador._nombre} vs Máquina")

        while self._jugador.get_puntos_vida() > 0 and self._maquina.get_puntos_vida() > 0:
            print("\nTablero actual:")
            print(self._jugador)
            print(self._maquina)

            if turno_jugador:
                print("Es tu turno.")
                self.fase_jugador(self._jugador)
            else:
                print("Turno de la máquina.")
                self.fase_maquina()

            turno_jugador = not turno_jugador

    def fase_jugador(self, jugador):
        # Implementar lógica de turnos para el jugador
        pass

    def fase_maquina(self):
        # Implementar lógica de turnos para la máquina
        pass
