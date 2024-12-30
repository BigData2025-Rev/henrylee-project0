import pandas as pd
from datetime import date
from user import User, LibraryAdmin, LibraryUser


class Book():
    book_file = '/Users/henrylee/Projects-Revature/Project0_Library/bookCatalog.csv'

    def __init__(self, book_id, book_title, book_author):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.checkout_date = None
        self.checked_out_by = None

    @classmethod
    def get_all_books(cls, user):
        book_df = pd.read_csv(Book.book_file)

        # if user, return only books checked out by this user
        if user.role == "user":
            book_df = book_df.loc[(book_df['Checked Out By'] == user.username)]
        
        print("\n=============================================================")
        print(book_df)
        print("=============================================================\n")
    
    @classmethod
    def get_available_books_for_checkout(cls):
        book_df = pd.read_csv(Book.book_file)

        book_df = book_df.loc[(book_df['Checked Out By'].isna() == True)]
        
        print("\n=============================================================")
        print(book_df)
        print("=============================================================\n")

    #add book to catalog
    def add_book(self):
        #read from csv file
        book_df = pd.read_csv(Book.book_file)

        #check if book exists
        book_record = book_df.loc[(book_df['Book ID'] == self.book_id)]
        if len(book_record) == 0:
            #if book does not exist, then add
            new_row = {'Book ID': self.book_id, 'Title': self.book_title, 'Author': self.book_author, 'Checkout Date': self.checkout_date, 'Checked Out By': self.checked_out_by}
            book_df = pd.concat([book_df, pd.DataFrame([new_row])], ignore_index=True)

            #write to csv
            book_df.to_csv(Book.book_file, index=False)

            print("\nBook " + self.book_title + " is added.")
        else:
            print("\nBook " + self.book_title + " is already in the library.")
    
    #remove book by book ID
    @classmethod
    def remove_book(cls, book_id):
        #read from csv file
        book_df = pd.read_csv(Book.book_file)

        #check if book exists and not checked out 
        book_record = book_df.loc[(book_df['Book ID'] == book_id) & (book_df['Checked Out By'].isna() == True)]
        if len(book_record) != 0:
            #if book exists, then remove
            book_df = book_df.loc[(book_df['Book ID'] != book_id)]

            #write to csv file
            book_df.to_csv(Book.book_file, index=False)
            print("\nBook " + book_id + " has been removed.") 
        else:
            print("\nBook " + book_id + " does not exist.")


    @classmethod
    def checkout_book(self, book_id, username):
        #read from csv file
        book_df = pd.read_csv(Book.book_file)

        today = date.today()

        book_df.loc[book_df['Book ID'] == book_id, 'Checked Out By'] = username
        book_df.loc[book_df['Book ID'] == book_id, 'Checkout Date'] = today
        book_df.to_csv(Book.book_file, index = False)
        print("\nBook " + book_id + " has been checked out.")

    @classmethod
    def return_book(self, book_id):
       #read from csv file
        book_df = pd.read_csv(Book.book_file)

        book_df.loc[book_df['Book ID'] == book_id, 'Checked Out By'] = None
        book_df.loc[book_df['Book ID'] == book_id, 'Checkout Date'] = None
        book_df.to_csv(Book.book_file, index = False)
        print("\nBook " + book_id + " has been returned.")


####### Test Cases #######

'''u1 = LibraryUser("Helen", "Lee", "helen")
Book.get_all_books(u1)'''

'''u2 = LibraryAdmin("Amy", "Lee", "alee")
Book.get_all_books(u2)'''

#add a book
'''book1 = Book("B2002", "Python in Action", "ABC Author")
book1.add_book()
Book.get_all_books(u2)'''

#remove a book
'''Book.remove_book("B2002")
Book.get_all_books(u2)'''

#checkout book
#Book.checkout_book("B2001", "henry")

#return book
#Book.return_book("B2001")
