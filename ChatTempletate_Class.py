from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
import os

llm=ChatOpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    model="deepseek/deepseek-r1-0528:free",
    temperature=0.4
    
)

chattemp=ChatPromptTemplate([("system : Hey its you are the master of {Domain}"),
                            ("user:give me explaination in 5 lines about{Topic}")])


prompt=chattemp.invoke({'Domain':'cricket','Topic':'wicket'})

res=llm.invoke(prompt)
print(res.content)
