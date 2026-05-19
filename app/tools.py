import os


NOTES_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "notes.txt")


def read_notes():
    """
    Reads all notes from the notes file.
    """
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return ["Error: notes.txt file not found."]


def search_notes(keyword):
    """
    Searches for a keyword inside the notes file.
    """
    notes = read_notes()
    results = []

    for line in notes:
        if keyword.lower() in line.lower():
            results.append(line.strip())

    return results


def add_note(note):
    """
    Adds a new note to the notes file.
    """
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write("\n" + note)

    return "Note added successfully."


def calculate(expression):
    """
    Evaluates a mathematical expression safely.
    """
    try:
        allowed_characters = "0123456789+-*/(). "
        for character in expression:
            if character not in allowed_characters:
                return "Invalid calculation."

        result = eval(expression)
        return result

    except Exception:
        return "Invalid calculation."