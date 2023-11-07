import random
import Interfaz


class Jugador:

    def __init__(self, nombre):
        self.nombre:str = nombre
        self.intentos_maximos = 6
        self.intentos_restantes = self.intentos_maximos

    def registrar_jugador(self):
        pass

    def crear_jugador(self):
        pass


class Problema:

    def crear_problema(self):
        elementos = [str(i) for i in range(10)] + ['+', '-', '*', '/', '=']
        secuencia = [random.choice(elementos) for _ in range(8)]
        return secuencia


class Juego:

    def __init__(self):
        self.intentos_maximos = 6
        self.intentos_restantes = self.intentos_maximos
        self.problem = Problema()
        self.target_sequence = self.problem.crear_problema()

    def cantidad_intentos(self) -> int:
        return self.intentos_restantes

    def comparar_problemas(self):
        intento = Interfaz.intento_pantalla.get()
        pocision_correcta = 0
        elementos_correctos = 0
        elementos_incorrectos = 0
        for i in range(8):
            if intento[i] == self.target_sequence[i]:
                pocision_correcta += 1
            elif intento[i] in self.target_sequence:
                elementos_correctos += 1
            else:
                elementos_incorrectos += 1
        return pocision_correcta, elementos_correctos, elementos_incorrectos
