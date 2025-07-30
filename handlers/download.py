import asyncio
import os

from aiogram import Router
from aiogram.types import Message
from aiogram.types import FSInputFile

from services import get_youtube_object, get_highest_stream, check_valid_video_size, download_video, delete_video

router = Router()

@router.message()
async def send_video(message: Message):
    url = message.text
    yt = get_youtube_object(url)
    stream = get_highest_stream(yt)
    if not check_valid_video_size(stream):
        await message.answer("Извините, файл слишком большой, телеграмм мне не позволяет отправить файлы такого размера")
        return
    file_path = await download_video(stream)
    await message.answer_video(video=FSInputFile(file_path))
    await delete_video(file_path)