import chatbot.llm
# message = input("Enter a message: ")
# response= chatbot.llm.generate_response(message)
while True:
    message = input("\nEnter a message: ")
    # response= chatbot.llm.generate_response(message)

    if message == "exit":
        print("yes")
        break
    response= chatbot.llm.generate_response(message)

