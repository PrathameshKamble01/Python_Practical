'''
Title:
    Dictionary Exercises

Prerequisites:
    Basic knowledge of Python dictionaries.

Objectives:

    Create a dictionary of favorite books and their authors.
    Add a new book to the dictionary and print the updated dictionary.
    Remove a book from the dictionary and print the updated dictionary.
    Use the keys() method to print a list of book titles in the dictionary.
    Use the values() method to print a list of author names in the dictionary.

'''

# Create a dictionary of favorite books and their authors
favorite_books = {
    "Harry Potter": "J.K. Rowling",
    "The Catcher in the Rye": "J.D. Salinger",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell"
}

# Print the dictionary of favorite books and authors
print("Favorite Books and Authors:")
for book, author in favorite_books.items():
    print(f"{book} by {author}")

# Add a new book to the dictionary
favorite_books["Pride and Prejudice"] = "Jane Austen"

# Print the updated dictionary
print("\nUpdated Favorite Books and Authors:")
for book, author in favorite_books.items():
    print(f"{book} by {author}")

# Remove a book from the dictionary
del favorite_books["1984"]

# Print the updated dictionary
print("\nUpdated Favorite Books and Authors after removing '1984':")
for book, author in favorite_books.items():
    print(f"{book} by {author}")

# Print a list of book titles using the keys() method
print("\nList of Book Titles:")
book_titles = list(favorite_books.keys())
print(book_titles)

# Print a list of author names using the values() method
print("\nList of Author Names:")
author_names = list(favorite_books.values())
print(author_names)
