import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлаин!')


""" ************** КЛИЕНТСКАЯ ЧАСТЬ **************"""


@dp.message_handler(commands=['start', 'help'])
async def command_star(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply("Общение с ботом через лс, напишите ему: \nhttps://t.me/Pizza_SheefOkBot")


@dp.message_handler(commands=['Время_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Работаем без выходных, часы работы: 7:00-21:00")


@dp.message_handler(commands=['Адрес'])
async def pizza_adress_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Адрес:  г.Красноярск, ул.Ленина, д.287, пом.1")


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


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
