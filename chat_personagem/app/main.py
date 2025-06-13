from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def carregar_chain():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="app/db", embedding_function=embeddings)
    retriever = db.as_retriever()
    llm = Ollama(model="llama3")
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain

if __name__ == "__main__":
    print("🤖 Chat com Fernando Pessoa iniciado! (Digite 'sair' para encerrar)\n")
    chain = carregar_chain()

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("👋 Encerrando...")
            break
        resposta = chain.run(pergunta)
        print(f"Pessoa: {resposta}\n")
