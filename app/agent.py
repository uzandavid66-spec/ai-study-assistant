from tools import search_notes, calculate


def process_question(question):
    """
    Processes user questions and executes commands.
    """

    if question.startswith("search "):
        keyword = question.replace("search ", "")
        results = search_notes(keyword)

        if results:
            return "\n".join(results)
        else:
            return "No results found."

    elif question.startswith("calculate "):
        expression = question.replace("calculate ", "")
        return str(calculate(expression))

    else:
        return "Unknown command."