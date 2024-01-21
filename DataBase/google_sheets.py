import gspread
from datetime import datetime
import pytz   



"""
https://docs.google.com/spreadsheets/d/1Q5njawnjf7CP3nlCsiz3kbwrjdXUwI8M8lhV-SWm2jg/edit#gid=0
столбцы: 1.дата  2.Нажатых старт  3.Посмотрел курсы
"""

def google_sheets():
    """подключается к google sheets"""
    gc = gspread.service_account(filename='parsing-auto-posting-59567be80d81.json')
    worksheet  = gc.open("информация о пользователях").sheet1
    return worksheet


def next_available_row(worksheet) -> int:
    """Определяет последнюю пустую строку в таблице(используется для записи в последнюю строку)"""
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def start_gs():
    """Добавляет +1 к столбцу 'Нажатых старт'
    Так же проверяет дату, если не сходится, то создается новая строка в таблице"""
    try:
        worksheet = google_sheets()
        moscow_time = str(datetime.now(pytz.timezone('Europe/Moscow'))).split(' ')[0] 
        last_date = list(filter(None, worksheet.col_values(1)))[-1] #забираем последнюю дату из таблицы
        last_row = int(next_available_row(worksheet))

        if last_date != moscow_time:
            worksheet.update_cell(row=last_row, col=1, value=moscow_time)
            worksheet.update_cell(row=last_row, col=2, value='1') 
            # worksheet.update_acell("A{}".format(last_row), moscow_time)

        else: 
            last_date = list(filter(None, worksheet.col_values(2)))[-1] 
            if last_date != 'NoneType':
                start_value = int(worksheet.cell(row=last_row-1, col=2).value) #берем последнее значение столбца синформацией о нажатой кнопкой старт
                worksheet.update_cell(row=last_row-1, col=2, value=str(start_value+1)) #добавляем к значению + 1
            else:
                worksheet.update_cell(row=last_row, col=2, value='1') 

    except Exception as ex:
        print(f'Упс, что то пошло не так с google_sheets - {ex}')



    
def watched_course():
    """Добавляет +1 к столбцу 'Посмотрел курсы'
    Так же проверяет дату, если не сходится, то создается новая строка в таблице"""
    worksheet = google_sheets()
    # try:
    worksheet = google_sheets()
    moscow_time = str(datetime.now(pytz.timezone('Europe/Moscow'))).split(' ')[0] 
    last_date = list(filter(None, worksheet.col_values(1)))[-1] #забираем последнюю дату из таблицы
    last_row = int(next_available_row(worksheet))

    if last_date != moscow_time:
        worksheet.update_cell(row=last_row, col=1, value=moscow_time)
        worksheet.update_cell(row=last_row, col=3, value='1') 
        # worksheet.update_acell("A{}".format(last_row), moscow_time)
    else: 
        start_value = worksheet.cell(row=last_row-1, col=3).value#берем последнее значение столбца синформацией о нажатой кнопкой старт

        if start_value:
            worksheet.update_cell(row=last_row-1, col=3, value=str(int(start_value)+1)) #добавляем к значению + 1
        else:
            worksheet.update_cell(row=last_row-1, col=3, value='1') 
    return True
    # except Exception as ex:
    #     print(f'Упс, что то пошло не так с google_sheets - {ex}')
    #     return False




    
