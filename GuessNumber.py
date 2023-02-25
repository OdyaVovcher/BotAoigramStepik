#25.02.2023
#GuessNumber Bot
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command

BOT_TOKEN: str = '6245446770:AAFJ2ULztGn22ur_tFE4I2Lc-jj2xDoQ5tk'

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS: int = 5

user: dict = {
    'in_game': False,
    'secret_number': None,
    'attemps': None,
    'total_games': 0,
    'wins':0
}