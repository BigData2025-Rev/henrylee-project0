'''
Library app
'''

import sys

from book import Book
from user import User, LibraryUser, LibraryAdmin
  
def library_menu(user): 
    option = True
    print("\nWelcome to Henry's Library " + user.get_full_name() + "\n")

    while option: 
        #list all books
        Book.get_all_books(user)

        print("1. Borrow Books")
        print("2. Return Books")
        print("3. Exit\n")

        menu_selection = input("Enter your option: \n")
        if menu_selection == "1":
            while True:
                Book.get_available_books_for_checkout()
                book_id = input("Enter a book ID to checkout the book, or 0 to return to the main menu: ")
                if book_id == "0":
                    break
                else: 
                    #checkout book
                    Book.checkout_book(book_id, user.username)

                    #list all books
                    Book.get_all_books(user)

        elif menu_selection == "2":
            while True:
                Book.get_all_books(user)
                book_id = input("Enter a book ID to return, or 0 to return to the main menu: ")
                if book_id == "0":
                    break
                else:
                    #checkout book
                    Book.return_book(book_id)

                    #list all books
                    Book.get_all_books(user)

        elif menu_selection == "3":
            print("\n Thank you for visiting. See you next time!\n")
            return False
        else:
            print("Invalid choice\n")
            return False

def library_menu_admin(user):
    print("\nWelcome to the Library's Admin Page " + user.get_full_name() + "\n")

    option = True
    while option: 
        print("1. Update Book Catalog")
        print("2. Manage Users")
        print("3. Exit\n")

        menu_selection = input("Enter your option: ")
        if menu_selection == "1":
            print("update book ")
            #list all books
            Book.get_all_books(user)

            while True:
                print("Update Book Catalog: ")
                print("1. Add a new book")
                print("2. Delete a book")
                print("0. Back to main menu\n")
                sub_menu_selection = input("Enter your option: ")

                if sub_menu_selection == "1":
                    #add new book
                    print("Enter a book's information to add")
                    book_id = input("Book ID: ")
                    title = input("Title: ")
                    author = input("Author: ")

                    new_book = Book(book_id, title, author)
                    new_book.add_book()

                    #list all books
                    Book.get_all_books(user)
                elif sub_menu_selection == "2":
                    #remove a book
                    print("Enter a book's ID to delete")
                    book_id = input("Book ID: ")
                    Book.remove_book(book_id)

                    #list all books
                    Book.get_all_books(user)
                elif sub_menu_selection == "0":
                    #go back to main menu
                    break
                else:
                    print("Invalid choice\n")

        elif menu_selection == "2":
            print("manage users")
            #list all users
            user.get_all_users()

            while True:
                print("Manage Users: ")
                print("1. Add a new user")
                print("2. Remove a user")
                print("0. Back to main menu\n")
                sub_menu_selection = input("Enter your option: ")

                if sub_menu_selection == "1":
                    #add user
                    print("Please enter user information: ")
                    username = input("User Name: ")
                    password = input("Password: ")
                    fname = input("First Name: ")
                    lname = input("Last Name: ")
                    role = input("Role (user or admin): ")

                    user.add_user(fname, lname, username, password, role)
                    user.get_all_users()
                elif sub_menu_selection == "2":
                    #remove user
                    print("Please enter a user to remove")
                    username = input("User Name: ")
                    user.remove_user(username)

                    #list all current users
                    user.get_all_users()
                elif sub_menu_selection == "0":
                    break
                else: 
                    print("Invalid Choice\n")
        elif menu_selection == "3":
            print("\nLogged Out. See you next time!\n")
            return False
        else:
            print("Invalid choice\n")


def login():
    print("\nWelome to Henry's Library!")
    print("\nPlease enter your user name and password to login ")
    user_name = input("User Name: ")
    password = input("Password: ")

    user_record = User.login(user_name, password) #look for record in table in users.csv
    if len(user_record) == 0:
        print("User not found.")
        sys.exit()
    else:
        #User found
        user_role = user_record["Role"].values[0]
        fname = user_record["First Name"].values[0]
        lname = user_record["Last Name"].values[0]
        username = user_record["User Name"].values[0]
        if user_role == 'user':
            print("Library User")
            return LibraryUser(fname, lname, username)
        else:
            print("admin user")
            return LibraryAdmin(fname, lname, username)
        

def main():
    login_user = login()

    if isinstance(login_user, LibraryUser):
        library_menu(login_user)
    else:
        library_menu_admin(login_user)
    
    #library_input = input("Enter your option: ")
    #library_menu(library_input)
    

if __name__ =="__main__":
    main()


    
