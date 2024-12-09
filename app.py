import streamlit as st
import requests

# Title of the app
st.title("AI Doctor Chatbot")
st.subheader("Ask any medical question, and I'll try my best to assist!")

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2-xl"
headers = {"Authorization": f"Bearer Your_Key_API"}

# Function to query Hugging Face model
def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Initialize session state for chat history if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input with a unique key to avoid the StreamlitDuplicateElementId error
user_input = st.text_input("Your Question:", key="user_input")  # Use a unique key for the user input box

if user_input:
    # Add user input to session state messages
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Send input to Hugging Face model
    result = query_huggingface({"inputs": user_input})
    
    # Accessing the response safely (handling list structure)
    if isinstance(result, list) and len(result) > 0:
        ai_response = result[0].get("generated_text", "I'm not sure about that.")
    else:
        ai_response = "Sorry, something went wrong."
    
    # Add AI response to session state messages
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

# Display the chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**AI Doctor:** {msg['content']}")

st.markdown("### Medical Disclaimer")
st.markdown("This is an AI tool and **not a substitute for professional medical advice**.")
