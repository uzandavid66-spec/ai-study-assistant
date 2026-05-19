from agent import process_question


def main():
    """
    Main entry point of the AI Study Assistant.
    """

    print("AI Study Assistant")
    print("Type 'help' to see available commands.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = process_question(user_input)
        print(response)


if __name__ == "__main__":
    main()