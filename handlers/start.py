from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_bot(message: Message):
    await message.answer("Привет! Это бот, который позволяет скачивать видео с Youtube. "
                         "Отправь мне ссылку и я тебе пришлю готовое видео")