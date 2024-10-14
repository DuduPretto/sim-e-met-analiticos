class Fila:
    def __init__(self, queueName: str, capacity: int, servers: int, arrivalInterval: tuple, serviceInterval: tuple):
        self.queueName = queueName
        self.status = 0 # customers
        self.capacity = capacity
        self.servers = servers
        self.arrivalInterval = arrivalInterval
        self.serviceInterval = serviceInterval
        self.losses = 0
        if capacity == 999:
            self.accumulator = [0] * 50 # Start with an empty list if infinite capacity
        else:
            self.accumulator = [0] * (capacity + 1)  # Times for finite capacity
       
    def enter(self):
        self.status += 1

    def out(self):
        self.status -= 1

    def loss(self):
        self.losses += 1

    def print(self):
        print(f"Queue Name: {self.queueName}")
        print(f"Capacity: {self.capacity}")
        print(f"Servers: {self.servers}")
        print(f"Arrival Interval: {self.arrivalInterval}")
        print(f"Service Interval: {self.serviceInterval}")
        print(f"Losses: {self.losses}")
        print(f"Accumulator: {self.accumulator}")