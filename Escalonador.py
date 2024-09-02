class Escalonador:
    def __init__(self):
        self.eventos = []

    def add(self, evento):
        self.eventos.append(evento)
        self.eventos.sort(key=lambda x: x.tempo)

    def get(self):
        return self.eventos.pop(0)