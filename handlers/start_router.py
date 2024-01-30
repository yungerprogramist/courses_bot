from aiogram import Router

from aiogram import Bot,  F
from aiogram.types import Message


from DataBase.google_sheet import GoogleSheet as gs
from DataBase.users_db import UsersDB
from utils import keyboard as kb
import messages as mes
from aiogram.types.input_file import FSInputFile


router = Router()

@router.message(F.text == '/start')
async def start(message: Message, bot:Bot):
    if message.from_user.username is not None:
        username = message.from_user.username
        chat_id = message.from_user.id

        if not UsersDB().check_reg(username):
            gs().start_gs() 
            UsersDB().start_db(username, chat_id)

            photo = FSInputFile("photos_for_message/start_photo.jpg")
            await bot.send_photo(chat_id=chat_id, photo=photo, caption=mes.start_mes, reply_markup=kb.start_but, parse_mode='Markdown')
            await bot.send_message(chat_id=-4086068688, text=f'Пользователь @{username}, нажал кнопку старт')

        else:

            photo = FSInputFile("photos_for_message/start_photo.jpg")
            await bot.send_photo(chat_id=chat_id, photo=photo, caption=mes.start_mes, reply_markup=kb.start_but, parse_mode='Markdown')

    

    else: 
        await message.answer('Для использования этого бота, установите username')