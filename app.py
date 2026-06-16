import chatbot.llm
message = input("Enter a message: ")
response= chatbot.llm.generate_response(message)
print(response)


