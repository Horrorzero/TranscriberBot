from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder




kb = [
    [KeyboardButton(text ='Speech to text')],
    [KeyboardButton(text ='Text to speech')],
    [KeyboardButton(text ='Languages')]
]


languages = InlineKeyboardBuilder()
languages.adjust(4)

flags = {
    "af": "🇿🇦",
    "ar": "🇸🇦",
    "bg": "🇧🇬",
    "bn": "🇧🇩",
    "bs": "🇧🇦",
    "ca": "🇦🇩",
    "cs": "🇨🇿",
    "da": "🇩🇰",
    "de": "🇩🇪",
    "el": "🇬🇷",
    "en": "🇬🇧",
    "es": "🇪🇸",
    "et": "🇪🇪",
    "fi": "🇫🇮",
    "fr": "🇫🇷",
    "gu": "🇮🇳",
    "hi": "🇮🇳",
    "hr": "🇭🇷",
    "hu": "🇭🇺",
    "id": "🇮🇩",
    "is": "🇮🇸",
    "it": "🇮🇹",
    "iw": "🇮🇱",
    "ja": "🇯🇵",
    "jv": "🇮🇩",
    "km": "🇰🇭",
    "kn": "🇮🇳",
    "ko": "🇰🇷",
    "la": "🇻🇦",
    "lv": "🇱🇻",
    "ml": "🇮🇳",
    "mr": "🇮🇳",
    "ms": "🇲🇾",
    "my": "🇲🇲",
    "ne": "🇳🇵",
    "nl": "🇳🇱",
    "no": "🇳🇴",
    "pl": "🇵🇱",
    "pt": "🇵🇹",
    "ro": "🇷🇴",
    "ru": "🇷🇺",
    "si": "🇱🇰",
    "sk": "🇸🇰",
    "sq": "🇦🇱",
    "sr": "🇷🇸",
    "su": "🇮🇩",
    "sv": "🇸🇪",
    "sw": "🇰🇪",
    "ta": "🇮🇳",
    "te": "🇮🇳",
    "th": "🇹🇭",
    "tl": "🇵🇭",
    "tr": "🇹🇷",
    "uk": "🇺🇦",
    "ur": "🇵🇰",
    "vi": "🇻🇳",
    "zh": "🇨🇳",
    "zh-TW": "🇹🇼",
}




for i in flags.keys():   
    languages.add(InlineKeyboardButton(text=flags[i], callback_data=f'{i}'))  
        

menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
