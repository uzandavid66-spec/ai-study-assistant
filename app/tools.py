def read_notes():
    """
    Reads all notes from the notes file.
    """
    try:
        with open("../data/notes.txt", "r", encoding="utf-8") as file:
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


def calculate(expression):
    """
    Evaluates a mathematical expression safely.
    """
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Invalid calculation."