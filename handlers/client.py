from aiogram import types, Dispatcher

from create_bot import dp, bot
from key_boards import kb_client


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через лс, напишите ему: \nhttps://t.me/Pizza_SheefOkBot")


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Работаем без выходных, часы работы: 7:00-21:00")


async def pizza_adress_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Адрес:  г.Красноярск, ул.Ленина, д.287, пом.1")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Время_работы'])
    dp.register_message_handler(pizza_adress_command, commands=['Адрес'])
