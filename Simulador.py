from Evento import *
from Gerador import *
from Escalonador import *
from Fila import *

class Simulador:
    def __init__(self, filas, networkConnections, initialTime):
        self.tempo_global = 0
        self.escalonador = Escalonador()
        self.filas = filas 
        self.eventCount = 0
        self.networkConnections = networkConnections  
        self.escalonador.add(t0=initialTime, t1=initialTime, globalTime=0, tipo="chegada")
    
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
            for fila in self.filas:
                print(f"\nResultados da fila {self.filas.index(fila)}:")
                self.exibirResultados(fila)

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
        fila = self.filas[0]
        if fila.status < fila.capacity:
            fila.enter()
            if fila.status <= fila.servers:
                # Parte nova
                aleatorio = self.escalonador.retornaAleatorio()

                probabilidadesRoteamento = self.networkConnections[fila.queueName]

                nomeFilaDestino = self.defineDestino(probabilidadesRoteamento, aleatorio)

                if(nomeFilaDestino == "exit"):
                    self.escalonador.add(t0=fila.serviceInterval[0], t1=fila.serviceInterval[1], globalTime=self.tempo_global, tipo="saida", filaOrigem=fila)
                else:
                    filaDeDestino = next((queue for queue in self.filas if queue.queueName == nomeFilaDestino), None)
                    self.escalonador.add(t0=fila.serviceInterval[0], t1=fila.serviceInterval[1], globalTime=self.tempo_global, tipo="passagem", filaOrigem=fila, filaDestino = filaDeDestino)

                # if len(self.filas) == 1:
                #     if fila.status <= fila.servers:
                #         self.escalonador.add(t0=fila.serviceInterval[0], t1=fila.serviceInterval[1], globalTime=self.tempo_global, tipo="saida")
                # elif fila.status <= fila.servers:
                #     self.escalonador.add(t0=fila.serviceInterval[0], t1=fila.serviceInterval[1], globalTime=self.tempo_global, tipo="passagem", filaOrigem=fila, filaDestino=self.filas[1])
        else:
            fila.loss()
        self.escalonador.add(t0=fila.arrivalInterval[0], t1=fila.arrivalInterval[1], globalTime=self.tempo_global, tipo="chegada")

    def saida(self, evento):
        self.acumulaTempo(evento)
        fila = evento.filaOrigem
        fila.out()
        if fila.status >= fila.servers:
            self.escalonador.add(t0=fila.serviceInterval[0], t1=fila.serviceInterval[1], globalTime=self.tempo_global, tipo="saida", filaOrigem=fila)

    def passagem(self, evento):
        self.acumulaTempo(evento)

        origem = evento.filaOrigem
        destino = evento.filaDestino
        
        origem.out()
        if origem.status >= origem.servers:
            aleatorio = self.escalonador.retornaAleatorio()

            probabilidadesRoteamento = self.networkConnections[origem.queueName]

            nomeFilaDestino = self.defineDestino(probabilidadesRoteamento, aleatorio)

            if(nomeFilaDestino == "exit"):
                self.escalonador.add(t0=origem.serviceInterval[0], t1=origem.serviceInterval[1], globalTime=self.tempo_global, tipo="saida", filaOrigem=origem)                
            else:
                filaDeDestino = next((queue for queue in self.filas if queue.queueName == nomeFilaDestino), None)
                self.escalonador.add(t0=origem.serviceInterval[0], t1=origem.serviceInterval[1], globalTime=self.tempo_global, tipo="passagem", filaOrigem=origem, filaDestino = filaDeDestino)

        if destino.status < destino.capacity:
            destino.enter()
            if destino.status <= destino.servers:
                
                aleatorio = self.escalonador.retornaAleatorio()

                probabilidadesRoteamento = self.networkConnections[destino.queueName]

                nomeFilaDestino = self.defineDestino(probabilidadesRoteamento, aleatorio)

                if(nomeFilaDestino == "exit"):
                    self.escalonador.add(t0=destino.serviceInterval[0], t1=destino.serviceInterval[1], globalTime=self.tempo_global, tipo="saida", filaOrigem=destino)
                else:
                    filaDeDestino = next((queue for queue in self.filas if queue.queueName == nomeFilaDestino), None)
                    self.escalonador.add(t0=destino.serviceInterval[0], t1=destino.serviceInterval[1], globalTime=self.tempo_global, tipo="passagem", filaOrigem=destino, filaDestino = filaDeDestino)

        else:
            destino.loss()

    def acumulaTempo(self, evento):
        for fila in self.filas:
            # while len(fila.accumulator) < fila.status:
            #     fila.accumulator.append(0)
            fila.accumulator[fila.status] += (evento.time - self.tempo_global)

    def defineDestino(self,probabilidades, aleatorio):
        cumulativo = 0  
        for chave, valor in probabilidades.items():
            cumulativo += valor
            if aleatorio < cumulativo:
                if chave == "exit":
                    return "exit"
                else:
                    return chave
