# app.py
# Main command-line interface for the notes app
from utils import format_note
from storage import save_note

def main():
    """
    Prompts the user to enter a note, formats it, saves it, and confirms saving.
    """
    note = input("Enter a note: ")
    print(f"before formatting: {note}")
    formatted = format_note(note)
    print(f"after formatting: {formatted}")
    save_note(formatted)
    print("Note saved!")
    print("v1 is working")

if __name__ == "__main__":
    main()


