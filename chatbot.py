from transformers import AutoModelForCausalLM, AutoTokenizer
import sqlite3
import pandas as pd

# Load the model and tokenizer from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Query function to search books in the database based on keyword (genre/title)
def query_books(keyword):
    conn = sqlite3.connect("books.db")
    query = f"SELECT * FROM books WHERE genre LIKE '%{keyword}%' OR title LIKE '%{keyword}%'"
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

# Chatbot response generation
def chatbot_response(user_input):
    if "recommend" in user_input.lower():  # Check if user is asking for book recommendations
        keyword = user_input.split("recommend")[-1].strip()  # Get the genre or title keyword
        books = query_books(keyword)
        if not books.empty:
            book = books.iloc[0]  # Get the first book from the search results
            return f"I recommend: {book['title']} by {book['author']} - {book['description']}"
        else:
            return "I couldn't find any books in that category. Try another genre or title!"
    else:
        # For any other query, generate a response from DialoGPT
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        return response

# Test chatbot functionality (CLI mode)
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

