import os

def load_documents():
    path = "data/sample.txt"
    with open(path, "r") as f:
        text = f.read()
    return text

def chunk_text(text, chunk_size=100):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def ingest():
    print("[Ingestion] Loading documents...")
    
    text = load_documents()
    chunks = chunk_text(text)
    
    print(f"[Ingestion] Created {len(chunks)} chunks")
    
    return chunks

if __name__ == "__main__":
    ingest()
