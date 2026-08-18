class book:
    def __init__(self,book_title,author):
        self.book_title=book_title
        self.author=author
        self.avalability=True
class library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print("Book Added Sucessfully.")
    
    def display_allBooks(self):
        if len(self.books) == 0:
            print ("All books are borrowed.")
        else:
            for book in self.books:
                status= "Available" if book.avalability else "Borrowed"
                print(f"Title : {book.book_title}")
                print(f"Author: {book.author}")
                print(f"Status:  {status}")
    def Borrow_book(self,title):
        for book in self.books:
            if book.book_title.lower() == title.lower():
                if book.avalability:
                    book.avalability=False
                    print("Book Borrowed Sucessfully. ")
                    return
                else:
                    print("Book is Already borrowed")
                    return               
        print("Book Not Found.")
    def return_book(self,title):
        for book in self.books:
            if book.book_title.lower()==title.lower():
                if  not book.avalability:
                    book.avalability=True
                    print("Book Returned Sucessfully.")
                    return
                else:
                    print("Book is already Avaliable.")
                    return
        print("Book Not Found.")
book1=book("Jurassic Park","Michael Crichton")
book2=book("The Lost World : A Novel","Michael Crichton")

library=library()
library.add_book(book1)
library.add_book(book2)
        
while True:
    print("\n ===== Library System ===== ")
    print("1. Add Book.")
    print("2. Display Books.")
    print("3. Borrow Book.")
    print("4. Return Book.")
    print("5. Exit")
    choice= input("Enter your Choice: ")
    if choice == "1":
        title=input("Enter Book Title: ")
        author=input("Enter Author Name: ")
        new_book=book(title,author)
        library.add_book(new_book)
    elif choice =="2":
        library.display_allBooks()
    elif choice =="3":
        title=input("Enter Book name to borrow: ")
        library.Borrow_book(title)
    elif choice=="4":
        title=input("Enter Book title to return: ")
        library.return_book(title)
    elif choice=="5":
        print("Exiting...............")
        break
    else:
        print("Invalid Choice")
avalable