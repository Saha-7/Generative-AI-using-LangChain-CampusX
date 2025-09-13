from langchain_community.embeddings import HuggingFaceEmbeddings

# Load a lightweight embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Delhi is the Capital of India"

# Convert text into a vector
vector = embedding.embed_query(text)

print("Vector:", str(vector))
print("Vector preview:", vector)  # show first 5 numbers
