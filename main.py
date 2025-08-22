import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import router
from keyboards import private_commands
from app1.database.models import async_main, check_db_connection
from middlewares import SaveUserMessageMiddleware

load_dotenv()
TOKEN = os.getenv("TOKEN")

#Создаем ф-цию которая ци2
# клически обрацается к dp раз. в к-л промежуток времени,
#сюда же перенесли переменные бота и диспетчера
#здесь де указали диспетчеру, что мы создали роутер в др папке
async def main():
    if await check_db_connection():
        print("✅ Успешно подключились к базе данных")
    else:
        print("❌ Не удалось подключиться к базе данных")
        return

    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.message.middleware(SaveUserMessageMiddleware())
    await bot.set_my_commands([cmd.model_dump() for cmd in private_commands])
    try:
        logging.basicConfig(level=logging.INFO)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

# ф-ция, которя циклически запускает ф-цию main (т.е. старт) каждый раз при работе бота
if __name__ == '__main__':
    asyncio.run(main())
