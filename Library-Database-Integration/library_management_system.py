
# Global variables and imports
import sys
import mysql.connector
from mysql.connector import Error

db_name = "fitness_db"
user = "root"
password = "843RnR$$"
host = "127.0.0.1"
port = 3306

def run_mysql_script(sql_path):
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        if conn.is_connected():
            cursor = conn.cursor()
            with open(sql_path, 'r') as file:
                sql_script = file.read()
            sql_commands = sql_script.split(';')
            for command in sql_commands:
                if command.strip(): 
                    cursor.execute(command)
            conn.commit()
            print("Executed successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
sql_path = 'library_management.sql'
run_mysql_script(sql_path)


# function that connects to mysql and creates cursor to execute adding a row to a passed in table with any number of columns
def add_row(db_name, user, password, host, port, table, columns, values):
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        #takes a list of columns and uses the len funcion to determine the number of cvalues to insert into 
        #the functions, variable values contain all of the values to put in 
        if conn.is_connected():
            cursor = conn.cursor()
            # identifies the number of values in the provided data and sets the m to %s 
            placeholders = ", ".join(["%s"] * len(values))
            sql_insert = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql_insert, values)
            conn.commit()
            print(f"Row added successfully to {table}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

#function connects to mysql and creates a cursor to execute searching for a given term within all of the rows of a provided table 
def search_for_item(db_name, user, password, host, port, table, search_item):
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )

        if conn.is_connected():
            cursor = conn.cursor()
            #iterates through eahc column of the given table to search for the provided term 
            search_conditions = " OR ".join([f"{col} = %s" for col in search_item.keys()])
            sql_search = f"SELECT * FROM {table} WHERE {search_conditions}"
            cursor.execute(sql_search, list(search_item.values()))
            #sets variable db_results equal to the row that is selsected based on the search criteria 
            db_results = cursor.fetchall()
            # if a row is selecte prints it off line by line 
            if db_results:
                for row in db_results:
                    print(row)
            else:
                print("No results found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

#function connects to mysql and creates a cursor to executes viewing all of the rows for each column in the table 
def view_all_items(db_name, user, password, host, port, table):
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
# function to view all of the items from a provided table line by line 
        if conn.is_connected():
            cursor = conn.cursor()
            sql_search = f"SELECT * FROM {table}"
            cursor.execute(sql_search)
            db_results = cursor.fetchall()
            if db_results:
                for row in db_results:
                    print(row)
            else:
                print("No results found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# function to change a specific value based on the provided value within a column and a passed in value to change it to
# will be utilized to chenge the status of the book, returned or out 
def change_value(db_name, user, password, host, port, table, id_column, id_change, change_column, new_value):
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )

        if conn.is_connected():
            cursor = conn.cursor()
            sql_change = f"UPDATE {table} SET {change_column} = %s WHERE {id_column} = %s"
            cursor.execute(sql_change, (new_value, id_change))
            conn.commit()
            print("Item changed")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# book class, runs functions and menu for book operations  
class Book:
    def __init__(self):
        pass

    def add_book(self):
        table = 'books'
        columns = 'title, isbn'
        title_value = input("Book name: ")
        isbn_value = input("Book isbn: ")
        add_row(db_name, user, password, host, port, table, columns, (title_value, isbn_value))

    def borrow_book(self):
        table = 'books'
        id_column = 'title'
        id_change = input('Title of book to checkout: ')
        change_column = 'availability'
        new_value = 0
        try:
            change_value(db_name, user, password, host, port, table, id_column, id_change, change_column, new_value)
            print("Book marked as 'Borrowed'")
        except Exception as e:
            print(f"An error occurred: {e}")

    def return_book(self):
        table = 'books'
        id_column = 'title'
        id_change = input('Title of book to return: ')
        change_column = 'availability'
        new_value = 1
        try: 
            change_value(db_name, user, password, host, port, table, id_column, id_change, change_column, new_value)
            print("Book marked as 'Returned'")
        except Exception as e:
            print(f"An error occurred: {e}")

    

    def search_book(self):
        search_genre = input("Type title or isbn of book: ")
        table = 'books'
        search_item = {"title": search_genre, "isbn": search_genre}
        search_for_item(db_name, user, password, host, port, table, search_item)

    def book_menu(self):
        while True:
            book_menu_selection = input("-----------------------------------\nBook Operations:\n 1. Add a new book\n 2. Borrow a Book\n 3. Return a Book\n 4. Search for a Book\n 5. Quit\n------------------------------------\n")
            if book_menu_selection == "1":
                self.add_book()
            elif book_menu_selection == "2":
                self.borrow_book()
            elif book_menu_selection == "3":
                self.return_book()
            elif book_menu_selection == "4":
                self.search_book()
            elif book_menu_selection == "5":
                break
            else:
                print("Invalid selection. Please try again.")

# user class, runs functions and menu for user operations  
class User:
    def __init__(self):
        pass

    def add_user(self):
        enter_name = input("Name: ")
        enter_user_id = input("User Id: ")
        table = 'users'
        columns = 'name, library_id'
        add_row(db_name, user, password, host, port, table, columns, (enter_name, enter_user_id))

    def view_user(self):
        search_user = input("Type user name or id: ")
        table = 'users'
        search_item = {"name": search_user, "library_id": search_user}
        search_for_item(db_name, user, password, host, port, table, search_item)

    def display_user(self):
        table = 'users'
        view_all_items(db_name, user, password, host, port, table)

    def user_menu(self):
        while True:
            user_menu_selection = input("-----------------------------------\nUser Operations:\n 1. Add a new user\n 2. View user details\n 3. Display all users\n 4. Quit\n------------------------------------\n")
            if user_menu_selection == "1":
                self.add_user()
            elif user_menu_selection == "2":
                self.view_user()
            elif user_menu_selection == "3":
                self.display_user()
            elif user_menu_selection == "4":
                break
            else:
                print("Invalid selection. Please try again.")

# author class, runs functions and menu for author operations  
class Author:
    def __init__(self):
        pass

    def add_author(self):
        table = 'authors'
        columns = 'name, biography'
        name = input("Author name: ")
        biography = input("Author biography: ")
        add_row(db_name, user, password, host, port, table, columns, (name, biography))

    def view_author(self):
        search_author = input("Type author name to view books: ")
        table = 'authors'
        search_item = {"name": search_author}
        search_for_item(db_name, user, password, host, port, table, search_item)

    def display_author(self):
        table = 'authors'
        view_all_items(db_name, user, password, host, port, table)

    def author_menu(self):
        while True:
            author_menu_selection = input("-----------------------------------\nAuthor Operations:\n 1. Add a new author\n 2. View author books\n 3. Display all authors\n 4. Quit\n------------------------------------\n")
            if author_menu_selection == "1":
                self.add_author()
            elif author_menu_selection == "2":
                self.view_author()
            elif author_menu_selection == "3":
                self.display_author()
            elif author_menu_selection == "4":
                break
            else:
                print("Invalid selection. Please try again.")

# genre class, runs functions and menu for genre operations  
class Genre:
    def __init__(self):
        pass

    def add_genre(self):
        table = 'genres'
        columns = 'name, description, category'
        name = input("Genre name: ")
        description = input("Genre description: ")
        category = input("Genre category: ")
        add_row(db_name, user, password, host, port, table, columns, (name, description, category))

    def display_genre(self):
        table = 'genres'
        view_all_items(db_name, user, password, host, port, table)

    def view_genre(self):
        search_genre = input("Type id, name, or category of genre: ")
        table = 'genres'
        search_item = {"id": search_genre, "name": search_genre, "category": search_genre}
        search_for_item(db_name, user, password, host, port, table, search_item)

    def genre_menu(self):
        while True:
            genre_menu_selection = input("-----------------------------------\nGenre Operations:\n 1. Add a new genre\n 2. View genre details\n 3. Display all genres\n 4. Quit\n------------------------------------\n")
            if genre_menu_selection == "1":
                self.add_genre()
            elif genre_menu_selection == "2":
                self.view_genre()
            elif genre_menu_selection == "3":
                self.display_genre()
            elif genre_menu_selection == "4":
                break
            else:
                print("Invalid selection. Please try again.")

# main menu function, program starts at main menu 
class Main:
    def main_menu(self):
        while True:
            main_menu_selection = input("-----------------------------------\n\tWelcome to the Library Management System with Database Integration!\n Main Menu:\n 1. Book Operations\n 2. User Operations\n 3. Author Operations\n 4. Genre Operations\n 5. Quit\n------------------------------------\n")
            if main_menu_selection == "1":
                book_operations = Book()
                book_operations.book_menu()
            elif main_menu_selection == "2":
                user_operations = User()
                user_operations.user_menu()
            elif main_menu_selection == "3":
                author_operations = Author()
                author_operations.author_menu()
            elif main_menu_selection == "4":
                genre_operations = Genre()
                genre_operations.genre_menu()
            elif main_menu_selection == "5":
                sys.exit()
            else:
                print("Invalid selection. Please try again.")


# Call the main menu function
main_menu = Main()
main_menu.main_menu()
