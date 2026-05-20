import os


MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "memory.txt"
)


def save_memory(message):
    """
    Saves a message into memory.
    """

    with open(MEMORY_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")


def load_memory():
    """
    Loads all memory entries.
    """

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        return []