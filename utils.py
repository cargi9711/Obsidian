def format_note(title, content):
    return f"# {title}\n\n{content}"

def link_notes(note_a, note_b):
    return f"[[{note_a}]] -> [[{note_b}]]"
