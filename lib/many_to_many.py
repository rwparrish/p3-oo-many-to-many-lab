import ipdb

class Author:
    
    def __init__(self, name):
        self.name = name
        self.books = set()
        self.contracts = set()
        
    def add_book(self, book):
        self.books.add(book)
        
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts.add(contract)
        book.contracts.add(contract)
    
    def total_royalties(self):
        total_royalties = []
        for c in self.contracts:
            total_royalties.append(c.royalties)
        return sum(total_royalties)
        


class Book:
    
    def __init__(self, title):
        self.title = title
        self.authors = set()
        self.contracts = set()
        
    def add_author(self, author):
        if isinstance(author, Author):
            self.authors.add(author)
        else:
            raise TypeError("Invalid types for author and/or book")
        
   

class Contract:
    
    all = []
    
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book):
            self.author = author
            self.book = book
            author.add_book(book)
            book.add_author(author)
            self.date = date
            self.royalties = royalties
            self.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        matching_dates = []
        for c in cls.all:
            if c.date == date:
                matching_dates.append(c)
        return matching_dates
       