#Echobot 7.1
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

#Сюда токен бота
API_TOKEN: str = '6245446770:AAFJ2ULztGn22ur_tFE4I2Lc-jj2xDoQ5tk'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь в ответ я пришлю тебе твое сообщение')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')
    

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

cdcdcd = 4

