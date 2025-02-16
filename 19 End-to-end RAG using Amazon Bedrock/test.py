from langchain.llms.bedrock import Bedrock
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import boto3
import streamlit as st


#Bedrock client

bedrock_client = boto3.client(
    service_name = "bedrock-runtime",
    region_name = "ap-south-1",
)

model_id = "mistral.mistral-7b-instruct-v0:2"


llm = Bedrock(
    model_id= model_id,
    client= bedrock_client,
    model_kwargs={"temperature": 0.9}
)



def my_chatbot(language, user_text):
    prompt = PromptTemplate(
        input_variables=["language", "user_text"],
        template="You are a chatbot. You are in {language}.\n\n{user_text}"
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt)
    response=bedrock_chain({'language':language, 'user_text':user_text})

    return response



st.title("Bedrock Chatbot Demo")

language = st.sidebar.selectbox("Language", ["english", "spanish", "hindi"])

if language:
    user_text = st.sidebar.text_area(label="what is your question?",
    max_chars=100)


if user_text:
    response = my_chatbot(language,user_text)
    st.write(response['text'])