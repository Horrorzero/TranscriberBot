import gtts
from aiogram import types


def TTS(text,lang):
    voice = gtts.gTTS(text,lang=lang)
    voice.save('voice.mp3')
    voice_file = types.FSInputFile('voice.mp3')
        
    return voice_file
    
    