from Evento import *
from Gerador import *
from Escalonador import *
from Fila import *

class Simulador:
    def __init__(self):
        self.tempo_global = 0
        self.escalonador = Escalonador()
        self.fila = Fila()

    def run(self):
        while self.tempo_global < 1000:
            evento = self.escalonador.get()
            self.tempo_global = evento.tempo
            if evento.tipo == 'chegada':
                self.chegada(evento)
            else:
                self.saida(evento)

    def chegada(self, evento):
        # acumula tempo
        if self.fila.status < self.fila.capacity:
            self.fila.enter()
            if self.fila.status <= self.fila.servers:
                self.escalonador.add(Evento(self.tempo_global + self.saida()))
        else:
            self.fila.loss()
        self.escalonador.add(Evento(self.tempo_global + self.chegada()))

    def saida(self, evento):
        # acumula tempo
        self.fila.out()
        if self.fila.status >= self.fila.servers:
            self.escalonador.add(Evento(self.tempo_global + self.saida()))