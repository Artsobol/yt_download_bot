from aiogram import Router

from .start import router as start_router
from .help import router as help_router
from .download import router as download_router

handlers_router = Router()

handlers_router.include_routers(
    start_router,
    help_router,
    download_router,
)
