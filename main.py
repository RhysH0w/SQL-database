import sqlite3

with sqlite3.connect("Quiz.db") as db:
    cursor = db.cursor()


def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

find_user = ('SELECT * FROM users WHERE username = ? AND password = ?')
cursor.execute(find_user, [(username), (password) ] )
results = cursor.fetchall()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname  VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO USER(username, firstname, surname, password)
VALUES("test_User", "Bob", "Smith", "MrBob")
""")
db.commit()


def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
