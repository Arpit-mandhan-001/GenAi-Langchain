from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

messages = [
    SystemMessage(content="You only give answer in 2 line"),
    HumanMessage(content="tell me about langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content[0]["text"]))

print(messages)
