🧠 Chat com Personagem Histórico — Fernando Pessoa (LangChain)
Este projeto permite conversar com Fernando Pessoa, simulando seu estilo e ideias com base em textos reais do autor. Foi construído com foco em LangChain, vetorização semântica e modelos LLM gratuitos, com objetivo de funcionar localmente e sem custos.

✅ Funcionalidades atuais
🔎 Vetorização de textos reais (Livro do Desassossego) com ChromaDB
💬 Chatbot funcional via terminal
🧠 Uso do modelo GPT-3.5-Turbo da OpenAI (temporário)
🧱 Estrutura modular para uso futuro de outros autores
📦 Código organizado e pronto para extensão com interface visual (Streamlit)
📁 Estrutura do projeto
chat_personagem/ ├── .env # API Key (OpenAI) - opcional ├── extract_pdf.py # Conversão PDF → .txt ├── requirements.txt │ ├── app/ │ ├── main.py # Chat via terminal │ ├── chat_app.py # (em desenvolvimento) Interface web com Streamlit │ ├── documents/ │ │ ├── livro_do_desassossego.pdf │ │ └── personagem.txt │ └── db/ # Base vetorial (Chroma)

Substituir o uso da API da OpenAI por um modelo local gratuito com Ollama.

Como mudar para Ollama:
Instale o Ollama (https://ollama.com/download)
Rode o modelo local no terminal:
ollama run llama3

Antes (OpenAI)
from langchain.chat_models import ChatOpenAI llm = ChatOpenAI(model_name="gpt-3.5-turbo")

Depois (modelo local)
from langchain_community.llms import Ollama llm = Ollama(model="llama3")

1. Ativar o ambiente virtual
.\venv\Scripts\activate # Windows

2. Rodar o modelo local (em breve)
ollama run llama3

3. Executar o chatbot
python app/main.py