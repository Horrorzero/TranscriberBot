from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.keyboards import localization
from bot.bot import bot
from bot.states.lang import Lang
from bot.utils.translations import translations



GREET_STICKER_ID = (
    "CAACAgIAAxkBAAEL9q9mJQ8UnTHaJH4wZhJselG3OaocfQACBAEAAladvQreBNF6Zmb3bDQE"
)

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Lang.lang)
    await bot.send_sticker(message.chat.id, sticker=GREET_STICKER_ID)
            
    lines = [
        "Я - Transcriber Bot, тут Ви можете конвертувати голосовий запис в текст",
        "Щоб отримати текст надішліть голосове повідомлення",
        "Щоб ознайомитись з командами введіть команду /help",
    ]

    await message.reply(
        text=" \n".join(lines),
        reply_markup=localization.as_markup()
    )

    
@router.callback_query(lambda c: c.data.startswith('lang_'))
async def set_language(callback_query: CallbackQuery, state: FSMContext):
    selected_lang = callback_query.data.split('_')[1]
    await state.update_data(lang = selected_lang)
    
    lines = [
        translations[selected_lang]['lang_selected'],
        translations[selected_lang]['send_voice'],
        translations[selected_lang]['view_commands']
    ]

    await callback_query.message.edit_text("\n".join(lines))
        