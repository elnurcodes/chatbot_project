import streamlit as st
from chatbot import chatbot_response

# Streamlit UI
st.title("Book Chatbot")
st.write("Ask me anything about books!")

# User input
user_input = st.text_input("Your question:")

# Check if the user has pressed the 'Send' button
if st.button("Send"):
    if user_input:
        # Get the chatbot's response
        response = chatbot_response(user_input)
        # Display the response
        st.write("Chatbot:", response)
    else:
        st.write("Please enter a question.")

