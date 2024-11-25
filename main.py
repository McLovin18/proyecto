import random
from Juego import Juego
from Jugador import Jugador
from Carta import CartaMonstruo, CartaMagica, CartaTrampa

def main():
    # Crear cartas de ejemplo
    cartas_monstruo = [
        CartaMonstruo(f"Monstruo {i+1}", "Descripción", 1000+i*10, 800+i*5, "L", "LUZ")
        for i in range(20)
    ]
    cartas_magicas = [
        CartaMagica(f"Mágica {i+1}", "Incrementa ataque", 200, "L") for i in range(5)
    ]
    cartas_trampa = [
        CartaTrampa(f"Trampa {i+1}", "Detiene ataque", "LUZ") for i in range(5)
    ]

    deck_jugador = cartas_monstruo[:10] + cartas_magicas[:3] + cartas_trampa[:2]
    deck_maquina = cartas_monstruo[10:] + cartas_magicas[3:] + cartas_trampa[2:]
    random.shuffle(deck_jugador)
    random.shuffle(deck_maquina)

    jugador = Jugador("Jugador 1", 4000, deck_jugador)
    maquina = Jugador("Máquina", 4000, deck_maquina)

    juego = Juego(jugador, maquina)
    juego.iniciar()

if __name__ == "__main__":
    main()
