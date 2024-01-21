import sqlite3
import os

db = sqlite3.connect('project.db') 
sql = db.cursor()


def check_reg(username: str):
    """Проверка, нажимал ли пользователь кнопку старт до этого"""
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()
        result = sql.execute(f'SELECT username FROM users_table WHERE username = "{username}"').fetchone()
        if result:
            return True
        return False
        

    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()



def start_db(username: str, chat_id: int):
    """Звполняет информацию о пользователе, который нажал start,  в бд"""
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()
        sql.execute(f'INSERT INTO users_table (username, chat_id, count_day) VALUES ("{username}", "{chat_id}", 0)')

    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()


def add_course_db(data: dict):
    """Добавляет курс в бд data = {name , description, value, filepath}"""
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()
        name = data['name']
        description = data['description']
        value = data['value']
        filepath = data['filepath']

        sql.execute(f'INSERT INTO course_table (name, description, value, filepath) VALUES("{name}", "{description}", "{value}", "{filepath}")')
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()


def get_names_course() :
    """Возвращает лист названий курсов"""
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()

        data = sql.execute(f'SELECT name FROM course_table').fetchall()
        answer = []
        for i in data:
            answer.append(i[0])

        return answer
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()



def get_description_corse(name):
    """Возвращает описание курса"""
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()

        return sql.execute(f'SELECT description FROM course_table WHERE name="{name}"').fetchone()[0]
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()



# можно обьеденить эту и верхнюю функцию, но я не знаю как это сделать без потери времени на ненужные запросы 
def get_course(name)-> tuple:
    """Возвращает инфу из бд про курс ->список (value, filepath)"""
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()

        return sql.execute(f'SELECT value, filepath FROM course_table WHERE name="{name}"').fetchall()[0]
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()



def delete_course(name)-> bool:
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()

        filepath = sql.execute(f'SELECT filepath FROM course_table WHERE name="{name}"').fetchone()[0]
        os.remove(path=filepath)

        sql.execute(f'DELETE FROM course_table WHERE name="{name}"')

        return True
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
        return False
    finally: 
        db.commit()
        if db: db.close()


def get_all_user_ids() ->list:
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()

        data = sql.execute(f'SELECT chat_id FROM users_table').fetchall()

        chat_id_list = []
        for i in data:
            chat_id_list.append(i[0])
        return chat_id_list
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()



def increment_days() -> None:
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()

        sql.execute(f'UPDATE users_table SET count_day = count_day + 1')
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()


def check_miling_time_days(days: int) -> list:
    db = None
    try: 
        db = sqlite3.connect('project.db') 
        sql = db.cursor()

        data = sql.execute(f'SELECT chat_id FROM users_table WHERE count_day = {days}').fetchall()

        chat_id_list = []
        for i in data:
            chat_id_list.append(i[0])
        return chat_id_list
        
    except sqlite3.Error as ex:
        if db: db.rollback() 
        print (f'Упс что то пошло не так с базой данных - {ex}') 
    finally: 
        db.commit()
        if db: db.close()




