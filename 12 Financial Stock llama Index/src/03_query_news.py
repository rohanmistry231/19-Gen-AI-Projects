import os
import openai
from dotenv import load_dotenv
from llama_index import StorageContext, load_index_from_storage

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# new version of llama index uses query_engine.query()
query_engine = index.as_query_engine()

# response = query_engine.query("What are some near-term risks to Nvidia?")
# print(response)


response = query_engine.query("Tell me about Google's new supercomputer.")
print(response)





