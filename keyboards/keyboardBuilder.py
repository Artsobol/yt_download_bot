from functools import singledispatchmethod
from typing import Self

from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class KeyboardBuilder:
    def __init__(self):
        self.kb_builder = InlineKeyboardBuilder()
        self.buttons: list[InlineKeyboardButton] = []

    def add_button(self, text: str, callback_data: str) -> Self:
        button = InlineKeyboardButton(text=text, callback_data=callback_data)
        self.buttons.append(button)

        return self

    def add_buttons(self, width: int | None = None, *args, **kwargs) -> Self:
        if args:
            for button in args:
                self.buttons.append(InlineKeyboardButton(text=button, callback_data=button))
        if kwargs:
            for button, text in kwargs.items():
                self.buttons.append(InlineKeyboardButton(text=text, callback_data=button))

        return self

    def next_row(self, width: int | None = None) -> Self:
        if self.buttons:
            self.kb_builder.row(*self.buttons, width=width)
            self.buttons.clear()
        return self

    def get_keyboard(self) -> InlineKeyboardMarkup:
        keyboard = self.kb_builder.as_markup()
        self.kb_builder = InlineKeyboardBuilder()
        self.buttons.clear()
        return keyboard