import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def main():
    token = os.getenv("TOKEN")
    bot = Bot(token=token)

    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

