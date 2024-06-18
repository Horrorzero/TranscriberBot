from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command(commands=['help']))
async def help(message: Message, state: FSMContext):
    state_data = await state.get_data()
    selected_lang = state_data.get('lang', 'ua')
    
    if selected_lang == 'ua':
        help_text = "Обрати мову: /langs \nЩоб отримати текст, просто надішліть голосове повідомлення"
    elif selected_lang == 'en':
        help_text = "Choose a language: /langs \nTo get the text, just send a voice message"
    
    await message.answer(help_text)