from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.filters.voice import Voice
from bot.utils.audio_to_text import STT
from bot.bot import bot


from pathlib import Path
import os

router = Router()
    
@router.message(Voice())
async def text(message: Message, state: FSMContext): 
    file_id = message.voice.file_id

    lang_data = await state.get_data()
    lang = lang_data.get('language', 'uk')
    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path("./Audios", f"{file_id}.mp3")
    file_on_disk = str(file_on_disk.resolve().absolute())
    await bot.download_file(file_path, destination=str(file_on_disk))
    
    try:
        txt = STT(file_on_disk, lang)
        await message.reply(txt)
        
    finally:
        os.remove(file_on_disk)
            