from Jugador import *
from Carta import *
import random

class Juego:
    def __init__(self):
        self.cartas = self.cargar_cartas_desde_archivo("Deck.txt")
        self.jugador = Jugador("jugador")
        self.maquina = Jugador("maquina")
        self.turno = 1  # Iniciar el turno
        self.iniciar_juego()

    def cargar_cartas_desde_archivo(self, archivo):
        cartas = []
        # Abrir el archivo y leerlo línea por línea
        with open(archivo, 'r') as file:
            for linea in file.readlines():
                # Limpiar la línea y dividirla por comas
                datos = linea.strip().split(', ')

                # Procesamos la carta dependiendo del número de atributos
                if len(datos) == 7:  # Es una carta de monstruo
                    nombre = datos[0]
                    descripcion = datos[1]
                    ataque = int(datos[3])
                    defensa = int(datos[4])
                    tipo = datos[5]
                    atributo = datos[6]
                    carta = CartaMonstruo(nombre, descripcion, ataque, defensa, tipo, atributo)

                elif len(datos) == 4: # trampa
                    nombre = datos[0]
                    descripcion = datos[1]
                    tipo = datos[3]
                    carta = CartaTrampa(nombre, descripcion, tipo)
                elif len(datos) == 5:
                    #"Poción de Vida", "Restaura 500 puntos de vida a un jugador", "Mágica", "Ninguno", 0
                    nombre =  datos[0]
                    descripcion = datos [1]
                    tipo = datos [3]
                    incremento = datos [4]
                    carta = CartaMagica(nombre,descripcion,incremento,tipo,"ATAQUE")
                    
                else:
                    # Si no cumple con ninguna de las condiciones, se puede omitir o mostrar un mensaje de advertencia
                    print(f"Advertencia: Línea no válida para una carta: {linea}")
                    continue  # Salta a la siguiente línea

                # Agregar la carta a la lista
                cartas.append(carta)

        for carta1 in cartas:
            print(carta1)
        return cartas

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

    def realizar_ataque(self, defensor, carta):
        # Asumimos que 'carta' es un monstruo que está siendo utilizado para atacar
        monstruo_atacante = carta  # Esto depende de cómo tengas estructurada la carta (puede ser una carta monstruo, mágica, etc.)

        # Si hay monstruos en el tablero del defensor, atacamos un monstruo
        if defensor.get_tablero_monstruos():
            # Aquí seleccionamos el primer monstruo del defensor para atacar
            monstruo_defensor = defensor.get_tablero_monstruos()[0]
            print(
                f"El atacante ({monstruo_atacante.get_nombre()}) ataca al monstruo defensor ({monstruo_defensor.get_nombre()})")

            # Calcular el daño
            if monstruo_atacante.get_ataque() > monstruo_defensor.get_defensa():
                # Si el ataque es mayor que la defensa, el defensor pierde vida
                daño = monstruo_atacante.get_ataque() - monstruo_defensor.get_defensa()
                defensor.perder_vida(daño)
                print(f"El defensor pierde {daño} puntos de vida. Nueva vida: {defensor.get_vida()}")
            else:
                print("El ataque del monstruo atacante no ha sido suficiente para destruir al defensor.")
        else:
            # Si no hay monstruos en el tablero, el atacante puede atacar directamente a la vida del defensor
            print(f"El jugador ataca directamente con {monstruo_atacante.get_nombre()}")
            defensor.perder_vida(monstruo_atacante.get_ataque())  # Se reduce la vida del defensor directamente
            print(f"La vida del defensor se reduce a {defensor.get_vida()} puntos.")

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
        eleccion = -1
        while eleccion < 0 or eleccion >= len(self.jugador.get_mano()):
            try:
                eleccion = int(input("Elige una carta para jugar (0-{}) : ".format(len(self.jugador.get_mano()) - 1)))
            except ValueError:
                print("Por favor, ingresa un número válido.")

        carta = self.jugador.get_mano()[eleccion]  # Utilizamos el índice correcto
        print(f"El jugador ha elegido {carta.get_nombre()}")

        if isinstance(carta, CartaMonstruo):  # Si la carta es un monstruo
            # El jugador decide si jugarla en modo ataque o defensa
            modo = ""
            while modo not in ["A", "D"]:  # Validamos que la entrada sea correcta
                modo = input("¿Quieres jugarlo en modo ataque o defensa? (A/D): ").upper()
                if modo not in ["A", "D"]:
                    print("Opción no válida. Por favor, ingresa 'A' para ataque o 'D' para defensa.")
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

            # Ahora, el jugador puede decidir atacar
            if self.maquina.get_tablero_monstruos():
                # Si la máquina tiene monstruos, el jugador elige uno para atacar
                ataque_a_realizar = -1
                while ataque_a_realizar < 0 or ataque_a_realizar >= len(self.maquina.get_tablero_monstruos()):
                    ataque_a_realizar = int(input("Elige un monstruo de la máquina para atacar (0-{}): ".format(
                        len(self.maquina.get_tablero_monstruos()) - 1)))
                monstruo_objetivo = self.maquina.get_tablero_monstruos()[ataque_a_realizar]
                self.realizar_ataque(self.maquina, monstruo_objetivo)
            else:
                # Si no hay monstruos, el jugador ataca directamente
                self.realizar_ataque(self.maquina, carta)

        elif isinstance(carta, CartaTrampa):  # Si la carta es una trampa
            print(f"El jugador coloca {carta.get_nombre()} en el campo de trampas.")
            self.jugador.get_tablero_trampas().append(carta)

        elif isinstance(carta, CartaMagica):  # Si la carta es una carta mágica
            print(f"El jugador activa {carta.get_nombre()}.")
            # Aquí deberías manejar la activación de cartas mágicas
            self.jugador.activar_carta_magica(self.jugador, carta)  # Método para manejar cartas mágicas

    def jugar_turno_maquina(self):
        print("--- Turno de la Máquina ---")

        # La máquina roba una carta si tiene menos de 5 cartas en mano
        if len(self.maquina.get_mano()) < 5:
            self.robar_carta(self.maquina)

        # Mostrar las cartas de la máquina
        print("Cartas en la mano de la máquina:")
        for idx, carta in enumerate(self.maquina.get_mano()):
            tipo = type(carta).__name__
            print(f"[{idx}] {carta.get_nombre()} - {tipo}")

        # La máquina debe decidir qué hacer con la carta
        carta = random.choice(self.maquina.get_mano())  # Elegir una carta aleatoria

        if isinstance(carta, CartaMonstruo):  # Si es una carta de monstruo
            if self.maquina.get_tablero_monstruos():  # Si la máquina ya tiene monstruos
                print(f"La máquina decide jugar {carta.get_nombre()}.")
                modo = "A" if carta.get_ataque() > carta.get_defensa() else "D"
                if modo == "A":
                    print(f"El monstruo {carta.get_nombre()} se coloca en modo ATAQUE.")
                    carta.set_modo("ATAQUE")
                    carta.set_boca_arriba(True)
                    self.maquina.get_tablero_monstruos().append(carta)
                else:
                    print(f"El monstruo {carta.get_nombre()} se coloca en modo DEFENSA.")
                    carta.set_modo("DEFENSA")
                    carta.set_boca_arriba(False)
                    self.maquina.get_tablero_monstruos().append(carta)
            else:
                # Si no tiene monstruos, atacar directamente
                print(f"La máquina no tiene monstruos en el tablero, así que no puede atacar.")
                self.maquina.get_tablero_monstruos().append(
                    carta)  # Se coloca en el tablero, en modo defensa si es necesario

            # Ahora, la máquina puede decidir atacar
            if self.jugador.get_tablero_monstruos():
                # Si el jugador tiene monstruos, la máquina elige uno para atacar
                ataque_a_realizar = random.randint(0, len(self.jugador.get_tablero_monstruos()) - 1)
                monstruo_objetivo = self.jugador.get_tablero_monstruos()[ataque_a_realizar]
                self.realizar_ataque(self.jugador, monstruo_objetivo)
            else:
                # Si no hay monstruos, la máquina ataca directamente
                self.realizar_ataque(self.jugador, carta)

        elif isinstance(carta, CartaTrampa):  # Si es una carta trampa
            print(f"La máquina coloca {carta.get_nombre()} en el campo de trampas.")
            self.maquina.get_tablero_trampas().append(carta)

        elif isinstance(carta, CartaMagica):  # Si es una carta mágica
            print(f"La máquina activa {carta.get_nombre()}.")
            self.maquina.activar_carta_magica(self.maquina, carta)

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