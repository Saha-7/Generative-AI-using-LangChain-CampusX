from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

from langchain_huggingface import ChatHuggingFace
model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the best Footballer of all time ?")
print(result.content)
