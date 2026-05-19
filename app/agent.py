from tools import search_notes, calculate, add_note


def process_question(question):
    """
    Processes user input and chooses the correct tool.
    """

    question = question.strip()

    if question == "help":
        return (
            "Available commands:\n"
            "- search <keyword>: search inside study notes\n"
            "- calculate <expression>: calculate a mathematical expression\n"
            "- add note <text>: add a new note to the notes database\n"
            "- help: show available commands\n"
            "- exit: quit the assistant"
        )

    if question.startswith("search "):
        keyword = question.replace("search ", "", 1)
        results = search_notes(keyword)

        if results:
            return "[AI] Results found:\n" + "\n".join(results)

        return "[AI] No results found."

    if question.startswith("calculate "):
        expression = question.replace("calculate ", "", 1)
        result = calculate(expression)

        return f"[AI] Calculation result: {result}"

    if question.startswith("add note "):
        note = question.replace("add note ", "", 1)
        return "[AI] " + add_note(note)

    return "[AI] Unknown command. Type 'help' to see available commands."