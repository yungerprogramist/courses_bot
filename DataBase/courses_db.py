from DataBase.Baseclass import BaseDB
import sqlite3
import os


class CoursesDB(BaseDB):
    __name_table = 'course_table'



    def add_course_db(self, data: dict):
        """Добавляет курс в бд data = {name , description, value, filepath}"""
        db = None
        try: 
            name = data['name']
            description = data['description']
            value = data['value']
            filepath = data['filepath']

            self.sql.execute(f'INSERT INTO {self.__name_table} (name, description, value, filepath) VALUES("{name}", "{description}", "{value}", "{filepath}")')
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()

    
    def get_names_course(self) :
        """Возвращает лист названий курсов"""
        db = None
        try: 
            data = self.sql.execute(f'SELECT name FROM {self.__name_table}').fetchall()
            answer = []
            for i in data:
                answer.append(i[0])

            return answer
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def get_description_corse(self, name):
        """Возвращает описание курса"""
        db = None
        try: 
            return self.sql.execute(f'SELECT description FROM {self.__name_table} WHERE name="{name}"').fetchone()[0]
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()
    

    # можно обьеденить эту и верхнюю функцию, но я не знаю как это сделать без потери времени на ненужные запросы 
    def get_course(self, name)-> tuple:
        """Возвращает инфу из бд про курс ->список (value, filepath)"""
        db = None
        try: 
            return self.sql.execute(f'SELECT value, filepath FROM {self.__name_table} WHERE name="{name}"').fetchall()[0]
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def delete_course(self, name)-> bool:
        db = None
        try: 

            self.sql.execute(f'DELETE FROM {self.__name_table} WHERE name="{name}"')

            return True
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
            return False
        finally: 
            self.db.commit()
            if db: self.db.close()