import psycopg2
import psycopg2.extras
import os
from application.database import Database

conn = Database.conn
cur = Database.cursor

def insert_user(users):
    cur.execute("INSERT INTO USERS(name, email, password) values(%s,%s,%s)",(
        users.name,
        users.email,
        users.password))
    conn.commit()


def get_user(email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    if user is None:
        return None
    conn.commit()
    return user
    

def post_question(questions):
    cur.execute("INSERT INTO questions (question, user_id) values(%s,now(),%s)",(
        questions.question,
        questions.user_id))
    conn.commit()

def get_questions(user_id):
    cur.execute("SELECT * FROM questions WHERE user_id =%s",(user_id,))
    questions = cur.fetchall()
    rows = []
    for row in questions:
        rows.append(dict(row))
    if rows is None:
        return None
    conn.commit()
    return rows
    

def get_question(id):
    cur.execute("SELECT * FROM question WHERE id = %s", (id,))
    questions = cur.fetchone()
    if questions is None:
        return None
    conn.commit()
    return questions

def edit_question(id, question):
    cur.execute("UPDATE questions SET question = %s = %s WHERE id = %s", (
        question['question'],
        id))
    conn.commit()

def delete_question(id):
    cur.execute("DELETE FROM questions WHERE id = %s", (id,))
    conn.commit()

def answer_question(answers):
    cur.execute("INSERT INTO answers (answer, questionId) values(%s,%s,%s)",(
        answers.answer,
        answers.questionId))
    conn.commit()

def drop_everything(self):
    self.cur.execute("DROP TABLE user;")
    self.cur.execute("DROP TABLE questions;")
    self.cur.execute("DROP TABLE answers;")
    self.conn.commit()