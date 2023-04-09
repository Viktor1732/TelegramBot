""" Код для создания файла цензуры .json из файла .txt """

import json

list_cens = []

with open('list_cens.txt', encoding='1251') as text:
    for t in text:
        if t != '':
            list_cens.append(t.lower().split('\n')[0])

with open('../cens.json', 'w', encoding='UTF-8') as rec_json:
    json.dump(list_cens, rec_json)


