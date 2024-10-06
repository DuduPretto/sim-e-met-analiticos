class Fila:
    def __init__(self, capacity: int, servers: int, arrivalInterval: tuple, serviceInterval: tuple):
        self.status = 0 # customers
        self.capacity = capacity
        self.servers = servers
        self.arrivalInterval = arrivalInterval
        self.serviceInterval = serviceInterval
        self.losses = 0
        self.accumulator = [0] * (capacity + 1) # Times
       

    def enter(self):
        self.status += 1

    def out(self):
        self.status -= 1

    def loss(self):
        self.losses += 1
