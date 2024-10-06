from Evento import *
from Gerador import *
from Escalonador import *
from Fila import *

class Simulador:
    def __init__(self):
        self.tempo_global = 0
        self.escalonador = Escalonador()
        # self.fila1 = Fila(5, servers, (2, 5), (3, 5))  
        self.eventCount = 0

        self.escalonador.add(t0=2.0, t1=2.0, globalTime=0, tipo="chegada")
    
    def run(self):
        try:
            while True: 
                evento = self.escalonador.get()
                
                if evento.type == 'chegada':
                    self.chegada(evento)
                    self.tempo_global = evento.time
                elif evento.type == 'passagem':
                    self.passagem(evento)
                    self.tempo_global = evento.time
                else:
                    self.saida(evento)
                    self.tempo_global = evento.time
        except StopIteration as e:
            print(e)
            print("\nFila 1 ---------------")
            self.exibirResultados(self.fila1)
            print("\nFila 2 ---------------")
            self.exibirResultados(self.fila2)

    def exibirResultados(self, fila):
        total = 0
        for i, tempo in enumerate(fila.accumulator):
            print(f"Estado {i}: {tempo} unidades de tempo ---  {tempo/self.tempo_global * 100}%")
            total += tempo
        print(f"Acumulado total: {total} ")    
        print(f"Número total de perdas: {fila.losses}")
        print(f"Tempo global da simulação: {self.tempo_global}")
    
    def chegada(self, evento):
        self.acumulaTempo(evento)
       
        if self.fila1.status < self.fila1.capacity:
            self.fila1.enter()
            if self.fila1.status <= self.fila1.servers:
                self.escalonador.add(t0=self.fila1.serviceInterval[0], t1=self.fila1.serviceInterval[1], globalTime=self.tempo_global, tipo="passagem")
        else:
            self.fila1.loss()
        self.escalonador.add(t0=self.fila1.arrivalInterval[0], t1=self.fila1.arrivalInterval[1], globalTime=self.tempo_global, tipo="chegada")

    def saida(self, evento):
        self.acumulaTempo(evento)
        
        self.fila2.out()
        if self.fila2.status >= self.fila2.servers:
            self.escalonador.add(t0=self.fila2.serviceInterval[0], t1=self.fila2.serviceInterval[1], globalTime=self.tempo_global, tipo="saida")

    def passagem(self, evento):
        self.acumulaTempo(evento)
        
        self.fila1.out()
        if self.fila1.status >= self.fila1.servers:
            self.escalonador.add(t0=self.fila1.serviceInterval[0], t1=self.fila1.serviceInterval[1], globalTime=self.tempo_global, tipo="passagem")

        if self.fila2.status < self.fila2.capacity:
            self.fila2.enter()
            if self.fila2.status <= self.fila2.servers:
                self.escalonador.add(t0=self.fila2.serviceInterval[0], t1=self.fila2.serviceInterval[1], globalTime=self.tempo_global, tipo="saida")
        else:
            self.fila2.loss()

    def acumulaTempo(self, evento):
        self.fila1.accumulator[self.fila1.status] += (evento.time - self.tempo_global)
        self.fila2.accumulator[self.fila2.status] += (evento.time - self.tempo_global)
