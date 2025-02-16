from src.helper import repo_ingestion, load_repo, text_splitter, load_embedding
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
import os

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY



# url = "https://github.com/entbappy/End-to-end-Medical-Chatbot-Generative-AI"

# repo_ingestion(url)


documents = load_repo("repo/")
text_chunks = text_splitter(documents)
embeddings = load_embedding()



#storing vector in choramdb
vectordb = Chroma.from_documents(text_chunks, embedding=embeddings, persist_directory='./db')
vectordb.persist()