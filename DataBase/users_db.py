from DataBase.Baseclass import BaseDB
import sqlite3


class UsersDB(BaseDB):
    __name_table = 'users_table'



    def check_reg(self, username: str):
        """Проверка, нажимал ли пользователь кнопку старт до этого"""
        db = None
        try: 
            result = self.sql.execute(f'SELECT username FROM {self.__name_table} WHERE username = "{username}"').fetchone()
            if result:
                return True
            return False
            

        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def start_db(self, username: str, chat_id: int):
        """Звполняет информацию о пользователе, который нажал start,  в бд"""
        db = None
        try: 
            self.sql.execute(f'INSERT INTO {self.__name_table} (username, chat_id, count_day) VALUES ("{username}", "{chat_id}", 0)')

        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def get_all_user_ids(self) ->list:
        db = None
        try: 
            data = self.sql.execute(f'SELECT chat_id FROM {self.__name_table}').fetchall()

            chat_id_list = []
            for i in data:
                chat_id_list.append(i[0])
            return chat_id_list
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def increment_days(self) -> None:
        db = None
        try: 
            self.sql.execute(f'UPDATE {self.__name_table} SET count_day = count_day + 1')
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def check_miling_time_days(self, days: int) -> list:
        db = None
        try: 
            data = self.sql.execute(f'SELECT chat_id FROM {self.__name_table} WHERE count_day = {days}').fetchall()

            chat_id_list = []
            for i in data:
                chat_id_list.append(i[0])
            return chat_id_list
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def get_count_users(self) ->int:
        """Возвращает количество пользователей в бд"""
        db = None
        try: 
            count_users = self.sql.execute(f'SELECT count(id) FROM {self.__name_table}').fetchone()[0]

            return count_users
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()


    def zero_days(self):
        """Обнуляет количество дней пользователей бота"""
        db = None
        try: 
            self.sql.execute(f'UPDATE {self.__name_table} SET count_day=0')
            
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
        finally: 
            self.db.commit()
            if db: self.db.close()