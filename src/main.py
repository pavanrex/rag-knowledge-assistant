from ingest import ingest
from retrieve import retrieve
from generate import generate

def main():
    query = input("Enter your query: ")
    
    chunks = ingest()
    context = retrieve(query, chunks)
    response = generate(context, query)
    
    print("\nResponse:")
    print(response)

if __name__ == "__main__":
    main()
