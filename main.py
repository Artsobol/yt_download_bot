import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers import handlers_router

load_dotenv(find_dotenv())

async def main():
    token = os.getenv("TOKEN")
    bot = Bot(token=token)

    dp = Dispatcher()

    dp.include_routers(handlers_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа была остановлена")
