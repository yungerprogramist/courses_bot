import sqlite3



class BaseDB:

    def __init__(self) -> None:
        db = sqlite3.connect('project.db') 
        self.sql = db.cursor()
        self.db = db 


    def create_user_db(self):
        self.sql.execute('''CREATE TABLE "users_table" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "username"  TEXT UNIQUE,
            "chat_id" INTEGER UNIQUE,
            "count_day" INTEGER
        )''')
        self.db.commit()
        self.sql.close()
        
    def create_course_db(self):
        self.sql.execute('''CREATE TABLE "course_table" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "name" TEXT,
            "description" TEXT,
            "value" TEXT,
            "filepath" TEXT
        )''')
        self.db.commit()
        self.sql.close()

# BaseDB().create_course_db()
# BaseDB().create_user_db()


