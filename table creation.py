import sqlite3 as lite

with lite.connect("Quiz.db") as db:
    cursor = db.cursor()

# Topics table

cursor.execute('''
CREATE TABLE IF NOT EXISTS topics(
topicID INTEGER PRIMARY KEY,
topicName VARCHAR(20) NOT NULL);
''')

# Scores table

cursor.execute('''
CREATE TABLE IF NOT EXISTS scores(
scoreID INTEGER PRIMARY KEY,
userID INTEGER NOT NULL,
score INTEGER NOT NULL,
topicID INTEGER NOT NULL,
FOREIGN KEY(userID) REFERENCES user(userID),
FOREIGN KEY(topicID) REFERENCES topics(topicID));
''')

# Questions table

cursor.execute('''
CREATE TABLE IF NOT EXISTS questions(
questionsID INTEGER PRIMARY KEY,
topicID INTEGER NOT NULL,
question VARCHAR(50),
option1 VARCHAR(50),
option2 VARCHAR(50),
option3 VARCHAR(50),
option4 VARCHAR(50),
answer VARCHAR(50),
FOREIGN KEY(topicID) REFERENCES topics(topicID));
''')
