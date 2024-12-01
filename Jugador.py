from Carta import *

class Jugador:
    def __init__(self, nombre):
        self.puntos = 0  # Atributo corregido
        self.nombre = nombre
        self.vida = 4000
        self.deck = []
        self.mano = []
        self.tablero_monstruos = []  # Lista dinámica para monstruos
        self.tablero_magicas = []  # Lista de cartas mágicas activas
        self.tablero_trampas = []  # Lista de cartas trampa activas


    def agregar_carta_deck(self, carta):
        """Agrega una carta al deck del jugador."""
        self.deck.append(carta)

    def mostrar_deck(self):
        """Muestra todas las cartas en el deck."""
        for carta in self.deck:
            print(carta.get_nombre(), "-", carta.get_descripcion())

    def activar_carta_magica(self, jugador, carta):
        """Activa una carta mágica y aplica su efecto."""
        print(f"Activando {carta.get_nombre()} de {jugador.get_nombre()}.")

        if carta.get_tipo_efecto() == "Ataque":
            if jugador.get_tablero_monstruos():
                monstruo = jugador.get_tablero_monstruos()[0]  # Escoge el primer monstruo
                carta.aplicar_efecto(monstruo)
            else:
                print("No hay monstruos en el tablero para aplicar el efecto de ataque.")

        elif carta.get_tipo_efecto() == "Defensa":
            if jugador.get_tablero_monstruos():
                monstruo = jugador.get_tablero_monstruos()[0]  # Escoge el primer monstruo
                carta.aplicar_efecto(monstruo)
            else:
                print("No hay monstruos en el tablero para aplicar el efecto de defensa.")

        else:
            print(f"El efecto de la carta {carta.get_nombre()} no se puede aplicar.")
    def agregar_carta_a_mano(self, carta):
        self.mano.append(carta)  # Agregar la carta a la mano del jugador


    def mostrar_mano(self):
        print("Mano de " + self.nombre + ":")
        for idx, carta in enumerate(self.mano):
            # Mostrar el nombre y el tipo de carta
            tipo = type(carta).__name__  # Obtener el nombre de la clase de la carta
            print(f"[{idx}] {carta.get_nombre()} - {tipo}")

    def inicializar_mano(self):
        """Inicializa la mano del jugador, robando 5 cartas de su deck."""
        while len(self.mano) < 5 and self.deck:
            self.robar_carta()

    def get_nombre(self):
        return self.nombre

    def get_vida(self):
        return self.vida
    
    def set_vida(self, nueva_vida):
        self.vida = max(0, nueva_vida)

    def get_puntos(self):
        return self.puntos

    def get_deck(self):
        return self.deck
    
    def set_deck(self, new_deck):
        self.deck = new_deck

    def set_mano(self, new_mano):
        self.mano = new_mano

    def get_mano(self):
        return self.mano

    def get_tablero_monstruos(self):
        return self.tablero_monstruos

    def get_tablero_magicas(self):
        return self.tablero_magicas

    def perder_vida(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        print(f"Vida restante del jugador: {self.vida}")
    def get_tablero_trampas(self):
        return self.tablero_trampas