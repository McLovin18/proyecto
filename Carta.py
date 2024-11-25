class Carta:
    def __init__(self, nombre, descripcion, tipo_carta):
        self._nombre = nombre
        self._descripcion = descripcion
        self._tipo_carta = tipo_carta

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def tipo_carta(self):
        return self._tipo_carta

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @tipo_carta.setter
    def tipo_carta(self, value):
        self._tipo_carta = value


    def __str__(self):
        return f"{self._nombre}: {self._descripcion}"