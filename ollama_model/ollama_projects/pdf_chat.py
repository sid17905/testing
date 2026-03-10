from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader("document.pdf")
documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OllamaEmbeddings(model="llama3.1")

# Store in vector DB
db = Chroma.from_documents(docs, embeddings)

# Load LLM
llm = Ollama(model="llama3.1")

print("PDF Chat Ready! Type 'exit' to quit.\n")

while True:

    query = input("Ask: ")

    if query == "exit":
        break

    results = db.similarity_search(query)

    context = "\n".join([doc.page_content for doc in results])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

    response = llm(prompt)

    print("\nAI:", response)
    print("\n-------------------\n")