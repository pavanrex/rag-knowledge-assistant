from ingest import ingest
from retrieve import retrieve
from generate import generate

def main():
    print("RAG Assistant (type 'exit' to quit)\n")
    
    chunks = ingest()
    
    while True:
        query = input("Enter your query: ")
        
        if query.lower() == "exit":
            print("Exiting...")
            break
        
        context = retrieve(query, chunks)
        response = generate(context, query)
        
        print("\nResponse:")
        print(response)
        print("-" * 40)

if __name__ == "__main__":
    main()
