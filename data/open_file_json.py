import json


def open_file_json_auto():
    '''Функция отвечающая за открытие json файла
    В файле находится автомобили и вся информация о них
    '''
    with open('data/parser.json') as file:
        data_auto = json.load(file)
    return data_auto