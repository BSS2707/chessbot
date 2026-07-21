import streamlit as st
import ollama

st.title("Chess ChatBot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def ask_ollama(prompt):
    response = ollama.chat(model="phi3:mini", messages=[
        {"role": "system", "content": "You are a chess tutor. Answer clearly and concisely."},
        *st.session_state["messages"],
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']

user_input = st.chat_input("Ask about chess...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    answer = ask_ollama(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": answer})

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
