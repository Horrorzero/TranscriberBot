from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.states.stt_lang import SttLang
from bot.keyboards import languages
from bot.utils.translations import translations

import pycountry


router = Router()

@router.message(Command(commands=['langs']))
async def langs(message: Message, state: FSMContext):
    await state.set_state(SttLang.waiting_for_language)
    
    state_data = await state.get_data()
    selected_lang = state_data.get('lang', 'ua')
 
    await message.answer(text=translations[selected_lang]['lang_text'], reply_markup=languages.as_markup(resize_keyboard=True))
    
  
@router.callback_query()
async def choosen(callback: CallbackQuery,state: FSMContext):
    lang = callback.data
    
    await state.update_data(language=lang)
    
    try:
        lng = pycountry.languages.get(alpha_2=lang)
    
        await callback.answer(lng.name) 
    except:       
        await callback.answer(callback.data) 
        