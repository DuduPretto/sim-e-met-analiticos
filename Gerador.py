# import matplotlib.pyplot as plt

class GeradorCongruenteLinear:
    def __init__(self, semente: int):
        self.a = 1664525
        self.c = 1013904223
        self.M = 4294967296
        self.ultimoNumero = semente
        self.counter = 0

    def geraPseudoAleatorio(self):
        if self.counter >= 100000:
            raise StopIteration("Limite de 100.000 números aleatórios alcançado.")
        
        self.ultimoNumero = (self.ultimoNumero * self.a + self.c) % self.M
        self.counter += 1  # Incrementa o contador
        return self.ultimoNumero / self.M
