import asyncio

from aiogram import Dispatcher

from bot.handlers import router
from bot.bot import bot
from bot.logger import get_logger


logger = get_logger(__name__)

async def main():
    
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)
    
if __name__ == '__main__':
    loop = asyncio.new_event_loop()

    loop.run_until_complete(main())