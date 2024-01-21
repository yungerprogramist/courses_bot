from aiogram import Router
from bot import ADMIN_PASSWORD

from aiogram import  F, Bot
from aiogram.types import Message, CallbackQuery 
from aiogram.fsm.context import FSMContext

from utils import keyboard as kb
from DataBase import db
from utils.FSMclasses import  DataCorse, MilingMes




router = Router()


@router.message(F.text == '/admin')
async def admin(message: Message):
    await message.answer('Для продолжения, введите пароль')


@router.message(F.text == ADMIN_PASSWORD)
async def admin_panel(message: Message):
    name = message.from_user.first_name
    await message.answer(f'Добро пожаловать администратор {name}', reply_markup= kb.choise_do_admin)

@router.callback_query(F.data == 'admin_panel')
async def admin_panel(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(f'Добро пожаловать администратор {name}', reply_markup= kb.choise_do_admin)


"""=======================добавить курс==================================="""

@router.callback_query(F.data == 'add_course')
async def add_course(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите название курса не более 16 символов (Можете дать название Курс №1)') 
    await state.set_state(DataCorse.name)

@router.message(DataCorse.name)
async def name_course(message: Message, state: FSMContext):

    if len(message.text) < 16:
        await state.update_data(name=message.text)
        await message.answer('Введите Описание курса, оно должно быть не более 4096символов')
        await state.set_state(DataCorse.description)
    else: 
        await message.answer('Введите название курса, оно должно быть не более 16 символов')
        await state.set_state(DataCorse.name)

@router.message(DataCorse.description)
async def description_course(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Пришлите основной текст курса и прикрепите к нему файл')
    await state.set_state(DataCorse.value)

@router.message(DataCorse.value)
async def value_course(message: Message, state: FSMContext, bot: Bot):

    text_value = message.caption
    await state.update_data(value=text_value)

    file_id = message.document.file_id
    file_path = f'content/{file_id}.pdf'
    await bot.download(file=file_id, destination=file_path)
    
    data = await state.get_data()
    data['filepath'] = file_path
    db.add_course_db(data)

    await state.clear()
    await message.answer('Курс успешно загружен', reply_markup=kb.admin_menu)



"""=======================удалить курс==================================="""
@router.callback_query(F.data == 'delete_course')
async def delete_course(callback: CallbackQuery):
    await callback.message.answer('Выберите курс, который хотите удалить. Аккуратнее, не промахнитесь!!!', reply_markup=kb.courselist_delete_markup())

    
@router.callback_query(lambda call: 'deletecourse:' in call.data )
async def deletecourse(callback: CallbackQuery):
    name = callback.data.split(':')[1]
    await callback.message.answer(f'Вы уверенны, что хотите удалить курс {name} ?', reply_markup= kb.accept_delete_course(name))

@router.callback_query(lambda call: 'deleteaccept:' in call.data )
async def deletecourse_accept(callback: CallbackQuery):
    name = callback.data.split(':')[1]
    if db.delete_course(name):
        await callback.message.answer(f'Курс {name} успешно удален', reply_markup=kb.admin_menu)
    else:
        await callback.message.answer(f'Что то пошло не так во время удаленния курса {name}', reply_markup=kb.admin_menu)



"""=======================рассылка сообщений==================================="""


@router.callback_query(F.data == 'miling_mes')
async def miling_mesage(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Отправьте сообщения и фотографию для рассылки')
    await state.set_state(MilingMes.mil_message)


@router.message(MilingMes.mil_message)
async def send_mil_message(message: Message, state: FSMContext, bot: Bot):
    await state.clear()

    try:

        for chat_id in db.get_all_user_ids():
            try: 

                await bot.copy_message(chat_id=chat_id, from_chat_id=message.from_user.id, message_id=message.message_id, parse_mode='Markdown')

            except:
                await message.answer(text=f'Что то пошло не так при попытке отправить сообщение пользователю с id - {chat_id}!')
    except:
        await message.answer(text='Что то пошло не так при попытке сделать рассылку, убедитесь, что вы отправили сообщение вместе с фотографией !')

    await message.answer(text='Рассылка закончена', reply_markup=kb.admin_menu)