from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_url = InlineKeyboardButton(text="Ссылка", callback_data="url")
button_title = InlineKeyboardButton(text="Название", callback_data="title")

start_kb = InlineKeyboardMarkup(inline_keyboard=[[button_url, button_title]])