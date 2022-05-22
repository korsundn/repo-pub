"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from os import environ

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = environ.get('BOT_TOKEN', '/opt/macroinfo/macroinfo.txt')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Сам ты {message.text}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
