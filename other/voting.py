import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

answ = dict()

inline_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Нравится', callback_data='like_1'),
    InlineKeyboardButton(text='Не нравится', callback_data='like_-1')
)


@dp.message_handler(commands='Голосование')
async def voting_commands(message: types.Message):
    await message.answer('Нравится ли вам наша пицца?', reply_markup=inline_kb)


@dp.callback_query_handler(Text(startswith='like_'))
async def voting_call(callback: types.CallbackQuery):
    result = int(callback.data.split('_')[1])
    if callback.from_user.id not in answ:
        answ[f'{callback.from_user.id}'] = result
        await callback.answer('Вы проголосовали!')
    else:
        await callback.answer('Вы уже проголосовали!', show_alert=True)


# starting_polling - бот периодически делает запросы на телеграм-сервер, чтоб узнать если ли новые сообщения.
executor.start_polling(dp, skip_updates=True)
