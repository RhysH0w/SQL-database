import sqlite3 as lite
import time

with lite.connect("Quiz.db") as db:
    cursor = db.cursor()


def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # with lite.connect("QuizScores.db") as db:
        #     cursor = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
        cursor.execute(find_user, [(username), (password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome " + i[2])

                return ("exit")

        else:
            print("username and password not recognized")
            again = input("Do you want to try again (Y/N)")
            if again.lower == "n":
                print("Goodbye")
                time.sleep(1)
                return ("exit")

def newUser():
    print("Add a new user")
    time.sleep(1)

    found = 0
    while found == 0:
        username = input("Enter a username: ")
        with lite.connect("Quiz.db") as db:
            cursor  = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ?')
        cursor.execute(find_user, [ (username)])

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

    insertData = '''INSERT INTO user(username, firstname, surname, password)
    VALUES(?, ?, ?, ?)'''
    cursor.execute(insertData, [(username), (firstName), (surname), (password)])
    db.commit()

def menu():
    while True:
        print("welcome to the database")
        menu = ('''
        1 - Create New User
        2 - Login
        3 - Exit
        - ''')

        userChoise = input(menu)

        if userChoise == "1":
            newUser()

        elif userChoise == "2":

          enter = login()
          if enter == "exit":
            break

        elif userChoise == "3":
            print("Goodbye")
            time.sleep(1)
            break

        else:
            print("input not recognized")


cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname  VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

db.commit()

cursor.execute("SELECT * FROM user")

print(cursor.fetchall())

menu()
