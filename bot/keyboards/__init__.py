from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


localization = InlineKeyboardBuilder()
localization.adjust(2)

lang_ua = InlineKeyboardButton(text='Українська', callback_data='lang_ua')
lang_en = InlineKeyboardButton(text='English', callback_data='lang_en')

localization.add(lang_ua,lang_en)


flags = {
    "de": "🇩🇪",
    "en": "🇬🇧",
    "es": "🇪🇸",
    "fi": "🇫🇮",
    "fr": "🇫🇷",
    "hi": "🇮🇳",
    "it": "🇮🇹",
    "ja": "🇯🇵",
    "ko": "🇰🇷",
    "nl": "🇳🇱",
    "pl": "🇵🇱",
    "pt": "🇵🇹",
    "ru": "🇷🇺",
    "uk": "🇺🇦",
    "vi": "🇻🇳",
    "zh": "🇨🇳",
}



languages = InlineKeyboardBuilder()
languages.adjust(4)


for i in flags.keys():   
    languages.add(InlineKeyboardButton(text=flags[i], callback_data=f'{i}'))  
        
