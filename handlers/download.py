import asyncio
import os
from pathlib import Path

from aiogram import Router
from aiogram.types import Message
from aiogram.types import FSInputFile

from services import get_video

router = Router()

@router.message()
async def send_video(message: Message):
    file_path = get_video(message.text)
    await message.answer_video(video=FSInputFile(path=file_path))
    await delete_video(file_path)

async def delete_video(path: Path):
    await asyncio.to_thread(os.remove, path)