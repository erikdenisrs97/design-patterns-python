class Author: # Low
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_author_info(self):
        return f"{self.name} was born in {self.birth_year}."
    
class Book: # High
    def __init__(self, title, pub_year, author: Author):
        self.title = title
        self.pub_year = pub_year
        self.author = author

    def get_book_info(self):
        return f"{self.title} was published in {self.pub_year} by {self.author}."
    
author_obj = Author("George Orwell", 1903)

book_obj = Book("1984", 1949, author_obj)