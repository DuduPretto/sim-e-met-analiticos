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

# Usage
# semente = 1  # Initial seed for the generator
# gerador = GeradorCongruenteLinear(semente)
# numerosAleatorios = []

# # Gerando números
# for i in range(1000):
#     numerosAleatorios.append(gerador.geraPseudoAleatorio())

# # Preparando dados para o gráfico de dispersão
# x = range(len(numerosAleatorios))
# y = numerosAleatorios

# # Criando o gráfico de dispersão
# plt.scatter(x, y, alpha=0.5)
# plt.title('Dispersão dos números pseudo-aleatórios')
# plt.xlabel('')
# plt.ylabel('')
# plt.show()