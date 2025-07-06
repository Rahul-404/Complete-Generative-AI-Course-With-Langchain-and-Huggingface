import os
from dotenv import load_dotenv

import streamlit as st 

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] =os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ypu are a helpful assistant. Please respond to the question asked"),
        ("user", "Question: {question}"),
    ]
)

## streamlit framework
st.title("Langchain Ollama App with Mistral")
input_text = st.text_input("What quastion you have in mind?")

## Ollama mistral model
llm = OllamaLLM(
    model="mistral",
    temperature=0.1,
    max_tokens=1000,
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))