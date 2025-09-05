
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

Model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite") # temperature for creativity

result = Model.invoke("Write a program to implement Doubly Linked List in Python")

print(result.content)