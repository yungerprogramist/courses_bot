import sqlite3

def change_user_db():
    db=sqlite3.connect('project.db')
    sql=db.cursor()
    sql.execute('''ALTER TABLE users_table ADD count_day INTEGER''')
    sql.execute('''UPDATE users_table SET count_day = 0''')
    db.commit()
    sql.close()


change_user_db()
