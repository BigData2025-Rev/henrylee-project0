import pandas as pd

class User:
    firstname = ''
    lastname = ''
    username = ''
    password = ''
    
    user_file = '/Users/henrylee/Projects-Revature/Project0_Library/user.csv'

    def __init__(self, fname, lname, uname) -> None:
        self.firstname = fname
        self.lastname = lname
        self.username = uname
    
    def print_full_name(self):
        print(f"{self.lastname}, {self.firstname}\n")
    
    def get_full_name(self):
        return self.firstname + " " + self.lastname
    
    @classmethod
    def login(cls, user_name, password):
        user_df = pd.read_csv(cls.user_file)
        #print(user_df.head())

        loc = user_df.loc[(user_df['User Name'] == user_name) & (user_df['Password'] == password)]
        #print(loc)

        return loc

class LibraryUser(User):
    role = "user"

    def __init__(self, fname, lname, uname) -> None:
        super().__init__(fname, lname, uname)


class LibraryAdmin(User):
    role = "admin"

    def __init__(self, fname, lname, uname) -> None:
        super().__init__(fname, lname, uname)

    # get all users from csv file
    def get_all_users(self):
        user_df = pd.read_csv(User.user_file)
        print("\n=================================================================")
        print(user_df)
        print("=================================================================\n")
    
    # add new user
    def add_user(self, fname, lname, uname, password, role):
        #read from csv file
        user_df = pd.read_csv(User.user_file)

        #check if user exists
        user_record = user_df.loc[(user_df['User Name'] == uname)]
        if len(user_record) == 0:
            # if user doesn't exist, then add
            new_row = {'User Name': uname, 'Password': password, 'First Name': fname, 'Last Name': lname, 'Role': role}
            user_df = pd.concat([user_df, pd.DataFrame([new_row])], ignore_index=True)

            # write to csv
            user_df.to_csv(User.user_file, index=False)

            print("\n User " + fname + " " + lname + " is added.")
        else:
            print("\n User " + fname + " " + lname + " has already existed.")

    # remove user
    def remove_user(self, uname):
        #read from csv
        user_df = pd.read_csv(User.user_file)

        #check if user exists
        user_record = user_df.loc[(user_df['User Name'] == uname)]
        if len(user_record) != 0:
            # if user exists, then remove
            user_df = user_df.loc[(user_df['User Name'] != uname)]

            # write to csv
            user_df.to_csv(User.user_file, index=False)
            print("\nUser " + uname + " has been removed.")
        else:
            print("User " + uname + " does not exist.")


####### Test Cases #########

###test print user name
'''user1 = User('amy','lee','alee')
user1.print_full_name()
print(user1.get_full_name())'''

###test login
'''User.login("henry", "admin123")
User.login("abc","user123")'''

#test adding/removing user
#user1 = LibraryAdmin("amy", "lee", "alee") 

#get all users
#user1.get_all_users()

#add new user
#user1.add_user("Adam", "Johnson", "adam", "test123", "user")
#user1.get_all_users()

#test remove user by user name
#user1.remove_user("adam")

#user1.get_all_users()

