import sqlite3 as lite
import time


class Quiz:
    def __init__(self):
        self.conn = lite.connect('Quiz.db')
        self.menu()

    def menu(self):
        cursor = self.conn.cursor

        while True:
            print("Welcome to the quiz")

            menu = ('''
            1 - Add to the database
            - ''')

            userChoise = input(menu)

            if userChoise == '1':
                enter = self.newQuestionTopic()

    def newQuestionTopic(self):
        with lite.connect("Quiz.db") as db:
            cursor = db.cursor()
        print("Add new question")
        time.sleep(1)

        cursor.execute('SELECT topicName FROM topics')
        topics = cursor.fetchall()

        while True:

            print("What topic is your question in?")

            for i in topics:
                print(i[0])

            hold = input("New topic (1)\n"
                         "- ")
            cursor.execute('SELECT topicName FROM topics WHERE topicName = ?', [hold])
            results = cursor.fetchone()
            if hold == '1':
                newTopic = input("What is the new topic name?")

                self.topic = newTopic

                insertData = '''INSERT INTO topics(topicName)
                    VALUES(?)'''
                cursor.execute(insertData, [(newTopic)])
                db.commit()

                temp = Quiz.NewQuestion(())

            elif results and results[0] == hold:
                temp = Quiz.NewQuestion()

            else:
                print("That is not a valid topic")

    def NewQuestion(self):
        with lite.connect("Quiz.db") as db:
            cursor = db.cursor()

        print("actually add a new question")

        time.sleep(1)


quiz = Quiz()
