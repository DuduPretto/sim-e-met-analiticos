class Evento:
    def __init__(self, tipo, tempo):
        self.tipo = tipo
        self.tempo = tempo

    def __str__(self):
        return f"{self.tipo} - {self.tempo}"