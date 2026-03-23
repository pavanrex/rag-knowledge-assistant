# RAG Knowledge Assistant

This project implements a simple retrieval-augmented generation (RAG) system that answers user queries based on custom documents.

## What it does
- Processes and chunks input documents
- Generates embeddings for each chunk
- Stores them in a vector database
- Retrieves relevant context for a given query
- Uses an LLM to generate responses grounded in retrieved data

## How it works
1. Documents are split into smaller chunks  
2. Each chunk is converted into embeddings  
3. Query is embedded and matched against stored data  
4. Relevant context is retrieved  
5. LLM generates an answer using this context  

## Why I built this
I wanted to understand how modern LLM systems use external knowledge instead of relying only on pre-trained data, and how retrieval improves accuracy.

## Tech
Python, OpenAI API, ChromaDB, Embeddings, Semantic Search

## Structure
- data/ → raw documents  
- src/ → ingestion, retrieval, generation logic  

## Future Improvements
- Add evaluation metrics for response quality  
- Improve retrieval with better chunking strategies  
- Add simple UI for interaction  
