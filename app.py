# app.py
# Flask web application for the notes app
from flask import Flask, render_template, request, redirect, url_for
from utils import format_note
from storage import save_note, load_notes, clear_notes

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page with all saved notes."""
    notes = load_notes()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    """Take a note from the form, format it, and save it."""
    note = request.form.get("note", "").strip()
    if note:
        formatted = format_note(note)
        save_note(formatted)
    return redirect(url_for("index"))


@app.route("/clear", methods=["POST"])
def clear_all():
    """Delete all notes."""
    clear_notes()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

