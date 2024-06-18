from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.keyboards import localization
from bot.bot import bot
from bot.states.lang import Lang



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
    
    if selected_lang == 'ua':
        lines = [
            "Ви обрали українську мову.",
            "Щоб отримати текст, надішліть голосове повідомлення.",
            "Щоб ознайомитись з командами введіть команду /help.",
        ]
    elif selected_lang == 'en':
        lines = [
            "You have selected English.",
            "To get the text, send a voice message.",
            "To view the commands, enter the /help command.",
        ]
    
    await callback_query.message.edit_text("\n".join(lines))
        