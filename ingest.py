from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os 

def ingest_documents(data_dir='data', vectorstore_dir='vectorstore'):
    print("Loading documents...")
    loader = DirectoryLoader(data_dir, glob="**/*.pdf", show_progress=True)
    documents = loader.load()

    print(f"Loaded {len(documents)} documents.")
    
    print("Chunking documents...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    for i, chunk in enumerate(chunks[:5]):  # Display first 5 chunks for verification
        print(f"Chunk {i+1}: {chunk.page_content[:100]}...\n")  # Display first 100 characters of
        # each chunk for quick verification
    if not os.path.exists(vectorstore_dir):
        os.makedirs(vectorstore_dir)
    print(f"Created {len(chunks)} chunks.")

    print("Generating embeddings (using sentence-transformers/all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("Storing in FAISS vectorstore...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(vectorstore_dir)

    print(f"Ingestion complete. Vectorstore saved to `{vectorstore_dir}/`")

if __name__ == "__main__":
    ingest_documents()
