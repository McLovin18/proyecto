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
    def __init__(self, nombre, descripcion, incremento, tipo_monstruo):
        super().__init__(nombre, descripcion)
        self.incremento = incremento
        self.tipo_monstruo = tipo_monstruo

    def get_incremento(self):
        return self.incremento

    def get_tipo_monstruo(self):
        return self.tipo_monstruo

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, atributo_contra):
        super().__init__(nombre, descripcion)
        self.atributo_contra = atributo_contra

    def get_atributo_contra(self):
        return self.atributo_contra