# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []
        
    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b
    
    #Only available to admin
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
        
    def searchByName(self,book,name):
        for book in self.books:
            if book.name == name:
                book.printBook()
            
            
            
            
 
    
    def searchByAuthor(self,author):
        pass
    
        
    def displayAllBooks(self):
        print ('Different Book Count',self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        
        print ('Total Book Count',c)
