from Jugador import *
from Carta import *
import random

class Juego:
    def __init__(self):
        self.jugador = Jugador("Jugador")
        self.maquina = Jugador("Máquina")
        self.turno = 1
        self.jugador_actual = None

    def inicializar_decks(self):
        # Configuración de las cartas (monstruos, mágicas y trampas)
        tipos_monstruos = ["L", "D", "Z", "G", "B", "O"]  # LUZ, OSCURIDAD, TIERRA, AGUA, FUEGO, VIENTO
        atributos = ["OSCURIDAD", "LUZ", "TIERRA", "AGUA", "FUEGO", "VIENTO"]

        for _ in range(20):  # Monstruos
            carta = CartaMonstruo(
                nombre=f"Monstruo_{random.randint(1, 100)}",
                descripcion="Carta de monstruo",
                ataque=random.randint(1000, 3000),
                defensa=random.randint(1000, 3000),
                tipo=random.choice(tipos_monstruos),
                atributo=random.choice(atributos),
            )
            self.jugador.get_deck().append(carta)
            self.maquina.get_deck().append(carta)

        for _ in range(5):  # Mágicas
            carta = CartaMagica(
                nombre=f"Mágica_{random.randint(1, 100)}",
                descripcion="Carta mágica",
                incremento=random.randint(100, 500),
                tipo_monstruo=random.choice(tipos_monstruos),
            )
            self.jugador.get_deck().append(carta)
            self.maquina.get_deck().append(carta)

        for _ in range(5):  # Trampas
            carta = CartaTrampa(
                nombre=f"Trampa_{random.randint(1, 100)}",
                descripcion="Carta de trampa",
                atributo_contra=random.choice(atributos),
            )
            self.jugador.get_deck().append(carta)
            self.maquina.get_deck().append(carta)

        random.shuffle(self.jugador.get_deck())
        random.shuffle(self.maquina.get_deck())

        self.jugador.inicializar_mano()
        self.maquina.inicializar_mano()




    def mostrar_estado_juego(self):
        # Muestra el estado del juego después de cada turno
        print("\n--- Estado del Juego ---")
        print(f"Vida del Jugador: {self.jugador.get_vida()}")
        print(f"Vida de la maquina: {self.maquina.get_vida()}")
        print("Tablero de Monstruos del Jugador:")
        for i, carta in enumerate(self.jugador.get_tablero_monstruos()):
            if carta:
                print(f"[{i}] {carta.get_nombre()} - Modo: {carta.get_modo()}")

        print(f"Vida de la Máquina: {self.maquina.get_vida()}")  # Mostrar vida (puntos)
        print("Tablero de Monstruos de la Máquina:")
        for i, carta in enumerate(self.maquina.get_tablero_monstruos()):
            if carta:
                print(f"[{i}] {carta.get_nombre()} - Modo: {carta.get_modo()}")

        print("\nMano de la Máquina:")
        for idx, carta in enumerate(self.maquina.get_mano()):
            print(f"[{idx}] {carta.get_nombre()}")



    def realizar_ataque(self, atacante, defensor, carta_atacante):
        print(f"{atacante.get_nombre()} ataca con {carta_atacante.get_nombre()}!")

        monstruos_defensa = [m for m in defensor.get_tablero_monstruos() if m and m.get_modo() == "DEFENSA"]

        if monstruos_defensa:
            # Ataque contra el primer monstruo en defensa (puedes cambiar esta lógica si prefieres atacar a todos)
            monstruo_defensor = monstruos_defensa[0]
            print(f"Atacando {monstruo_defensor.get_nombre()} con ataque de {carta_atacante.get_ataque()} y defensa de {monstruo_defensor.get_defensa()}")

            if carta_atacante.get_ataque() > monstruo_defensor.get_defensa():
                print(f"{monstruo_defensor.get_nombre()} es destruido!")
                defensor.get_tablero_monstruos()[defensor.get_tablero_monstruos().index(monstruo_defensor)] = None
            else:
                print(f"{monstruo_defensor.get_nombre()} defiende con éxito!")
        else:
            # Ataque directo
            daño = carta_atacante.get_ataque()
            defensor.set_vida(defensor.get_vida() - daño)
            print(f"¡{atacante.get_nombre()} inflige {daño} puntos de daño directamente!")

        if defensor.get_vida() <= 0:
            print(f"{defensor.get_nombre()} ha perdido el juego.")
            return True  # El juego termina aquí

        return False  # El juego no termina



    def jugar_turno_jugador(self):
        print("\n--- Turno del Jugador ---")
        if len(self.jugador.get_mano()) < 5:
            self.jugador.robar_carta()
            print("Has robado una carta.")

        turno_terminado = False

        while not turno_terminado:
            self.jugador.mostrar_mano()
            accion = input("Elige una acción:\n1. Jugar carta\n2. Pasar turno\nOpción: ")

            if accion == "1":
                try:
                    indice = int(input("Elige el índice de la carta a jugar: "))
                    carta = self.jugador.get_mano()[indice]

                    if isinstance(carta, CartaMonstruo):
                        posicion = input("Colocar en (A)taque o (D)efensa: ").upper()
                        carta.set_modo("ATAQUE" if posicion == 'A' else "DEFENSA")
                        self.jugador.get_mano().pop(indice)
                        self.jugador.get_tablero_monstruos().append(carta)

                        print(f"{self.jugador.get_nombre()} ha jugado {carta.get_nombre()} en modo {carta.get_modo()}.")
                        
                        if carta.get_modo() == "ATAQUE":
                            if self.realizar_ataque(self.jugador, self.maquina, carta):
                                return  # El juego termina si el ataque gana
                            
                            turno_terminado = True

                    elif isinstance(carta, CartaMagica):
                        # Lógica de carta mágica
                        pass

                    elif isinstance(carta, CartaTrampa):
                        # Lógica de carta trampa
                        pass

                    turno_terminado = True  # El jugador termina su turno después de jugar una carta

                except IndexError:
                    print("Índice no válido.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            elif accion == "2":
                turno_terminado = True  # El jugador decide pasar turno

        print("Fin del turno del Jugador.")

    

    def jugar_turno_maquina(self):
        print("\n--- Turno de la Máquina ---")
        self.maquina.robar_carta()  # La máquina roba una carta

        # Estrategia: Jugar una carta de la mano
        for carta in self.maquina.get_mano():
            if isinstance(carta, CartaMonstruo):
                # Decidir si colocar en ataque o defensa
                posicion = "ATAQUE" if carta.get_ataque() >= carta.get_defensa() else "DEFENSA"
                carta.set_modo(posicion)
                carta.set_boca_arriba(True)  # Siempre boca arriba al jugar
                self.maquina.get_mano().remove(carta)
                self.maquina.get_tablero_monstruos().append(carta)
                print(f"La máquina juega {carta.get_nombre()} en modo {posicion}.")
                break  # Termina al jugar una carta
            elif isinstance(carta, CartaMagica):
                # Jugar una carta mágica
                for monstruo in self.maquina.get_tablero_monstruos():
                    if monstruo and monstruo.get_tipo() == carta.get_tipo_monstruo():
                        monstruo.set_ataque(monstruo.get_ataque() + carta.get_incremento())
                        self.maquina.get_mano().remove(carta)
                        print(f"La máquina usa {carta.get_nombre()} en {monstruo.get_nombre()}, incrementando su ataque.")
                        break
                break  # Termina al usar una carta mágica
            elif isinstance(carta, CartaTrampa):
                # Colocar una trampa en el tablero
                self.maquina.get_mano().remove(carta)
                self.maquina.get_tablero_trampas().append(carta)
                print(f"La máquina coloca una trampa: {carta.get_nombre()}.")
                break  # Termina al colocar una trampa

        # Estrategia: Declarar batalla con cartas en ataque
        for carta in self.maquina.get_tablero_monstruos():
            if carta and carta.get_modo() == "ATAQUE":
                print(f"La máquina ataca con {carta.get_nombre()}.")
                if self.realizar_ataque(self.maquina, self.jugador, carta):
                    return  # Termina si el jugador pierde

        print("La máquina no puede realizar más acciones y pasa el turno.")


    def jugar(self):
        self.inicializar_decks()

        while self.jugador.get_vida() > 0 and self.maquina.get_vida() > 0:
            if self.turno % 2 == 1:
                self.jugar_turno_jugador()
            else:
                self.jugar_turno_maquina()

            self.mostrar_estado_juego()
            self.turno += 1  # Cambiar turno

        if self.jugador.get_vida() <= 0:
            print("¡La máquina gana!")
        elif self.maquina.get_vida() <= 0:
            print("¡El jugador gana!")


if __name__ == "__main__":
    juego = Juego()
    juego.jugar()





#La solucion seria crear una forma de juego de maquina que sea igual a la de juego, pero que esta se pueda controlar por si sola,
#El error radica en que la IA no sabe como usar x poder, y depende siempre que una carta aleatoria sea de tipo monstruo y que este en ataques
#Si buscamos la manera en la que la maquina pueda interactuar por si misma, ya seria increible, eso seria lo unico que nos falta
#El juego de por si ya es completo, solo hay que ver una forma en la que la maquina pueda usar aleatoriamente una carta y usarla como se debe
#La maquina por si sola debera escojer una carta de sus 5 que tiene en su mazo:
#Si la carta es de clase Monstruo, que decida si le es conveniente atacar o defenderse con ella, y ya se sabe que hace si esta en modo ataque o defensa
#Si la carta es de clase Trampa, deberia usarla si es que un oponente quiere atacar con una carta, si este ataca, la carta de clase trampa aparece y bloquea el ataque

#se considera esto para la maquina
#Lógica de la Máquina	
#La máquina debe jugar todas las opciones que tenga en su mano. 
#La máquina siempre debe declara batalla, si es posible.
#La máquina solo debe jugar cartas en defensa si no es posible jugar en ataque.
