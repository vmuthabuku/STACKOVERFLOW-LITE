import psycopg2
import os

def reset_migration():
    from application.app import db

    conn = db.conn
    cur = db.cursor

    cur.execute("""DELETE FROM answers;""")

    cur.execute("""DELETE FROM questions;""")

    cur.execute("""DELETE FROM user;""")

    conn.commit()

def migrate():
    from application.app import db

    conn = db.conn
    cur = db.cursor

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY, 
        name varchar, 
        email varchar UNIQUE, 
        password varchar
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS questions(
        id serial PRIMARY KEY, 
        question varchar,
        user_id INT, 
        FOREIGN KEY (user_id) REFERENCES users(id)
    );""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS answers(
        id serial PRIMARY KEY, 
        answer varchar,
        question_id INT,
        FOREIGN KEY (question_id) REFERENCES questions(id)
    );""")
    
    conn.commit()