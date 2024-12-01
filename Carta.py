class Carta:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def get_nombre(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion

class CartaMonstruo(Carta):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo, atributo):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo
        self.atributo = atributo
        self.boca_arriba = True
        self.modo = "ATAQUE"  # Puede ser "ATAQUE" o "DEFENSA"

    def get_ataque(self):
        return self.ataque

    def set_ataque(self, nuevo_ataque):
        self.ataque = nuevo_ataque

    def get_defensa(self):
        return self.defensa

    def set_defensa(self, nueva_defensa):
        self.defensa = nueva_defensa

    def get_tipo(self):
        return self.tipo

    def get_atributo(self):
        return self.atributo

    def get_boca_arriba(self):
        return self.boca_arriba

    def set_boca_arriba(self, estado):
        self.boca_arriba = estado

    def get_modo(self):
        return self.modo

    def set_modo(self, nuevo_modo):
        self.modo = nuevo_modo

class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incremento, tipo_monstruo, tipo_efecto):
        """
        :param nombre: Nombre de la carta.
        :param descripcion: Descripción de la carta.
        :param incremento: El incremento en puntos de ataque o defensa.
        :param tipo_monstruo: Tipo de monstruo al que afecta la carta (o 'Ninguno' para efecto global).
        :param tipo_efecto: Tipo de efecto ('Ataque' o 'Defensa').
        """
        super().__init__(nombre, descripcion)
        self.incremento = incremento
        self.tipo_monstruo = tipo_monstruo
        self.tipo_efecto = tipo_efecto  # Nuevo atributo que define el tipo de efecto

    def get_incremento(self):
        return self.incremento

    def get_tipo_monstruo(self):
        return self.tipo_monstruo

    def get_tipo_efecto(self):
        return self.tipo_efecto  # Método para obtener el tipo de efecto

    def aplicar_efecto(self, monstruo):
        """Aplica el efecto de la carta mágica sobre un monstruo si el tipo coincide."""
        if self.tipo_monstruo == "Ninguno" or monstruo.get_tipo() == self.tipo_monstruo:
            if self.tipo_efecto == "Ataque":  # Cambiado de nombre a 'tipo_efecto'
                monstruo.set_ataque(monstruo.get_ataque() + self.incremento)
                print(f"{monstruo.get_nombre()} ahora tiene {monstruo.get_ataque()} de ataque.")
            elif self.tipo_efecto == "Defensa":  # Cambiado de nombre a 'tipo_efecto'
                monstruo.set_defensa(monstruo.get_defensa() + self.incremento)
                print(f"{monstruo.get_nombre()} ahora tiene {monstruo.get_defensa()} de defensa.")

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, atributo):
        super().__init__(nombre, descripcion)
        self.atributo = atributo

    def get_atributo_contra(self):
        return self.atributo_contra

    def activar(self, monstruo_atacante):
        """Verifica si la trampa se activa dependiendo del monstruo atacante"""
        # Aquí podrías agregar la lógica de activación de la trampa
        # Ejemplo:
        if self.atributo == "VIENTO" and monstruo_atacante.get_elemento() == "VIENTO":
            print(f"La trampa {self.get_nombre()} ha detenido el ataque de un monstruo VIENTO.")
            return True  # La trampa se activa y detiene el ataque
        return False