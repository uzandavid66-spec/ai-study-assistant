from agent import process_question


print("AI Study Assistant")
print("Type 'exit' to quit.")


while True:

    user_input = input(">> ")

    if user_input.lower() == "exit":
        break

    response = process_question(user_input)

    print(response)