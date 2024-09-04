class Fila:
    def __init__(self, capacity: int, servers: int, arrivalInterval: tuple, serviceInterval: tuple):
        self.currentStatus = 0
        self.capacity = capacity
        self.servers = servers
        self.arrivalInterval = arrivalInterval
        self.serviceInterval = serviceInterval
        self.losses = 0
        self.accumulator = []
        for i in range(self.accumulator): # testar se não ta criando com uma posição a mais
            self.accumulator.append(0)

    def enter(self):
        self.status += 1

    def out(self):
        self.status -= 1

    def loss(self):
        self.losses += 1
