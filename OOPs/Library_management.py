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
        
main = Book("Test", "ahmed", 2021)          
main.info()   

print("\n")    
        
harry_potter = Book("Harry Potter", "J.K. Rowling", 1997)
harry_potter.info()
print("\n")

nat_geo = NonFictionBook("National Geographic", "The world", 1888, "Science")   
nat_geo.info()         