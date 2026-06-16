from ollama import chat
from ollama import ChatResponse 

def generate_response(message):
    response: ChatResponse = chat(model='smollm2:360m',messages=[
        {
            'role':'user',
            'content':message
         },
    ])
    return response.message.content
    



