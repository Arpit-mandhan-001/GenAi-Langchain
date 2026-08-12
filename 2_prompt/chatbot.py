from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

chat_history = [
    SystemMessage(content='you have to give answer in 1 line')
]

while True:
    user_input = input("You: ")
    if user_input ==  'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    print("AI: ", result.content[0]['text'])
    chat_history.append(AIMessage(content=result.content[0]['text']))

print(chat_history)