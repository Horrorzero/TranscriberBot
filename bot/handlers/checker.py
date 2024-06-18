from aiogram import Router
from aiogram.types import Message
from aiogram.enums.chat_type import ChatType

from bot.bot import bot

router = Router()

@router.message()
async def checker(message: Message):
    if message.chat.type != ChatType.GROUP and message.chat.type != ChatType.SUPERGROUP:
        await bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)