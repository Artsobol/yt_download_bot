from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.start_kb import start_kb
from lexicon import LEXICON_RU

router = Router()


@router.message(CommandStart())
async def start_bot(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        LEXICON_RU["/start"],
        reply_markup=start_kb,
    )
