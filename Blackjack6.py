class Carta:

    def __init__(self, pinta, valor):
        self.pinta = pinta
        self.valor = valor

class Baraja:

    def __init__(self):
        self.cartas = []

    def mezclar(self):
    # Implementar la lógica para mezclar las cartas en la baraja
    pass

    def sacar_carta(self):
    # Implementar la lógica para sacar una carta de la baraja
    pass

class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.fichas = 100
        self.mano = []

    def apostar(self, cantidad):
    # Implementar la lógica para que el jugador apueste una cantida de fichas
    pass

    def pedir_carta(self, carta):
    # Implementar la lógica para que el jugador reciba una carta en su mano
    pass

    def obtener_valor_mano(self):
    # Implementar la lógica para obtener el valor total de la mano del jugador
    pass

    def mostrar_mano(self):
    # Implementar la lógica para mostrar la mano del jugador en pantalla
    pass

class Casa:

    def __init__(self):
    self.mano = []

    def pedir_carta(self, carta):
    # Implementar la lógica para que la casa reciba una carta en su mano
    pass

    def obtener_valor_mano(self):
    # Implementar la lógica para obtener el valor total de la mano de la casa
    pass

    def mostrar_mano(self, mostrar_todas=True):
    # Implementar la lógica para mostrar la mano de la casa en pantalla
    pass

class Juego:

    def __init__(self):
    self.baraja = Baraja()
    self.jugador = None
    self.casa = Casa()

    def registrar_jugador(self, nombre):
    # Implementar la lógica para registrar al jugador
    pass

    def iniciar_juego(self):
    # Implementar la lógica para iniciar el juego
    pass

    def hacer_jugada_jugador(self):
    # Implementar la lógica para que el jugador realice una jugada
    pass

    def hacer_jugada_casa(self):
    # Implementar la lógica para que la casa realice una jugada
    pass

    def finalizar_juego(self):
    # Implementar la lógica para finalizar el juego
    pass