from tools import search_notes, calculate, add_note
from memory import save_memory, load_memory


def process_question(question):
    """
    Processes user input and chooses the correct tool.
    """

    question = question.strip()

    # Save user message
    save_memory("USER: " + question)

    # HELP COMMAND
    if question == "help":

        response = (
            "Available commands:\n"
            "- search <keyword>: search inside study notes\n"
            "- calculate <expression>: calculate a mathematical expression\n"
            "- add note <text>: add a new note to the notes database\n"
            "- memory: show conversation memory\n"
            "- help: show available commands\n"
            "- exit: quit the assistant"
        )

        save_memory("AI: help command used")

        return response

    # MEMORY COMMAND
    if question == "memory":

        memory = load_memory()

        if not memory:
            return "[AI] No memory found."

        response = "[AI] Conversation memory:\n" + "".join(memory)

        save_memory("AI: memory displayed")

        return response

    # SEARCH COMMAND
    if question.startswith("search "):

        keyword = question.replace("search ", "", 1)

        results = search_notes(keyword)

        if results:
            response = "[AI] Results found:\n" + "\n".join(results)
        else:
            response = "[AI] No results found."

        save_memory(response)

        return response

    # CALCULATE COMMAND
    if question.startswith("calculate "):

        expression = question.replace("calculate ", "", 1)

        result = calculate(expression)

        response = f"[AI] Calculation result: {result}"

        save_memory(response)

        return response

    # ADD NOTE COMMAND
    if question.startswith("add note "):

        note = question.replace("add note ", "", 1)

        response = "[AI] " + add_note(note)

        save_memory(response)

        return response

    # UNKNOWN COMMAND
    response = "[AI] Unknown command."

    save_memory(response)

    return response