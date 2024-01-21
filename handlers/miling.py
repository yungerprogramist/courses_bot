from aiogram import Router
import asyncio
import aioschedule as schedule
from aiogram import Bot,  F
from time import sleep
from DataBase.db import increment_days, check_miling_time_days

from aiogram.utils.markdown import link



from dotenv import load_dotenv
import os
load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))


link_text = link('можно тут', 'https://pawetta.com/vihrov')
chanel_link = link('канале', 'https://t.me/trafficisobar')

text_3day = f'Привет! 3 дня назад я отправил тебе курс. Надеюсь, удалось изучить, применить, и получить результат 😊\n\n*Приглашаю тебя* изучить мой канал (если еще нет), там много полезного, я собираю самые интересные посты в мини-курсы и делюсь ими в этом боте.\n\nПочитать обо мне — {link_text}\nЗадать вопрос — @aeads7\n\n*Спасибо, что читаешь и делишься обратной связью*. Это помогает создавать новые продукты ❤️'

text_30days = f'Привет, у нас первая дата!\n\nСегодня месяц, как мы познакомились ☺️\n\nЗа этот месяц — было выпущено куча контента в {chanel_link}, перетестированы кучи гипотез, сделаны выводы. ~~Чаще — неутешительные~~. И пришло время готовить новый контент.\n\n*Хочешь почитать о чем-то конкретном? Хочешь мини-курс по какой-то важной теме?* \n\nОтвечай прямо в этот чатик, оно сразу падает мне в личку 🚀Вечное спасибо и миллион likes — тебе'


async def mailing_messages():

    increment_days()
        
    for user_id in check_miling_time_days(3):
        bot.send_message(chat_id=user_id, text=text_3day, parse_mode='Markdown')



    for user_id in check_miling_time_days(30):
        bot.send_message(chat_id=user_id, text=text_30days, parse_mode='Markdown')


    





