from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

Model = ChatOpenAI(model="gpt-4", temperature=0.5, max_completion_tokens=10) # temperature for creativity

result = Model.invoke("Write a poem on Football")

print(result.content)