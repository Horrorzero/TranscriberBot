from aiogram import Bot

import os
from dotenv import load_dotenv

load_dotenv()

#client of bot

bot = Bot(token=os.environ.get('BOT_TOKEN'))