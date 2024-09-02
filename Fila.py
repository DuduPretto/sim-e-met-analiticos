class Fila:
    def __init__(self):
        self.status = 0
        self.capacity = 10
        self.servers = 1
        self.losses = 0

    def enter(self):
        self.status += 1

    def out(self):
        self.status -= 1

    def loss(self):
        self.losses += 1