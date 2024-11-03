class Library:
    # Initializing Constructor
    def __init__(self, list_of_books, nm):
        self.booklist = list_of_books
        self.name = nm
        self.BooksBeenBorrowed = {}


    def AddBooks(self, BookTitle):
        self.booklist.append(BookTitle) # Adding new Books in The List
        print(f"The {BookTitle} has been added to the Book List")
    

    def DisplayBooks(self):
        print(f"The available Books in the {self.name} Library")

        for Book in self.booklist:
            print(Book)

    
    def BorrowBooks(self, username, BookTitle):
        if BookTitle not in self.booklist:
            print(f"We are sorry wedo not have that Book with Title {BookTitle}")
        elif BookTitle in self.BooksBeenBorrowed:
            print(f"This Book is already been Borrowed by {self.BooksBeenBorrowed[BookTitle]}")
        else:
            self.BooksBeenBorrowed[BookTitle] = username
            print("The book data base has been Updated, you can take the Book NOW !")
    

    def returnBooks(self, BookTitle):
        if BookTitle in self.BooksBeenBorrowed:
            del self.BooksBeenBorrowed[BookTitle]
            print("Book has been returned")
        else:
            print("That Book was now Borrowed from us")


# Creating Objects
Obj1 = Library(["Python Programing", "Harry Potter", "C++ Basics", "Unity Tutorials"], "Codingal's Library")
