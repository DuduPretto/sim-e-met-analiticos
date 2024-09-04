from Evento import *
from Gerador import *
from Escalonador import *
from Fila import *

class Simulador:
    def __init__(self):
        self.tempo_global = 0
        self.escalonador = Escalonador()
        # self.fila = Fila(5, servers, (2, 5), (3, 5))  
        self.eventCount = 0

        self.escalonador.add(t0=2.0, t1=2.0, globalTime=0, tipo="chegada")
    
    def run(self):
        try:
            while True: 
                evento = self.escalonador.get()
                
                if evento.type == 'chegada':
                    self.chegada(evento)
                    self.tempo_global = evento.time
                else:
                    self.saida(evento)
                    self.tempo_global = evento.time
        except StopIteration as e:
            print(e)
            self.exibirResultados()

    def exibirResultados(self):
        total = 0
        for i, tempo in enumerate(self.fila.accumulator):
            print(f"Estado {i}: {tempo} unidades de tempo")
            total += tempo
        print(f"Acumulado total: {total} ")    
        print(f"Número total de perdas: {self.fila.losses}")
        print(f"Tempo global da simulação: {self.tempo_global}")
    
    def chegada(self, evento):
        self.fila.accumulator[self.fila.status] += (evento.time - self.tempo_global )
       
        if self.fila.status < self.fila.capacity:
            self.fila.enter()
            if self.fila.status <= self.fila.servers:
                self.escalonador.add(t0=self.fila.serviceInterval[0], t1=self.fila.serviceInterval[1], globalTime=self.tempo_global, tipo="saida")
        else:
            self.fila.loss()
        self.escalonador.add(t0=self.fila.arrivalInterval[0], t1=self.fila.arrivalInterval[1], globalTime=self.tempo_global, tipo="chegada")

    def saida(self, evento):
        self.fila.accumulator[self.fila.status] += (evento.time - self.tempo_global)
        
        self.fila.out()
        if self.fila.status >= self.fila.servers:
            self.escalonador.add(t0=self.fila.serviceInterval[0], t1=self.fila.serviceInterval[1], globalTime=self.tempo_global, tipo="saida")
