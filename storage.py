# storage.py
# Handles saving and loading notes
# Imports

def save_note(note):
    """
    Appends the note to data/notes.txt.
    Args:
        note (str): The note to save.
    """
    print("Saving note...")
    with open('data/notes.txt', 'a', encoding='utf-8') as f:
        f.write(note + '\n')
