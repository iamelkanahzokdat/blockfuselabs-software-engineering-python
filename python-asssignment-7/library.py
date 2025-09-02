"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.


library = []

def add_book(book):
    Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    

def search_books(search_param):
    Search for books by multiple keywords (title, author).
    return books that match search description.
    

def borrow_book(book_id):
    Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
"""

library = []

def add_book(book_id, title, author, **kwargs):
    """Add a new book into the library with flexible details."""
    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    # Add extra optional details (e.g., year, genre)
    for key, value in kwargs.items():
        book[key] = value
    library.append(book)
    return f"Book {title} added successfully!"

def search_books(*args):
    """Search for books by multiple keywords (title, author)."""
    results = []
    for book in library:
        for arg in args:
            if arg in book['title'] or arg in book['author']:
                results.append(book)
                break   # stop checking more args once matched
    return results

def borrow_book(book_id):
    """Borrow a book if available."""
    for book in library:
        if book['id'] == book_id:
            if book['available']:
                book['available'] = False
                return f"You borrowed {book['title']}."
            else:
                return f"Book {book['title']} not available."
    return "Book ID not found."

def return_book(book_id):
    """Return a borrowed book."""
    for book in library:
        if book['id'] == book_id:
            if not book['available']:
                book['available'] = True
                return f"You returned {book['title']}."
            else:
                return f"Book {book['title']} was not borrowed."
    return "Book ID not found."



print(add_book(1, "Things Fall Apart", "Chinua Achebe", year=1958, genre="Classic"))
print(add_book(2, "Half of a Yellow Sun", "Chimamanda Ngozi Adichie", year=2006, genre="Historical Fiction"))
print(add_book(3, "Clean Code", "Robert C. Martin", year=2008, genre="Programming"))

print("\n--- Search Results ---")
print(search_books("Chinua", "Achebe"))

print("\n--- Borrowing Books ---")
print(borrow_book(2))   
print(borrow_book(2))   

print("\n--- Returning Books ---")
print(return_book(2))  
print(return_book(2))   