from Gerador import *
from Evento import *
class Escalonador:
    def __init__(self):
        self.events = [Evento]
        seed = 1
        self.gerador = GeradorCongruenteLinear(seed)

    def add(self, t0: int, t1: int, globalTime: float, tipo: str):
        self.events.append(Evento(type= tuple, time= (globalTime + self.calculateTime(t0, t1))))
        self.events.sort(key=lambda x: x.time)

    def calculateTime(self, a: int, b: int):
        return a + ((b - a) + (b - a) * self.gerador.geraPseudoAleatorio())
    def get(self):
        return self.events.pop(0)