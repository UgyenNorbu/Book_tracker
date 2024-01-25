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
    """
    A class to represent a reading list.
    """

    def __init__(self):
        """
        Initializes a reading list object.
        """
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """ 
            CREATE TABLE IF NOT EXISTS reading_list(
                name TEXT,
                author TEXT,
                status TEXT,
                availability TEXT
            )
        """)
        print(f"* Reading list created.\n")
        
    def add_book(self, book):
        """
        Adds a book to the reading list.

        This method adds a book to the library's list of books. It checks if the book is already in the library before adding it.

        Args:
            book (Book): A book object which contains the details of the book.
        """
        all_books = self.cursor.execute("SELECT * FROM reading_list WHERE name = ? AND author = ?", (book.name, book.author))
        if not all_books.fetchone():
            self.cursor.execute("INSERT INTO reading_list VALUES (?, ?, ?, ?)", (book.name, book.author, book.status, book.availability))
            self.conn.commit()
            print(f"- '{book.name}' added to the reading list.")
        else:
            print(f"- ERROR: '{book.name}' cannot be added to the reading list as it already exists.")
    
    def _update_book_status(self, book):
        """
        A private method that updates the status of a book in the reading list.

        Args:
            book (Book): A book object which contains the status of the book.
        """
        self.cursor.execute("UPDATE reading_list SET status = ? WHERE name = ? AND author = ?", (book.status, book.name, book.author))
        self.conn.commit()
    
    def display_reading_list(self):
        """
        Displays the reading list.

        This method displays the list of books in the reading list in a table format.
        """
        all_books = self.cursor.execute("SELECT * FROM reading_list")
        table = [[book[0], book[1], book[2], book[3]] for book in all_books]
        print(tabulate(table, headers= ["Book title", "Author", "Reading status", "Availability"]))
        print("\n*** End of reading list. ***")
class User():
    """
    A class to represent a user.
    """
    def __init__(self, name):
        """
        Initializes a user object.

        Args:
            name (str): Name of the user.
        """
        self.name = name
        print(f"- User '{self.name}' is created.")
    
class UserList():
    """
    A class to represent a user list.
    """
    def __init__(self):
        self.conn = sqlite3.connect("users_list.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                Name TEXT
            )
        """)
        print("* User list created.\n")

    def add_user(self, user):
        """
        Adds a user to the user list.

        Args:
            user (User): A user object which contains the name of the user.
        """
        all_users = self.cursor.execute("SELECT * FROM users WHERE Name = ?", (user.name, ))
        if not all_users.fetchone():
            self.cursor.execute("INSERT INTO users VALUES (?)", (user.name,))
            self.conn.commit()
            print(f"- '{user.name}' added to the user list.")
        else:
            print(f"- ERROR: Cannot add '{user.name}' to the user list as the already exists.")