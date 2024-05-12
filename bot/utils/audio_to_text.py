import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()

#converting voice message to text

def STT(file,lang):
    aai.settings.api_key = os.environ.get('API_TOKEN')

    FILE_URL = file
    
    config = aai.TranscriptionConfig(language_code=lang)

    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(FILE_URL)
    
    print(transcript.text)
    
    return transcript.text


