import os
import streamlit as st
import chromadb
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

# Open AI API key Environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize Chroma Presistant Client - Chroma_db
chroma_client = chromadb.PersistentClient(path="chroma_db")

# OpenAI embeddings
embeddings = OpenAIEmbeddings(api_key=openai_api_key)

# Load vector store from Chroma_db collection
vector_store = Chroma(
    client=chroma_client,
    embedding_function=embeddings,
    persist_directory="chroma_db"
)

# Create retriever from Chroma vector store
retriever = vector_store.as_retriever()

# Initializing the language model- Gpt-3.5-turbo
llm = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=openai_api_key)

# Creating a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Streamlit UI- Front end Configration
st.set_page_config(page_title="CSV-Insight Chatbot", layout="wide")

st.sidebar.title("Chat Assistant")
st.sidebar.markdown("""
Simply type your queries, and our intelligent system will deliver the answers you need.

""")

st.title("CSV-Insight Chatbot")
st.markdown("**Hello, Welocme i am chat Assistant! Ask me anything about the CSV content**")

# Initializing  chat history to Store chats
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello, I am Chat Assistant. How can I help you?"}
    ]

# Get user input Query
user_query = st.chat_input("Type Your Questions Here...")


if user_query:
    try:
        # Add user query to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_query})

        
        with st.spinner("Thinking..."):
            response = qa_chain.invoke({"query": user_query})

        # Add bot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response["result"]})

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")




# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])
    elif message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
