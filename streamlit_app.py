import streamlit as st
from llama_cpp import Llama
import os

# 1. Load the Model (Jarvis's Local Brain)
# We use a cached function so the model only loads once
@st.cache_resource
def load_jarvis():
    # You will need to upload a .gguf file to your repo or download it via code
    # For this example, we assume 'jarvis_model.gguf' is in your repo
    return Llama(model_path="jarvis_model.gguf", n_ctx=2048)

st.title("J.A.R.V.I.S. Core (Private LLM)")

# 2. Mentorship Logic
llm = load_jarvis()

# 3. Create an API-like receiver for your Mobile App
# URL format: https://your-app.streamlit.app/?prompt=hello
prompt = st.query_params.get("prompt")

if prompt:
    st.write(f"Incoming Command: {prompt}")
    output = llm(
        f"Q: You are JARVIS, a mentor. Answer this briefly and call me Sir: {prompt} A:", 
        max_tokens=100, 
        stop=["Q:", "\n"]
    )
    response_text = output["choices"][0]["text"]
    st.header("JARVIS Response:")
    st.write(response_text) # Your mobile app will "read" this text
