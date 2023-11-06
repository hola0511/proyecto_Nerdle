import random


class Jugador:

    def registrar_jugador(self):
        pass
    def crear_jugador(self):
        pass


class problema:

    def crear_problema(self):
        elementos = [str(i) for i in range(10)] + ['+', '-', '*', '/', '=']
        secuencia = [random.choice(elementos) for _ in range(8)]
        return secuencia

    def mostrar_problema(self):
        pass


class juego:

    def cantidad_intentos(self):
        pass

    def comparar_problemas(self):
        pass

    def finalizar_problema(self):
        pass

    def siguiente_intento(self):
        pass