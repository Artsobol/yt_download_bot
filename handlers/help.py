from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command(commands="help"))
async def help(message: Message):
    await message.answer("Я могу отправлять тебе видео в формате .mp4 c Youtube."
                         "Для этого отправь мне ссылку на видео и я тебе пришлю готовое видео")