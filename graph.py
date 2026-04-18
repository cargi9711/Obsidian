class Graph:
    def __init__(self):
        self.connections = {}

    def connect(self, note_a, note_b):
        self.connections.setdefault(note_a, []).append(note_b)
        self.connections.setdefault(note_b, []).append(note_a)

    def show(self):
        return self.connections
