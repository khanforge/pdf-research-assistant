import streamlit as st
from config import settings

st.set_page_config(page_title="Agentic RAG", layout="wide")

st.title("Agentic RAG")
st.markdown("Build a retrieval-augmented generation assistant with agentic workflows.")

st.sidebar.title("Configuration")
st.sidebar.write(f"Model: {settings.model_name}")

st.write("Use the sidebar to upload documents and start the agent.")
