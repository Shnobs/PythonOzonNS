import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '1902053824:AAEvs2gIrrbyU6fiIzHs1HXdY0St1-RH2Nk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchBot!\nPowered by aiogram")