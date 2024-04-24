from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.bot import bot


GREET_STICKER_ID = (
    "CAACAgIAAxkBAAEL9q9mJQ8UnTHaJH4wZhJselG3OaocfQACBAEAAladvQreBNF6Zmb3bDQE"
)

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await bot.send_sticker(message.chat.id, sticker=GREET_STICKER_ID)

    lines = [
        "Я - Transcriber Bot, тут Ви можете конвертувати голосовий запис в текст і навпаки",
        "Щоб ознайомитись з командами введіть команду /help",
    ]

    if message.from_user is not None:
        lines.insert(0, f"Вітаю, {message.from_user.first_name}.")

    await message.reply(
        text="\n".join(lines),
    )
    