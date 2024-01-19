import sqlite3

import datetime
class Book():
    def __init__(self, bookName, authorName, status = "Not started"):
        self.name = bookName
        self.author = authorName
        self.status = status
        # self.start = None
        # self.end = None
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                name text, 
                author text, 
                status text
                )
                """)
        self.cursor.execute("INSERT INTO books VALUES (?, ?, ?)", (self.name, self.author, self.status))
        self.conn.commit()
        print(f"- Book '{self.name}' by '{self.author}' is added to the library.\n")


    # def start_reading(self):
    #     self.start = datetime.datetime.now()
    #     formatted_date = self.start.strftime("%A, %-dth %b. %Y")
    #     self.status = "Reading"
    #     print(f"- Book '{self.name}' by '{self.author}' started reading since {formatted_date}\n")
        
    # def end_reading(self):
    #     self.end = datetime.datetime.now()
    #     formatted_date = self.start.strftime("%A, %-dth %b. %Y")
    #     self.status = "Finished"
    #     print(f"- Book '{self.name}' by '{self.author}' finished reading on {formatted_date}\n")

    def start_reading(self):
        self.status = "Reading"
        self.cursor.execute("UPDATE boosk SET status = ? WHERE name = ? AND author = ?", (self.status, self.naem, self.author))
        self.conn.commit()
class ReadingList:

    def __init__(self):
        self.books = []
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS reading_list(
                name text,
                author text,
                status text
            )
        """)
        
    def add_book(self, book):
        self.books.append(book)
        self.cursor.execute("INSERT INTO reading_list VALUES (?, ?, ?)", (self.name, self.author, self.status))
        self.conn.commit()
        print(f"{book.name} added to the reading list.")
    
    # def display_reading_list(self):
    #     for book in self.books:
    #         print(f"Title:      {book.name}")
    #         print(f"Author:     {book.author}")
    #         print(f"Status:     {book.status}")
    #         if book.start:
    #             start_date = book.start.strftime("%A, %-dth %b. %Y")
    #             print(f"Start:      {start_date}")
            
    #         if book.end:
    #             end_date = book.end.strftime("%A, %-dth %b. %Y")
    #             print(f"End:        {end_date}")