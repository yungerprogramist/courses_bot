from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import asyncio

from handlers import start_router, admin_router, users_router


import asyncio
import schedule

from handlers.miling import mailing_messages




def run_miling():
    asyncio.create_task(mailing_messages())
    

async def job_schedule():
    schedule.every().day.at("12:00", "Europe/Moscow").do(run_miling)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(): 
    asyncio.create_task(job_schedule())
    



load_dotenv()
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(
            start_router.router,
            admin_router.router,
            users_router.router,
        )
    
    
    dp.startup.register(on_startup)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

