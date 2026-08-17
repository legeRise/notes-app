# storage.py
# Handles saving and loading notes
import os

NOTES_FILE = os.path.join(os.path.dirname(__file__), 'data', 'notes.txt')


def save_note(note):
    """
    Appends the note to data/notes.txt.
    Args:
        note (str): The note to save.
    """
    os.makedirs(os.path.dirname(NOTES_FILE), exist_ok=True)
    with open(NOTES_FILE, 'a', encoding='utf-8') as f:
        f.write(note + '\n')


def load_notes():
    """
    Reads all notes from data/notes.txt.
    Returns:
        list: A list of note strings.
    """
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def clear_notes():
    """
    Clears all notes in data/notes.txt.
    """
    os.makedirs(os.path.dirname(NOTES_FILE), exist_ok=True)
    open(NOTES_FILE, 'w').close()
