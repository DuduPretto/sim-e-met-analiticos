class Evento:
    def __init__(self, type, time):
        self.type = type
        self.time = time

    def __str__(self):
        return f"{self.type} - {self.time}"