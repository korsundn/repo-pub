"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5302540901:AAGt-IeG8Q9zV4xwkmxGPaQWc61pyBAD-fE'

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
