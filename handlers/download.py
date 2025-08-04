from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import Message, CallbackQuery

from config.Itag import Itag
from config.states import DownloadVideoStates
from keyboards import KeyboardBuilder
from lexicon import LEXICON_RU
from services import (
    get_youtube_object,
    download_video,
    get_available_itags,
    check_valid_video_and_audio_size,
    delete_all,
    merge_streams,
    get_video_and_audio_stream,
    get_thumbnail_url, get_stream_by_itag,
)

router = Router()


@router.callback_query(F.data == "url")
async def get_url(cb: CallbackQuery, state: FSMContext):
    bot_message = await cb.message.edit_text(LEXICON_RU["url"])
    await state.update_data(bot_message=bot_message.message_id)
    await state.set_state(DownloadVideoStates.url)


@router.message(DownloadVideoStates.url)
async def choose_resolution(message: Message, state: FSMContext):
    bot_message = (await state.get_data())["bot_message"]
    await message.bot.delete_message(chat_id=message.chat.id, message_id=bot_message)
    await message.delete()

    url = message.text
    yt = get_youtube_object(url)

    await state.update_data(url=yt)
    available_itags = get_available_itags(yt)
    args = [str(itag) for itag in available_itags]
    kb = KeyboardBuilder()
    kb.add_buttons(*args).next_row(2)
    kb.add_buttons(**{"preview": "Получить превью", "audio": "Скачать аудио"}).next_row(2)

    await message.answer_photo(
        photo=get_thumbnail_url(yt),
        caption=LEXICON_RU["resolution"].format(
            title=yt.title,
            author=yt.author,
            video_url=url,
            channel_url=yt.channel_url,
            date=yt.publish_date,
            description=yt.description,
        ),
        reply_markup=kb.get_keyboard(),
    )
    await state.set_state(DownloadVideoStates.resolution)

@router.callback_query(DownloadVideoStates.resolution, F.data == "preview")
async def send_preview_to_user(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    preview = get_thumbnail_url(data["url"])
    await cb.message.delete()
    await cb.message.answer_document(document=preview)

    await state.clear()

@router.callback_query(DownloadVideoStates.resolution, F.data == "audio")
async def send_audio_to_user(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    audio_stream = get_stream_by_itag(data["url"], 140)
    audio_file_path = await download_video(audio_stream)
    await cb.message.delete()
    await cb.message.answer_audio(audio=FSInputFile(audio_file_path))

    await delete_all(audio_file_path)
    await state.clear()

@router.callback_query(DownloadVideoStates.resolution, ~F.data.in_({"preview", "audio"}))
async def send_video_to_user(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    selected_itag = next(i for i in Itag if str(i) == cb.data)
    print(selected_itag)
    video_stream, audio_stream = get_video_and_audio_stream(
        data["url"], selected_itag.value
    )

    if not check_valid_video_and_audio_size(video_stream, audio_stream):
        await cb.message.answer(LEXICON_RU["error_big_file"])
        return
    await cb.message.delete()
    temp_message = await cb.message.answer(LEXICON_RU["waiting_download"])
    video_file_path = await download_video(video_stream)
    audio_file_path = await download_video(audio_stream)
    file_path = await merge_streams(video_file_path, audio_file_path)

    await cb.bot.delete_message(
        chat_id=cb.message.chat.id, message_id=temp_message.message_id
    )
    await cb.message.answer_video(video=FSInputFile(file_path))
    await delete_all(video_file_path, audio_file_path, file_path)

    await state.clear()
