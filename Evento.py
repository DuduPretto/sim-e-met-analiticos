class Evento:
    def __init__(self, type, time, filaOrigem, filaDestino):
        self.type = type
        self.time = time
        self.filaOrigem = filaOrigem
        self.filaDestino = filaDestino

    def __str__(self):
        return f"{self.type} - {self.time} - {self.filaOrigem} - {self.filaDestino}"