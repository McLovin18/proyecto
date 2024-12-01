from Jugador import *
from Carta import *
import random

class Juego:
    def __init__(self):
        # Cartas iniciales
        self.cartas = [
            CartaMonstruo("Dragón Rojo", "Dragón de fuego que destruye todo a su paso", 2500, 2000, "Monstruo", "FUEGO"),
            CartaMonstruo("Lanzador Mágico", "Monstruo que lanza hechizos poderosos", 1500, 1000, "Monstruo", "LUZ"),
            CartaMonstruo("Zombi Infierno", "Zombi con poderes oscuros", 1800, 1500, "Monstruo", "OSCURIDAD"),
            CartaMonstruo("Guerrero Valiente", "Guerrero de gran coraje", 1600, 1200, "Monstruo", "TIERRA"),
            CartaMonstruo("Bestia Salvaje", "Bestia feroz que ataca sin piedad", 1700, 1300, "Monstruo", "AGUA"),
            CartaMagica("Espada de Arturo", "Aumenta el ataque de los guerreros", 200, "Guerrero"),
            CartaMagica("Escudo de Chamelote", "Aumenta la defensa de los guerreros", 200, "Guerrero"),
            CartaMagica("Poción de Vida", "Restaura 500 puntos de vida a un jugador", 500, "Ninguno"),
            CartaTrampa("Barrera de Magia", "Protege un monstruo de los ataques", "Ninguno"),
            CartaTrampa("Tornado de Polvo", "Detiene el ataque de un monstruo de atributo VIENTO", "VIENTO")
        ]

        # Jugadores
        self.jugador = Jugador("jugador")
        self.maquina = Jugador("maquina")

        self.turno = 1  # Iniciar el turno

        self.iniciar_juego()

    def iniciar_juego(self):
        # Asignar 5 cartas aleatorias a la mano del jugador
        self.jugador.set_mano(random.sample(self.cartas, 5))
        
        # Asignar 5 cartas aleatorias a la mano de la máquina
        self.maquina.set_mano(random.sample(self.cartas, 5))
        
        print("--- Cartas Iniciales del Jugador ---")
        for carta in self.jugador.get_mano():
            print(carta.get_nombre())
        
        print("--- Cartas Iniciales de la Máquina ---")
        for carta in self.maquina.get_mano():
            print(carta.get_nombre())

    
    def realizar_ataque(self, atacante, defensor, monstruo_atacante):
        # Verificar si hay monstruos en el tablero del defensor
        if len(defensor.get_tablero_monstruos()) == 0:
            print("No hay monstruos en el tablero del defensor para atacar directamente.")
            # Si no hay monstruos, el ataque va directo a los puntos de vida
            defensor.perder_vida(monstruo_atacante.get_ataque())
            print(f"{monstruo_atacante.get_nombre()} ataca directamente y reduce la vida de {defensor.get_nombre()} a {defensor.get_vida()}.")
            return

        # Elige un monstruo defensor aleatorio
        monstruo_defensor = random.choice(defensor.get_tablero_monstruos())
        print(f"{monstruo_atacante.get_nombre()} está atacando a {monstruo_defensor.get_nombre()}.")

        # Comparar puntos de ataque del atacante con los puntos de defensa del defensor
        if monstruo_atacante.get_ataque() > monstruo_defensor.get_defensa():
            print(f"{monstruo_atacante.get_nombre()} destruye a {monstruo_defensor.get_nombre()}!")
            defensor.get_tablero_monstruos().remove(monstruo_defensor)  # Eliminar monstruo defensor del tablero
            daño = monstruo_atacante.get_ataque() - monstruo_defensor.get_defensa()
            defensor.perder_vida(daño)  # Reducir los puntos de vida
            print(f"{defensor.get_nombre()} pierde {daño} puntos de vida. Vida restante: {defensor.get_vida()}.")
        elif monstruo_atacante.get_ataque() == monstruo_defensor.get_defensa():
            print(f"El ataque de {monstruo_atacante.get_nombre()} ha sido neutralizado. Ambos monstruos permanecen en el campo.")
        else:
            print(f"{monstruo_atacante.get_nombre()} no puede destruir a {monstruo_defensor.get_nombre()}. El atacante recibe daño.")
            daño = monstruo_defensor.get_defensa() - monstruo_atacante.get_ataque()
            atacante.perder_vida(daño)
            print(f"{atacante.get_nombre()} pierde {daño} puntos de vida. Vida restante: {atacante.get_vida()}.")





    def mostrar_estado_juego(self):
        # Muestra el estado del juego después de cada turno
        print("\n--- Estado del Juego ---")
        print(f"Vida del Jugador: {self.jugador.get_vida()}")
        print(f"Vida de la máquina: {self.maquina.get_vida()}")

        # Mostrar monstruos en los tableros
        print("\nTablero de Monstruos del Jugador:")
        for i, carta in enumerate(self.jugador.get_tablero_monstruos()):
            if carta:
                print(f"[{i}] {carta.get_nombre()} - Modo: {carta.get_modo()}")

        print("\nTablero de Monstruos de la Máquina:")
        for i, carta in enumerate(self.maquina.get_tablero_monstruos()):
            if carta:
                print(f"[{i}] {carta.get_nombre()} - Modo: {carta.get_modo()}")

        print("\nMano de la Máquina:")
        self.maquina.mostrar_mano()  # Mostrar la mano del jugador

    def robar_carta(self, jugador):
        # Robar una carta aleatoria de la lista de cartas
        carta_robada = random.choice(self.cartas)
        print(f"{jugador.get_nombre()} ha robado una carta: {carta_robada.get_nombre()}")
        jugador.agregar_carta_a_mano(carta_robada)

    def jugar_turno_jugador(self):
        print("--- Turno del Jugador ---")

        # El jugador roba una carta si tiene menos de 5 cartas en mano
        if len(self.jugador.get_mano()) < 5:
            self.robar_carta(self.jugador)

        # Mostrar las cartas del jugador
        print("Cartas en la mano del jugador:")
        for idx, carta in enumerate(self.jugador.get_mano()):
            tipo = type(carta).__name__
            print(f"[{idx}] {carta.get_nombre()} - {tipo}")

        # El jugador elige una carta de su mano
        eleccion = int(input("Elige una carta para jugar (0-{}) : ".format(len(self.jugador.get_mano()) - 1)))  # Aquí cambiamos el rango
        carta = self.jugador.get_mano()[eleccion]  # Utilizamos el índice correcto
        print(f"El jugador ha elegido {carta.get_nombre()}")

        if isinstance(carta, CartaMonstruo):  # Si la carta es un monstruo
            # El jugador decide si jugarla en modo ataque o defensa
            modo = input("¿Quieres jugarlo en modo ataque o defensa? (A/D): ").upper()
            if modo == "A":
                print(f"El jugador coloca {carta.get_nombre()} en modo ATAQUE.")
                carta.set_modo("ATAQUE")
                carta.set_boca_arriba(True)
                self.jugador.get_tablero_monstruos().append(carta)
            elif modo == "D":
                print(f"El jugador coloca {carta.get_nombre()} en modo DEFENSA.")
                carta.set_modo("DEFENSA")
                carta.set_boca_arriba(False)
                self.jugador.get_tablero_monstruos().append(carta)

        elif isinstance(carta, CartaTrampa):  # Si la carta es una trampa
            print(f"El jugador coloca {carta.get_nombre()} en el campo de trampas.")
            self.jugador.get_tablero_trampas().append(carta)

        elif isinstance(carta, CartaMagica):  # Si la carta es una carta mágica
            print(f"El jugador activa {carta.get_nombre()}.")
            self.realizar_ataque(self.jugador, self.maquina, carta)


    def jugar_turno_maquina(self):
        print("--- Turno de la Máquina ---")

        if len(self.maquina.get_mano()) < 5:
            self.robar_carta(self.maquina)

        print("Cartas en la mano de la máquina:")
        for idx, carta in enumerate(self.maquina.get_mano()):
            tipo = type(carta).__name__
            print(f"[{idx}] {carta.get_nombre()} - {tipo}")

        # Primero, verifica si hay cartas trampa que puedan activarse
        for carta in self.maquina.get_mano():
            if isinstance(carta, CartaTrampa):
                # Si es una carta trampa, intenta activarla
                if self.jugador.get_tablero_monstruos():
                    # La máquina elige un monstruo de su tablero para atacar
                    monstruo_atacante = random.choice(self.maquina.get_tablero_monstruos())
                    print(f"La máquina decide atacar con {monstruo_atacante.get_nombre()}.")
                    self.realizar_ataque(self.maquina, self.jugador, monstruo_atacante)

        # Si no se activó ninguna trampa, la máquina juega una carta normal
        carta = random.choice(self.maquina.get_mano())  # Elegir carta aleatoria de la mano
        print(f"La máquina elige {carta.get_nombre()}")

        # Si es una carta monstruo, se maneja como en el turno del jugador
        if isinstance(carta, CartaMonstruo):
            # La máquina juega el monstruo en modo ataque o defensa de forma aleatoria
            modo = random.choice(["A", "D"])
            if modo == "A":
                print(f"La máquina coloca {carta.get_nombre()} en modo ATAQUE.")
                carta.set_modo("ATAQUE")
                carta.set_boca_arriba(True)
            elif modo == "D":
                print(f"La máquina coloca {carta.get_nombre()} en modo DEFENSA.")
                carta.set_modo("DEFENSA")
                carta.set_boca_arriba(False)
            self.maquina.get_tablero_monstruos().append(carta)

            # Si la máquina tiene monstruos en el tablero, realiza un ataque
            if self.jugador.get_tablero_monstruos():
                ataque_objetivo = random.choice(self.jugador.get_tablero_monstruos())  # Elegir monstruo aleatorio del jugador
                print(f"La máquina decide atacar a {ataque_objetivo.get_nombre()} con {carta.get_nombre()}.")
                self.realizar_ataque(self.maquina, self.jugador, carta)
                return  # Después de atacar, termina el turno de la máquina



    def jugar(self):
        while self.jugador.get_vida() > 0 and self.maquina.get_vida() > 0:
            self.mostrar_estado_juego()

            # Turno del jugador
            self.jugar_turno_jugador()

            if self.maquina.get_vida() <= 0:
                print("¡El jugador ha ganado!")
                break

            # Turno de la máquina
            self.jugar_turno_maquina()

            if self.jugador.get_vida() <= 0:
                print("¡La máquina ha ganado!")
                break

# Inicializamos el juego
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
