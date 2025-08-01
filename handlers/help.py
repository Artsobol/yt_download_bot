from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from lexicon import LEXICON_RU

router = Router()


@router.message(Command(commands="help"))
async def help(message: Message):
    await message.answer(LEXICON_RU["/help"])
