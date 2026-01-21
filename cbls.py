#Camous Book Lending System (CBLS)
books = {}
def add_book(book_id, title, author):
    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
}




def view_books():
    if not books:
        print("No books available")
    return
    for book_id, details in books.items():
        status = "Available" if details["available"] else "Borrowed"
    print(f"{book_id}: {details['title']} by {details['author']} - {status}")




def borrow_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book borrowed successfully")
    else:
        print("Book not available")




def return_book(book_id):
    if book_id in books and not books[book_id]["available"]:
        books[book_id]["available"] = True
        print("Book returned successfully")
    else:
        print("Invalid return attempt")




def main():
    while True:
        print("\nCampus Book Lending System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")


        choice = input("Select an option: ")


        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            add_book(book_id, title, author)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_id = input("Book ID: ")
            borrow_book(book_id)
        elif choice == "4":
            book_id = input("Book ID: ")
            return_book(book_id)
        elif choice == "5":
            break
        else:
            print("Invalid option")




if __name__ == "__main__":
    main()