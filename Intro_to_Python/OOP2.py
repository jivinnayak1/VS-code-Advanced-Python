class Library:
    global book
    book = []
    def __init__(self, libname):
        self.libname = libname

    def addBook(self, bookname):
        if bookname not in book:
            book.append(bookname)
            print(f"{bookname} added to the library")
        else:
            print(f"Error. Attempt to add {bookname}. This book is already available in the library")

    def SellBook(self, bookname):
        if bookname in book:
            book.remove(bookname)
            print(f"{bookname} sold")
        else:
            print(f"{bookname} not available in the library")
    def ShowBook(self):
        if book:
            print("Availible Books-")
            for item in book:
                print(item)
        else:
            print("No book available in the library")


inl = Library("Indian National Library")
inl.addBook("Harry Potter")
inl.addBook("The Alchemist")
inl.addBook("The Ice Monster")
inl.addBook("The Alchemist")
inl.SellBook("Harry Potter")
inl.SellBook("The Alchemist")
inl.SellBook("The Ice Monster")
inl.ShowBook()
