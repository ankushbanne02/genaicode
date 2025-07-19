from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt

# Load environment variables
load_dotenv()

# Initialize the model
llm = ChatOpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    model="deepseek/deepseek-r1-0528:free",
    temperature=0.7
)

# Load and fill prompt
template = load_prompt("template.json")  # loaded as a PromptTemplate
filled_prompt = template.format(topic="Artificial Intelligence")  # Provide input values

# Invoke model with the filled prompt string
response = llm.invoke(filled_prompt)

# Print result
print(response.content)
