import sqlite3 as lite
import time


class Quiz:
    def __init__(self):
        self.conn = lite.connect('Quiz.db')
        self.answer1 = None
        self.answer2 = None
        self.answer3 = None
        self.answer4 = None
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
                check = self.adminCheck()
                if check == 'login':
                    enter = self.newQuestionTopic()


                elif check == 'fail':
                    break

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

                temp = self.NewQuestion(())
                if temp == 'done':
                    break

            elif results and results[0] == hold:
                self.topic = 'hold'
                temp = self.NewQuestion()
                if temp == 'done':
                    temp = self.addQuestion()
                    break

            else:
                print("That is not a valid topic")

    def NewQuestion(self):
        with lite.connect("Quiz.db") as db:
            cursor = db.cursor()

        print("actually add a new question")

        time.sleep(1)
        while True:
            self.question = input("What is the question?")
            while True:
                hold = input("from 2-4, how many possible answers are there")
                if hold !='2' and hold != '3' and hold !='4':
                    print("That is not a valid value")
                else:
                    self.answer1 = input("What is the first answer")
                    self.answer2 = input("What is the second answer")

                    if hold == '3':
                        self.answer3 = input("What is the third answer?")

                    elif hold == '4':
                        self.answer3 = input("What is the third answer?")
                        self.answer4 = input("What is the fourth answer")

                    self.trueAnswer = input("What is the correct answer?")
                    return 'done'
        return 'done'

    def adminCheck(self):

        if input("Please confirm you are an admin") == 'yup':
            return 'login'
        else:
            print('you are not an admin')
            return 'fail'
    def addQuestion(self):
        with lite.connect("Quiz.db") as db:
            cursor = db.cursor()
        findTopic = ('''
        SELECT topicID
        FROM topics
        WHERE topics.topicID == questions.topicID
        AND topicName = ?''')
        cursor.execute(findTopic, [(self.topic)])
        topicID = cursor.fetchall()

        insertData = '''
        INSERT INTO questions(topicID, question, option1, option2, option3, option4, answer)
        VALUES(?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insertData, [(topicID), (self.question), (self.answer1), (self.answer2), (self.answer3), (self.answer4), (self.trueAnswer)])
        db.commit()


quiz = Quiz()
