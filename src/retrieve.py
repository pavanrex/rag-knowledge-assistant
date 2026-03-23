def simple_retrieval(chunks, query):
    # naive keyword match (shows logic)
    results = [chunk for chunk in chunks if query.lower() in chunk.lower()]
    
    if not results:
        return chunks[:1]  # fallback
    
    return results

def retrieve(query, chunks):
    print(f"[Retrieval] Searching for relevant chunks...")
    
    results = simple_retrieval(chunks, query)
    
    return " ".join(results)
