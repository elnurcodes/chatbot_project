import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect("books.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a books table
cursor.execute('''
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre TEXT,
    description TEXT
)
''')

# Insert sample book data
books = [
    (1, "Dune", "Frank Herbert", "Science Fiction", "A classic science fiction novel."),
    (2, "1984", "George Orwell", "Dystopian", "A dystopian novel about totalitarianism."),
    (3, "Pride and Prejudice", "Jane Austen", "Romance", "A romantic classic set in the 19th century."),
]

cursor.executemany('INSERT INTO books VALUES (?, ?, ?, ?, ?)', books)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database setup complete!")

