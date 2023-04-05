from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Hello':
        await message.answer('Hello too!')

    # Ответ на сообщение
    # await message.answer(message.text)

    # Отвечает на сообщения путем выделения пользователя
    # await message.reply(message.text)

    # Ответ на сообщение в личку
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)
