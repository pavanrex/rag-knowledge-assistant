def simple_retrieval(chunks, query):
    scored_results = []
    
    for chunk in chunks:
        score = chunk.lower().count(query.lower())
        scored_results.append((chunk, score))
    
    # sort by score (higher = more relevant)
    scored_results.sort(key=lambda x: x[1], reverse=True)
    
    # take top result
    top_chunk, top_score = scored_results[0]
    
    return top_chunk, top_score


def retrieve(query, chunks):
    print("[Retrieval] Searching for relevant chunks...")
    
    context, score = simple_retrieval(chunks, query)
    
    print(f"[Retrieval] Confidence score: {score}")
    
    return context
