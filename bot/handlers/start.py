from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import menu

from bot.config import bot


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEL9q9mJQ8UnTHaJH4wZhJselG3OaocfQACBAEAAladvQreBNF6Zmb3bDQE')
    
    lines = [
        f"Вітаю, {message.from_user.first_name}.",
        "Я - Transcriber Bot, тут Ви можете конвертувати голосовий запис в текст і навпаки",
        "Щоб ознайомитись з командами введіть команду /help"
    ]
    
    await message.reply(
        text='\n'.join(lines),
    )
    