import sqlite3 as lite
import time


class Users:
    def __init__(self):
        self.conn = lite.connect('Quiz.db')
        self.menu()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
        userID INTEGER PRIMARY KEY,
        username VARCHAR(20) NOT NULL,
        firstname VARCHAR(20) NOT NULL,
        surname VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL);
        ''')

        self.conn.commit()

    def newUser(self):
        print("Add a new user")
        time.sleep(1)
        username = ()

        found = 0
        while found == 0:
            username = input("Enter a username: ")
            with lite.connect("Quiz.db") as db:
                cursor = db.cursor()
            find_user = ('SELECT * FROM user WHERE username = ?')
            cursor.execute(find_user, [(username)])

            if cursor.fetchall():
                print("Username Taken")
            else:
                found = 1

        firstName = input("Please enter your first name: ")
        surname = input("Please enter your last name: ")
        password = input("Please enter a password: ")
        password2 = input("Please re-enter your password: ")
        while password != password2:
            print("Passwords did not match")
            password = input("Please enter a password: ")
            password2 = input("Please re-enter your password: ")
        self.username = username
        self.password = password
        self.firstname = firstName
        self.surname = surname

        insertData = '''INSERT INTO user(username, firstname, surname, password)
            VALUES(?, ?, ?, ?)'''
        cursor.execute(insertData, [(username), (firstName), (surname), (password)])
        db.commit()

    @property
    def login(self):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            with lite.connect("Quiz.db") as db:
                cursor = db.cursor()

            find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
            cursor.execute(find_user, [(username), (password)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    print("Welcome " + i[2])

                    return ("exit")

            else:
                print("username or password not recognized")

                again = input("Do you want to try again (Y/N)").lower()
                while again != "n" and again != "y":
                    print("You did not enter a Y or N as your Input")
                    again = input("Do you want to try again (Y/N)").lower()

                if again == 'y':
                    return "more"

                else:
                    return "exit"

                    # if again.lower == "y":
                    #     self.login()
                    # else:
                    #     print("Goodbye")
                    #     time.sleep(1)
                    #     return "exit"



    def displayDatabase(self):
        with lite.connect("Quiz.db") as db:
            cursor = db.cursor()

        cursor.execute('SELECT userID, username, firstname, surname FROM user ORDER BY userID ASC')
        results = cursor.fetchall()

        for i in results:
            print(i)

    def menu(self):

        self.createTable()

        while True:
            print("welcome to the database")
            menu = ('''
            1 - Create New User
            2 - Login
            3 - Display the database
            4 - Exit
            - ''')

            userChoise = input(menu)

            if userChoise == "1":
                self.newUser()

            elif userChoise == "2":

                while True:

                    enter = self.login
                    if enter == "exit":
                        break

            elif userChoise == "3":
                self.displayDatabase()

            elif userChoise == "4":
                print("Goodbye")
                time.sleep(1)
                break

            else:
                print("input not recognized")


user = Users()
