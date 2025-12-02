# tightly coupled
from chat import JokeBot
import streamlit as st 

def init_session_states():
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    if "bot" not in st.session_state:
        st.session_state.bot = JokeBot()
        
def display_chat_messages():
    """Iterate over all historical messages and display them"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            
def handle_user_input():
    
    if prompt := st.chat_input("Joke with JokBot"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        bot_response = st.session_state.bot.chat(prompt).get("bot")
        
        response = f"Ro Båt: {bot_response}"
        
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            st.markdown(response)
            
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        
def layout():
    st.markdown("# Chat with RoBÅT")
    st.markdown("RoBÅT is a funny robot that jokjes about programming")
    
    display_chat_messages()
    handle_user_input()
    
if __name__=="__main__":
    
    init_session_states()
    layout()
