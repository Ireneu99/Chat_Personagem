import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA

@st.cache_resource
def carregar_chain():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="app/db", embedding_function=embeddings)
    retriever = db.as_retriever()
    llm = Ollama(model="mistral")
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain

# --- INTERFACE ---
st.set_page_config(page_title="Chat com Fernando Pessoa", page_icon="📜")
st.title("📚 Chat com Fernando Pessoa")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

pergunta = st.chat_input("Faça uma pergunta a Fernando Pessoa...")

if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    chain = carregar_chain()
    prompt = f"Responda em português como se fosse Fernando Pessoa. Pergunta: {pergunta}"
    resposta = chain.run(prompt)
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})

# Mostrar histórico
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
