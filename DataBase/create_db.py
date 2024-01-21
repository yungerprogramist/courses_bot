import sqlite3

def create_user_db():
    db=sqlite3.connect('project.db')
    sql=db.cursor()
    sql.execute('''CREATE TABLE "users_table" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "username"  TEXT UNIQUE,
        "chat_id" INTEGER UNIQUE,
        "count_day" INTEGER
    )''')
    db.commit()
    sql.close()
    

def create_course_db():
    db=sqlite3.connect('project.db')
    sql=db.cursor()
    sql.execute('''CREATE TABLE "course_table" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" TEXT,
        "description" TEXT,
        "value" TEXT,
        "filepath" TEXT
    )''')
    db.commit()
    sql.close()


