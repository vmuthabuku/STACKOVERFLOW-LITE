import os
import psycopg2

def reset_migration():
    from application.app import db

    conn = db.conn
    cur = db.cursor

    cur.execute("""DELETE FROM answers;""")

    cur.execute("""DELETE FROM questions;""")

    cur.execute("""DELETE FROM users;""")

    conn.commit()

def migrate():
    from application.app import db

    conn = db.conn
    cur = db.cursor

    cur.execute("""CREATE TABLE IF NOT EXISTS user(
        userId int, 
        userName varchar, 
        email varchar, 
        password varchar
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS questions(
        questionId  int, 
        questionBody varchar,
        user_id INT, 
        FOREIGN KEY (user_id) REFERENCES user(id)
    );""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS answers(
        Id serial PRIMARY KEY, 
        answerBody varchar,
        question_id INT,
        FOREIGN KEY (question_id) REFERENCES questions(id)
    );""")
    
    conn.commit()