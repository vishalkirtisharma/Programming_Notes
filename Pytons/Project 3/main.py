
class Library:

    def  __init__(self,listofbook):
        self.books=listofbook

    def displaybooks(self):
        print("The books avalale in library are: ")
        for book in self.books:
            print(" *" + book)

    def borrow(self,bookname):
        if bookname in self.books:
            print(f"{bookname} issue to you.")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry book not available in current stock")
            return False
    
    def returnbook(self,bookname):
        print("Thanks for return this book")
        self.books.append(bookname)


class Student:
    # def __init__(self):
    #     self.book = []

    def requestbooks(self):
        self.book= input("Enter the name of the book for borrow: ")
        # reqbooks= input("Enter the name of the borrow")
        # self.book.append(reqbooks)
        return self.book

    def returnbooks(self):
        self.book= input("Enter the name of the books for return: ")
        # reqbooks= input("Enter the name of the borrow")
        # self.book.append(reqbooks)
        return self.book


# Project start from here
if __name__ == "__main__":
    Books=["Python","C","Java","Django","Data Science"]

    Centerlibrary=Library(Books)
    Students=Student()
    # Centerlibrary.displaybooks()

    while True:
        msg='''Welcome to code! Please select option
        Please select below option
        1. Show all books
        2. Request a book
        3. Return a book
        4. Exit this code
        '''
        print(msg)
        a=int(input("Please enter your choice: "))
        if a==1:
            Centerlibrary.displaybooks()
        elif a==2:
            Bookname=Students.requestbooks()
            Centerlibrary.borrow(Bookname)
        elif a==3:
            Bookname= Students.returnbooks()
            Centerlibrary.returnbook(Bookname )
        elif a==4:
            print("Thanks for use this code.")
            exit()

        else:
            print("Invalid choice")


