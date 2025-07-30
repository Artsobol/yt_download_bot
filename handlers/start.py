from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.start_kb import start_kb

router = Router()

@router.message(CommandStart())
async def start_bot(message: Message, state: FSMContext):
    await state.clear()

    await message.answer("Привет! Это бот, который позволяет скачивать видео с Youtube. "
                         "Выбери как ты хочешь скачать видео", reply_markup=start_kb)