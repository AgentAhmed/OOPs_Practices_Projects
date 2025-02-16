# Title :  Library Management System

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        
class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre
        
    def info(self):
        super().info()
        print(f"Genre: {self.genre}")   
        
class NonFictionBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic
        
    def info(self):
        super().info()
        print(f"Topic: {self.topic}")    
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def display_books(self):
        for book in self.books:
            book.info()
            print("\n")  
            
    def search_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        if found_books:
            print(f"Books by {author}:")
            for book in found_books:        
                    book.info()
                    print("\n")
                    
        else:
            print(f"No books by {author} found")     
            
    def search_year(self, start_year, end_year):
        found_books = []
        for book in self.books:
            if book.year >= start_year and book.year <= end_year:
                found_books.append(book)
        if found_books:
            print(f"Books between {start_year} and {end_year}:")
            for book in found_books:        
                    book.info()
                    print("\n")
                    
        else:
            print(f"No books between {start_year} and {end_year} found")
        
library = Library()

book1 = FictionBook("Harry Potter", "J.K. Rowling", 1997, "Fantasy")

book2 = FictionBook("The Alchemist", "Paulo Coelho", 1988, "Adventure") 

book3 = NonFictionBook("National Geographic", "The world", 1888, "Science") 

book4 = NonFictionBook("The power of habit", "Charles Duhigg", 2012, "Self-help")   

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# library.display_books()

library.search_author("J.K. Rowling")
library.search_year(1990, 2000)

# main = Book("Test", "ahmed", 2021)          
# main.info()   

# print("\n")    
        
# harry_potter = Book("Harry Potter", "J.K. Rowling", 1997)
# harry_potter.info()
# print("\n")

# nat_geo = NonFictionBook("National Geographic", "The world", 1888, "Science")   
# nat_geo.info()         