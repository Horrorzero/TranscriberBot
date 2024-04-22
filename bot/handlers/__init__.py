from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from bot.handlers.start import router as start_router
from bot.handlers.checker import router as checker_router
from bot.config import bot

from bot.utils.stt import audio_to_text
from bot.utils.tts import TTS
from bot.utils.fsm import Lang

from bot.utils.filter import Voice
from bot.utils.filter import Checker

from bot.keyboards import languages

from pathlib import Path
import os
import pycountry


router = Router()

router.include_routers(start_router,checker_router)


@router.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer('Голосове в текст: /stt \nТекст в голосове: /tts \nОбрати мову: /langs ')
    

@router.message(Command(commands=['tts']))
async def text_to_speech(message: Message):
    msg = await message.answer('Введіть текст:')
    id = msg.message_id
   
    @router.message(Checker(id))
    async def audio(message: Message,  state: FSMContext):
        lang_data = await state.get_data()
        lang = lang_data.get('language', 'uk')
        
        audio = TTS(message.text,lang)
        await message.answer_voice(audio.text_to_audio())
        
           
@router.message(Command(commands=['stt']))
async def speech_to_text(message: Message):
    await message.answer(text='Надішліть голосове повіломлення!')
    
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
            txt = audio_to_text(file_on_disk, lang)
            await message.reply(txt)
            
            os.remove(file_on_disk)
        except:
            await message.reply('Нажаль, обрана мова не підтримується для цієї функції \nСпробуйте обрати іншу')
            os.remove(file_on_disk)
        
             
@router.message(Command(commands=['langs']))
async def langs(message: Message, state: FSMContext):
    await state.set_state(Lang.waiting_for_language)
    await message.answer('Мови, які Ви можете обрати для транскрибування: ', reply_markup=languages.as_markup(resize_keyboard=True))
    
  
@router.callback_query()
async def choosen(callback: CallbackQuery,state: FSMContext):
    lang = callback.data
    
    await state.update_data(language=lang)
    
    try:
        lng = pycountry.languages.get(alpha_2=lang)
    
        await callback.answer(lng.name) 
    except:       
        await callback.answer(callback.data) 
        