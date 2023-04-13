import hashlib
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/' + text
    # Формируем идентификатор, на примере официальной документации
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title='Статья Wikipedia:',
            url=link,
            input_message_content=types.InputTextMessageContent(
                message_text=link
            ))]

    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)
