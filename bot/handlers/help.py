from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer('Голосове в текст: /stt \nТекст в голосове: /tts \nОбрати мову: /langs ')