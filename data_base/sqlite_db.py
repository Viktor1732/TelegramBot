import sqlite3


def sql_start():
    global base, cur
    base = sqlite3.connect('pizza_base.db')
    cur = base.cursor()
    if base:
        print("Соединение с базой данных прошло успешно!")
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_data(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()
