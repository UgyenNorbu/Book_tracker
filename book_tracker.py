import sqlite3

import datetime
class Book():
    def __init__(self, bookName, authorName, status = "Not started"):
    def __init__(self, bookName, authorName, status = "Not started", available = "Yes"):
        """
        Initializes a book object.

        Args:
            bookName (str): Title of the book.
            authorName (str): Name of the author(s).
            status (str, optional): Reading status of the book. Defaults to "Not started".
            available (str, optional): Availability of the book. Defaults to "Yes".
        """
        self.name = bookName
        self.author = authorName
        self.status = status
        self.availability = available
        print(f"- Book '{self.name}' by '{self.author}' is created.")

    def start_reading(self, reading_list):
        """
        Updates the status of the book to "Reading".

        Args:
            reading_list (ReadingList): A reading list object which contains the books.
        """
        self.status = "Reading"
        reading_list._update_book_status(self)
        print(f"- Status of '{self.name}' updated to 'Reading'.")

    def complete_reading(self, reading_list):
        """
        Updates the status of the book to "Completed".

        Args:
            reading_list (ReadingList): A reading list object which contains the books.
        """
        self.status = "Completed"
        reading_list._update_book_status(self)
        print(f"- Status of '{self.name}' updated to 'Completed'.")
class ReadingList:

    def __init__(self):
        self.books = []
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS reading_list(
                name TEXT,
                author TEXT,
                status TEXT
            )
        """)
        print(f"* Reading list created.\n")
        
    def add_book(self, book):
        all_books = self.cursor.execute("SELECT * FROM reading_list WHERE name = ? AND author = ?", (book.name, book.author))
        if not all_books.fetchone():
            self.cursor.execute("INSERT INTO reading_list VALUES (?, ?, ?)", (book.name, book.author, book.status))
            self.conn.commit()
            print(f"- '{book.name}' added to the reading list.")
        else:
            print(f"- ERROR: '{book.name}' cannot be added to the reading list as it already exists.")
    
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