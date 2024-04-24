from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.states.lang import Lang
from bot.keyboards import languages

import pycountry


router = Router()

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
        