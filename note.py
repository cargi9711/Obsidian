class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.links = []

    def add_link(self, note_title):
        self.links.append(note_title)

    def __str__(self):
        return f"Note: {self.title}\nLinks: {', '.join(self.links)}"
