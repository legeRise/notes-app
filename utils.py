# utils.py
# Helper functions for the notes app

def format_note(note):
    """
    Trims whitespace and capitalizes the note.
    Args:
        note (str): The note to format.
    Returns:
        str: The formatted note.
    """
    return note.strip().capitalize()
