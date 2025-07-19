from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
import os


load_dotenv()

llm=ChatOpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    model="deepseek/deepseek-r1-0528:free"
)

history=[SystemMessage(content="act as mathematcial which give answer in prompt just give answer as it is dont explain it.")]
while True:
    user_input=input("User :")
    if user_input=="Exit":
        break
    history.append(HumanMessage(content=user_input))
    res=llm.invoke(history)
    history.append(AIMessage(content=res.content))
    print("AI:",res.content)

print(history)
