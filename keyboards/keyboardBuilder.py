from aiogram.utils.keyboard import InlineKeyboardBuilder


class KeyButton:
    def __init__(self):
        self.kb_builder = InlineKeyboardBuilder()

    def add_button(text: str, callback_data: str) -> None:
        pass
