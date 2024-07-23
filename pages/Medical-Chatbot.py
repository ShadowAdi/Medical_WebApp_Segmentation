import streamlit as st
from gemini.creatingModel import get_gemini_response


st.set_page_config(
    page_title="MedBot",
    page_icon="😷",
)




st.header("MediBot")


if 'chat_history' not in st.session_state:
    st.session_state["chat_history"]=[]

prompt=st.chat_input("Enter your Queries",key="input")
USER = "user"
ASSISTANT = "assistant"

if prompt:
    response=get_gemini_response(prompt)
    st.session_state["chat_history"].append((USER,prompt))
    
    st.chat_message(USER).write(prompt)

    for chunk in response:
        st.chat_message(ASSISTANT).write(f"{chunk.text}")
        st.session_state["chat_history"].append((ASSISTANT,chunk.text))




st.divider()

if st.session_state["chat_history"] != []:
    st.subheader("Chat History")
    for sender, message in st.session_state["chat_history"]:
        st.chat_message(sender).write(message)

    btn=st.button("Clear Chat History")

    if btn:
        st.session_state["chat_history"]=[]