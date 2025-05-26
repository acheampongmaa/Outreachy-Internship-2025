'''Object Interaction by building a Library class that can store and manage the Book objects'''

#The Book class

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def is_modern(self):
        return self.year >= 2000 
    
    def summary(self):
        return f" '{self.title}' by {self.author} published in {self.year}."
    
    def is_written_by(self, author_name):
        return self.author.lower() == author_name.lower()
    
    def age(self, current_year):
        return current_year - self.year
    
    def recommend(self):
        print(f"If you enjoy good reads try '{self.title}' by {self.author}!")

    def update_year(self, new_year):
        self.year = new_year

#creating object

# my_book = Book("Eat that Frog", "Brain Tracy", 2001, "self help book")            
# print(my_book.is_modern())
# print(my_book.is_written_by("Brain Tracy"))
# print(my_book.age(2025))
# my_book.recommend()
# print(my_book.summary())
# my_book.update_year(2025)
# print(my_book.year)


class Library:
    def __init__(self):
        self.books = [] #this will store book objects
    
    def add_book(self, book):
        self.books.append(book)
        print(f" Added '{book.title}' by {book.author} to the Library.")

    def list_book(self):
        if not self.books:
            print("The library has no books yet.")
            return
        print("Books in the library:")
        for books in self.books:
            print(f"-{books.summary()}")

#creating book objects
book1=Book("Atomic Habits", "James Clear", 2018, "Self-help")
book2=Book("The Alchemist", "Paulo Coelho", 1988, "Fiction")

#creating a Library
my_library=Library()

#add books to library
my_library.add_book(book1)
my_library.add_book(book2)

#list books
my_library.list_book()