from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env
load_dotenv()

# Initialize OpenRouter+DeepSeek model
llm = ChatOpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),       # OpenRouter endpoint like https://openrouter.ai/api/v1
    api_key=os.getenv("OPENAI_API_KEY"),         # Your OpenRouter API key
    model="deepseek/deepseek-r1-0528:free" ,     # Free DeepSeek model via OpenRouter
    temperature=0.7
)
# Step 1: Define the template
template = PromptTemplate(
    template="Write about {topic}. Give some history in {length} lines.",
    input_variables=["topic", "length"]
)
# Step 2: Fill the template with actual values
filled_prompt = template.format(
    topic="Artificial Intelligence",
    length="5"
)
# Step 3: Use the filled prompt
response = llm.invoke(filled_prompt)

# Output result
print(response.content)
