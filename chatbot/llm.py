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
from chatbot.memory import conversation 
def generate_response(message):
    conversation.append(
        { 'role': 'user',
          'content': message
        }
    )
    stream = chat(model='smollm2:360m',messages=conversation,
    #     {
    #         'role':'user',
    #         'content': message
    #     }
    # ],
    stream=True
    )
    answer = ""
    for chunk in stream:
        print(chunk.message.content,end='',flush=True)
        answer += chunk.message.content
    conversation.append(
        { 'role': 'assistant',
          'content': answer
        }
    )
    return answer

