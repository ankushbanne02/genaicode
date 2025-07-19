from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


llm=ChatOpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    model="deepseek/deepseek-r1-0528:free",
    temperature=0.4
    
)


result=llm.invoke("What is apple")
print(result)
