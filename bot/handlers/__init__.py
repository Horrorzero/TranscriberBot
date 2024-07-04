from aiogram import Router

from bot.handlers.start import router as start_router
from bot.handlers.help import router as help_router
from bot.handlers.stt import router as stt_router
from bot.handlers.lang import router as lang_router
from bot.handlers.checker import router as checker_router
from bot.logger import get_logger


router = Router()

logger = get_logger(__name__)

router.include_routers(
    start_router, help_router, stt_router, lang_router, checker_router
)