import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("BOT_TOKEN")
if bot_token is None:
    raise ValueError(
        "BOT_TOKEN environment variable is not set. Please set it in order to run the bot. You can get a bot token from telegram."
    )

bot = Bot(bot_token)
