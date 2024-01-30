from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton , ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from DataBase.courses_db import CoursesDB




"""================================Пользовательские клавиатуры============================"""

start_but = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Доступные курсы')]], resize_keyboard=True)

back_in_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='вернуть в меню', callback_data='menu')]])

most_subscribe = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Подписаться', url='https://t.me/trafficisobar')]])

def courselist_show_markup():
    """Возвращает клавиатуру курсов, которые есть сейчас в базе"""
    builder = InlineKeyboardBuilder()
    for name in CoursesDB().get_names_course():
        builder.button(text= f"{name}", callback_data= f'courseforuser:{name}')
    builder.adjust(1)
    return builder.as_markup()


def open_course_markup(name):
    open_course = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Забрать', callback_data=f'showcourse:{name}')],
    [InlineKeyboardButton(text='Задать вопрос', callback_data=f'ask_question:{name}')],
    [InlineKeyboardButton(text='В меню', callback_data='menu')]
])
    return open_course





"""================================Админ клавиатуры============================"""

admin_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='вернуть в админ панель', callback_data='admin_panel')]])


choise_do_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить курс', callback_data='add_course')],
    [InlineKeyboardButton(text='Удалить курс', callback_data='delete_course')],
    [InlineKeyboardButton(text='Инфо о боте', callback_data='info_courses')],
    [InlineKeyboardButton(text='Рассылка', callback_data='miling_mes')]
])

def courselist_delete_markup():
    builder = InlineKeyboardBuilder()
    for name in CoursesDB().get_names_course():
        builder.button(text= f"{name}", callback_data= f'deletecourse:{name}')
    return builder.as_markup()

def accept_delete_course(name):
    delete_course = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data=f'deleteaccept:{name}')],
    [InlineKeyboardButton(text='Нет', callback_data='menu')]
])
    return delete_course


