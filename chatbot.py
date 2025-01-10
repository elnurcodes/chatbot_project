from transformers import AutoModelForCausalLM, AutoTokenizer
import sqlite3
import pandas as pd

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Query function for books database
def query_books(keyword):
    conn = sqlite3.connect("books.db")
    query = f"SELECT * FROM books WHERE genre LIKE '%{keyword}%' OR title LIKE '%{keyword}%'"
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

# Chatbot logic
def chatbot_response(user_input):
    if "recommend" in user_input.lower():
        keyword = user_input.split("recommend")[-1].strip()
        books = query_books(keyword)
        if not books.empty:
            book = books.iloc[0]
            return f"I recommend: {book['title']} by {book['author']} - {book['description']}"
        else:
            return "I couldn't find any books in that category. Try another genre!"
    else:
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        outputs = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        return response

# Test chatbot
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

