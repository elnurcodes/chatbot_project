# Book Chatbot

This project is a chatbot that provides book recommendations and general conversation based on the user's input. It integrates a conversational AI model (`DialoGPT-small`) from Hugging Face for general responses, and a local SQLite database (`books.db`) to recommend books based on the genre or title.

## Features

- **Book Recommendations**: The chatbot can recommend books from a database based on the genre or title mentioned by the user.
- **General Conversation**: It uses the `DialoGPT-small` model to generate responses for casual conversation.
- **Web Interface**: The chatbot is available via a simple Streamlit web app, where users can interact with it.

## Prerequisites

To run this project, you need the following:

- Python 3.7 or later
- Libraries: `transformers`, `torch`, `pandas`, `streamlit`, and `sqlite3`
  
### Install Required Libraries

You can install the required libraries by running the following command in your terminal:

```bash
pip install transformers torch pandas streamlit sqlite3

