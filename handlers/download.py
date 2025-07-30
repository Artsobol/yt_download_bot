from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import Message, CallbackQuery

from config.Itag import Itag
from config.states import DownloadVideoStates
from keyboards.resolution_kb import create_inline_keyboard
from services import get_youtube_object, download_video, \
    get_available_itags, check_valid_video_and_audio_size, delete_all, merge_streams, \
    get_video_and_audio_stream

router = Router()

@router.callback_query(F.data == "url")
async def get_url(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("Отправьте, пожалуйста, ссылку на видео")
    await state.set_state(DownloadVideoStates.url)


@router.message(DownloadVideoStates.url)
async def choose_resolution(message: Message, state: FSMContext):
    url = message.text
    yt = get_youtube_object(url)

    await state.update_data(url=yt)
    available_itags = get_available_itags(yt)
    args = [str(itag) for itag in available_itags]
    kb = create_inline_keyboard(2, *args)

    await message.answer("Выберите качество", reply_markup=kb)
    await state.set_state(DownloadVideoStates.resolution)

@router.callback_query(DownloadVideoStates.resolution)
async def download_chosen_resolution(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    selected_itag = next(i for i in Itag if str(i) == cb.data)
    video_stream, audio_stream = get_video_and_audio_stream(data["url"], selected_itag.value)

    if not check_valid_video_and_audio_size(video_stream, audio_stream):
        await cb.message.answer("Извините, файл слишком большой, телеграмм мне не позволяет отправить файлы такого размера")
        return
    video_file_path = await download_video(video_stream)
    audio_file_path = await download_video(audio_stream)
    file_path = await merge_streams(video_file_path, audio_file_path)

    await cb.message.answer_video(video=FSInputFile(file_path))
    await delete_all(video_file_path, audio_file_path, file_path)

    await state.clear()