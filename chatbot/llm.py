# from ollama import chat
# from ollama import ChatResponse 

# def generate_response(message):
#     response: ChatResponse = chat(model='smollm2:360m',messages=[
#         {
#             'role':'user',
#             'content':message
#          },
#     ])
#     return response.message.content


from ollama import chat 
def generate_response(message):
    stream = chat(model='smollm2:360m',messages=[
        {
            'role':'user',
            'content':message
        }
    ],
    stream=True
    )
    for chunk in stream:
        print(chunk.message.content,end='',flush=True)

