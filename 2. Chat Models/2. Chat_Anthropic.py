
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

Model = ChatAnthropic(model="claude-opus-4-1-20250805") # temperature for creativity

result = Model.invoke("Write a program to implement Doubly Linked List in Python")

print(result.content)