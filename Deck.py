from CartaMonstruo import CartaMonstruo
from CartaMagica import CartaMagica
from CartaTrampa import CartaTrampa
import random

class Deck:
    def __init__(self):
        self.cartas = []

    def cargar_cartas(self, archivo):
        monstruos = []  
        magicas = []    
        trampas = []    

        # Abrir y leer el archivo
        with open(archivo, 'r') as f:
            for line in f:
                atributos = line.strip().split(',')
                nombre = atributos[0].strip()
                descripcion = atributos[1].strip()
                tipo_carta = atributos[2].strip()

                # Cargar cartas de tipo 'Monstruo'
                if tipo_carta == 'Monstruo':
                    ataque = int(atributos[3].strip())
                    defensa = int(atributos[4].strip())
                    tipo = atributos[5].strip()
                    atributo = atributos[6].strip()
                    monstruos.append(CartaMonstruo(nombre, descripcion, tipo_carta, ataque, defensa, tipo, atributo))
                 
                # Cargar cartas de tipo 'Mágica'
                elif tipo_carta == 'Mágica':
                    tipo_monstruo_influenciado = atributos[3].strip()
                    incremento = int(atributos[4].strip())
                    magicas.append(CartaMagica(nombre, descripcion, tipo_carta, tipo_monstruo_influenciado, incremento))

                # Cargar cartas de tipo 'Trampa'
                elif tipo_carta == 'Trampa':
                    atributo_monstruo_influenciado = atributos[3].strip()
                    trampas.append(CartaTrampa(nombre, descripcion, tipo_carta, atributo_monstruo_influenciado))

        # Seleccionar 20 cartas aleatorias de monstruos, 5 de mágicas y 5 de trampas
    
        cartas_monstruos = random.sample(monstruos, 20)  
        cartas_magicas = random.sample(magicas, 5)      
        cartas_trampas = random.sample(trampas, 5)       
        self.cartas = cartas_monstruos + cartas_magicas + cartas_trampas
       

    def repartir_cartas(self, jugador):
        random.shuffle(self.cartas)  
        jugador.deck= self.cartas
        jugador.mano = [self.cartas.pop() for _ in range(5)]
        
