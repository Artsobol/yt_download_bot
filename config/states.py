from aiogram.fsm.state import StatesGroup, State


class DownloadVideoStates(StatesGroup):
    url = State()
    resolution = State()
