from langchain_community.llms import Ollama     
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#creating my prompts

prompt = ChatPromptTemplate.from_messages(
    [
    ("system" ,'you are helpful assitant.please reaspond to the questions asked'),
    ("user","Questions:{question}")
    ]
)




#streamlit code
st.title("where should be begin !")
input_text = st.text_input("what question do you have")
#now weare using llm model (gamma2)

llm = Ollama(model="gemma2:latest")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

#validation based input
if input_text:
   st.write(chain.invoke({"question":input_text}))