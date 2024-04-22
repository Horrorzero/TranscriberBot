import gtts
from aiogram import types



class TTS():
    '''Converting text to audio '''
    
    def __init__(self,text,lang):
        self.tts = text
        self.language = lang
        
    def text_to_audio(self):
        voice = gtts.gTTS(self.tts, lang=self.language)
        voice.save('voice.mp3')
        voice_file = types.FSInputFile('voice.mp3')
        
        return voice_file
    
    