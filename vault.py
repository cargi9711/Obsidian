class Vault:
    def __init__(self, name):
        self.name = name
        self.notes = {}

    def add_note(self, note):
        self.notes[note.title] = note

    def get_note(self, title):
        return self.notes.get(title)

    def list_notes(self):
        return list(self.notes.keys())
