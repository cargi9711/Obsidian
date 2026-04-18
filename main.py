from note import Note
from vault import Vault
from graph import Graph

vault = Vault("My Vault")
graph = Graph()

note1 = Note("Obsidian Basics", "Markdown system")
note2 = Note("Graph View", "Connections")

note1.add_link("Graph View")

vault.add_note(note1)
vault.add_note(note2)

graph.connect(note1.title, note2.title)

print(vault.list_notes())
print(graph.show())
