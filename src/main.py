from retrieve import retrieve
from generate import generate

def main():
    query = "What is this document about?"
    context = retrieve(query)
    response = generate(context, query)
    print(response)

if __name__ == "__main__":
    main()
