from aiogram import Bot, F
from DataBase.users_db import UsersDB

from aiogram.utils.markdown import link
from aiogram.types.input_file import FSInputFile



from dotenv import load_dotenv
import os
load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))


# link_text = link('можно тут', 'https://pawetta.com/vihrov')
# chanel_link = link('канале', 'https://t.me/trafficisobar')
# text_3day = f'Привет! 3 дня назад я отправил тебе курс. Надеюсь, удалось изучить, применить, и получить результат 😊\n\n*Приглашаю тебя* изучить мой канал (если еще нет), там много полезного, я собираю самые интересные посты в мини-курсы и делюсь ими в этом боте.\n\nПочитать обо мне — {link_text}\nЗадать вопрос — @aeads7\n\n*Спасибо, что читаешь и делишься обратной связью*. Это помогает создавать новые продукты ❤️'
# text_30days = f'Привет, у нас первая дата!\n\nСегодня месяц, как мы познакомились ☺️\n\nЗа этот месяц — было выпущено куча контента в {chanel_link}, перетестированы кучи гипотез, сделаны выводы. ~~Чаще — неутешительные~~. И пришло время готовить новый контент.\n\n*Хочешь почитать о чем-то конкретном? Хочешь мини-курс по какой-то важной теме?* \n\nОтвечай прямо в этот чатик, оно сразу падает мне в личку 🚀Вечное спасибо и миллион likes — тебе'

post1 = link('Как мы собрали 180к солнышек в телеграм-бота', 'https://t.me/trafficisobar/214')
post2 = link('Перечень необычных зверей', 'https://t.me/trafficisobar/163')
post3 = link('Про рекламные посты', 'https://t.me/trafficisobar/174')
post4 = link('Массовый байт на коммуникации через ботов', 'https://t.me/trafficisobar/231')
post5 = link('раз', 'https://t.me/trafficisobar/193')
post6 = link('два', 'https://t.me/trafficisobar/226')
post7 = link('Как я растил этот канал', 'https://t.me/trafficisobar/107')
post8 = link('Микро-воронки на посты', 'https://t.me/trafficisobar/269')
post9 = link('Поднимаем коэф. возвратов', 'https://t.me/trafficisobar/222')
post10 = link('Пдфки', 'https://t.me/trafficisobar/196')
post11 = link('Сравнение стоимости трафика', 'https://t.me/trafficisobar/184')
post12 = link('Как мы сделали 7 млн. SEO-страниц', 'https://t.me/trafficisobar/202')
post13 = link('Как мы написали 10.000 плохих отзывов', 'https://t.me/trafficisobar/168')
post14 = link('Быстрые продажи из CRM', 'https://t.me/trafficisobar/282')
post15 = link('Как быстро найти работу', 'https://t.me/trafficisobar/167')
post16 = link('Контент в гугл-таблицах', 'https://t.me/trafficisobar/170')
post17 = link('15 минут на работу', 'https://t.me/trafficisobar/228')
post18 = link('Как я искал альтушку', 'https://t.me/trafficisobar/172')
post19 = link('Про сложное', 'https://t.me/trafficisobar/139')
post20 = link('Как узнать, как твои дела', 'https://t.me/trafficisobar/276')
result_url = link('результаты', 'https://t.me/trafficisobar/167')


text1 = 'Cпишь?\n\nСамое время знакомиться.\n\nМеня зовут Вихров Никита, я делаю всякое с диджиталом, SEO, и прочими цифровыми игрушками.\n\nА еще пишу всякое в телеграм-канале: @trafficisobar\n\nТак получилось, что сильнейший мой инфо-продукт — это курс «Как найти работу».\nВот тут подробнее о нем: https://t.me/trafficisobar/167\n\nВот и познакомились.\nЗнаешь сколько людей пишет блогерам? Недостаточно.\n\n→ Поэтому буду рад любой обратной связи, ее можно написать прямо в ответ на это сообщение или мне в личку @aeads7.'

text2 = f'Сегодня видел как двое подростков целуется на скамейке. Это мне напомнило мои подростковые года.\n\nКогда я был подростком видел, как другие подростки целуются.\n\nНу ладно. Зато я написал классные посты, которые действительно помогают с маркетингом в крупных компаниях. Держи подборку лучшего.\n\nВ телеграм:\n— {post1};\n— {post2};\n— {post3};\n— {post4};\n— Куда льют коллеги, {post5} и {post6};\n— {post7}; \n— {post8};\n\nВ internet:\n— {post9} на сайте за 3000 russian rubles;\n— {post10};\n— {post11};\n— {post12};\n— {post13};\n— {post14};\n\nОтсебятина:\n— {post15}; 📣\n— {post16};\n— {post17};\n— {post18}\n— {post19};\n— {post20};\n\nСпасибо. Шутки — тебе. Есть шутки, которые некому отправить? Ты знаешь куда можно: @aeads7'

text3 = f'Однажды — один мальчик не сделал ничего → и ничего не произошло.\n\nИ вот так закончилась эта история.\n\nНаша — наоборот, я улучшил работоспособность бесплатного скрипта из курса «Как найти работу».\n\nТеперь — времени тратится меньше, а зовут на работу — чаще. Посмотри мои {result_url}.\n\nХорошей охоты 🫡'


async def mailing_messages():

    UsersDB().increment_days()

    # for user_id in UsersDB().check_miling_time_days(1):
    #     try: 
    #         photo = FSInputFile("photos_for_message/photo_1day.jpg")
    #         await bot.send_photo(chat_id=user_id, photo=photo, caption=text1, parse_mode='Markdown')
    #     except: 
    #         continue

    # for user_id in UsersDB().check_miling_time_days(3):
    #     try: 
    #         photo = FSInputFile("photos_for_message/photo_3day.jpg")
    #         await bot.send_photo(chat_id=user_id, photo=photo)
    #         await bot.send_message(chat_id=user_id, text=text2, parse_mode='Markdown', disable_web_page_preview=True)
    #     except:
    #         continue

    # for user_id in UsersDB().check_miling_time_days(7):
    #     try: 
    #         photo = FSInputFile("photos_for_message/photo_7day.jpg")
    #         await bot.send_photo(chat_id=user_id, photo=photo, caption=text3, parse_mode='Markdown')
    #     except:
    #         continue

    photo = FSInputFile("photos_for_message/photo_3day.jpg")
    await bot.send_photo(chat_id=6297488038, photo=photo)
    await bot.send_message(chat_id=6297488038 ,text=text2, parse_mode='Markdown', disable_web_page_preview=True)

    # photo = FSInputFile("photos_for_message/photo_3day.jpg")
    # await bot.send_photo(chat_id=636749011, photo=photo)
    # await bot.send_message(chat_id=636749011, text=text2, parse_mode='Markdown', disable_web_page_preview=True)
    # await bot.send_message(chat_id=6297488038, text=text2, parse_mode='Markdown', disable_web_page_preview=True)

    


    


        
    # for user_id in UsersDB().check_miling_time_days(3):
    #     bot.send_message(chat_id=user_id, text=text_3day, parse_mode='Markdown')
    # for user_id in UsersDB().check_miling_time_days(30):
    #     bot.send_message(chat_id=user_id, text=text_30days, parse_mode='Markdown')


    





