import streamlit as st
from chatbot import chatbot_response

# Streamlit UI
st.title("Book Chatbot")
st.write("Ask me anything about books!")

# User input
user_input = st.text_input("Your question:")
if st.button("Send"):
    response = chatbot_response(user_input)
    st.write("Chatbot:", response)

