from aiogram import Router

from aiogram import  Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile

from utils import keyboard as kb
from DataBase.courses_db import CoursesDB
from DataBase.google_sheet import GoogleSheet as gs
import messages as mes
from utils.FSMclasses import Qestion



CHANEL_DB = '@courses_b_db'


router = Router()

@router.message(F.text == 'Доступные курсы')
async def courses(message: Message, bot: Bot):
    chanel_id = message.from_user.id
    channel_id_sub = '-1001579575685'
    user_channel_status = await bot.get_chat_member(chat_id=channel_id_sub, user_id=chanel_id)
    
    if not ('left' in str(user_channel_status)):
        photo = FSInputFile("photos_for_message/courses_photo.jpg")
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=mes.show_courses, reply_markup=kb.courselist_show_markup())

    else:
        await message.answer(mes.most_subscribe, reply_markup=kb.most_subscribe)

# Две одинаковые функции, нужно фиксить повторение кода
@router.callback_query(F.data == 'menu')
async def courses_show(callback: CallbackQuery, bot: Bot):
    chamel_id = callback.from_user.id
    channel_id = '-1001579575685'
    user_channel_status = await bot.get_chat_member(chat_id=channel_id, user_id=chamel_id)
    if not ('left' in str(user_channel_status)):
        photo = FSInputFile("photos_for_message/courses_photo.jpg")
        await bot.send_photo(chat_id=callback.from_user.id, photo=photo, caption=mes.show_courses, reply_markup=kb.courselist_show_markup())
    else:
        await callback.message.answer(mes.most_subscribe)



@router.callback_query(lambda call: 'courseforuser:' in call.data )
async def courses_show(callback: CallbackQuery):
    course_name = callback.data.split(':')[1]
    description = CoursesDB().get_description_corse(course_name)
    await callback.message.answer(text = f'{course_name} \n\n{description}', reply_markup=kb.open_course_markup(course_name))

@router.callback_query(lambda call: 'showcourse:' in call.data )
async def show_course(callback: CallbackQuery, bot: Bot):
    msg = await callback.message.answer('Актуализируем курс…✏️')

    course_name = callback.data.split(':')[1]
    data_course = CoursesDB().get_course(course_name)

    value = data_course[0]
    filepath = data_course[1]

    chat_id = callback.from_user.id

    await callback.message.answer(text=value)
    await bot.send_document(chat_id=callback.from_user.id, document=filepath)
    

    await bot.delete_message(chat_id=chat_id, message_id=msg.message_id)

    gs().watched_course()

    
    await bot.send_message(chat_id=-4086068688, text=f'Пользователь @{callback.from_user.username}, забрал курс {course_name}')
    




@router.callback_query(lambda call: 'ask_question:' in call.data )
async def ask_question(callback: CallbackQuery, bot: Bot, state: FSMContext):
    photo = FSInputFile("photos_for_message/question_photo.jpg")
    await bot.send_photo(chat_id=callback.from_user.id,photo=photo, caption=mes.ask_qustion, reply_markup=kb.back_in_menu)
    course = callback.data.split(':')[1]
    await state.update_data(course = course)
    await state.set_state(Qestion.qestion)
    

@router.message(Qestion.qestion)
async def send_question(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    course = data['course']
    await state.clear()
    username = message.from_user.username
    text = f'@aeads7 \nВам пришел вопрос от пользователя @{username} \nКурс - {course} \nВопрос: {message.text}'
    await bot.send_message(chat_id=-4086068688, text=text)

    await message.answer('Ваш вопрос успешно отправлен, ожидайте ответа', reply_markup=kb.back_in_menu)



