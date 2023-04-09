from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("/Время_работы")
b2 = KeyboardButton("/Адрес")
b3 = KeyboardButton("/Меню")

# b4 = KeyboardButton("Поделиться номером", request_contact=True)
# b5 = KeyboardButton("Отправить моё месторасоложение", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# Расположение копок в столбец
kb_client.add(b1).add(b2).add(b3)

# Если есть место в строке, то кнопка встанет в строку
# kb_client.add(b1).add(b2).insert(b3)

# Расположение кнопок в ряд
# kb_client.row(b1, b2, b3)
