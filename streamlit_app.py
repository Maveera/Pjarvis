import streamlit as st
from huggingface_hub import InferenceClient

# 1. Setup Client
# Set 'HF_TOKEN' in Streamlit Secrets (Settings > Secrets)
client = InferenceClient(api_key=st.secrets["HF_TOKEN"])

st.title("J.A.R.V.I.S. Core")

# 2. Mentorship Logic (Socratic Mentor)
SYSTEM_PROMPT = "You are JARVIS. Be a witty British mentor. Call the user Sir. Guide him with wisdom."

# 3. Handle Mobile Requests
# Your phone will call: https://your-app.streamlit.app/?prompt=Hello
user_input = st.query_params.get("prompt")

if user_input:
    response = ""
    # We use Llama 3.2 3B - Very fast and smart for mentorship
    messages = [{"role": "system", "content": SYSTEM_PROMPT}, 
                {"role": "user", "content": user_input}]
    
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct",
        messages=messages,
        max_tokens=200
    )
    
    reply = completion.choices[0].message.content
    st.header("JARVIS_RESPONSE_START")
    st.write(reply)
    st.header("JARVIS_RESPONSE_END")
