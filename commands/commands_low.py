from data import open_file_json
from time import sleep


def response_to_commands_low(token_bot, add_message):

    token_bot.send_message(add_message.from_user.id, 'Автомобили отсортированы:\n'
                                                     'от минимальной до максимальной цены')
    data_auto = open_file_json.open_file_json_auto()
    sort_data_auto = sorted(data_auto, key=lambda d: d['PRICE'])
    for y in sort_data_auto:
        token_bot.send_photo(add_message.from_user.id, photo=y['LINK'][0], caption=f"{y['AUTO']}\n"
                                                                                   f"{y['RUN']}\n"
                                                                                   f"{y['ENGINE']}\n"
                                                                                   f"{y['YEAR_OF_ISSUE']}\n"
                                                                                   f"{y['FUEL']}\n"
                                                                                   f"{y['PRICE']}",
                             )
        sleep(0.5)
    token_bot.send_message(add_message.from_user.id, '<b>Сортировка окончена\n</b>'
                                                     '<b>/start</b> - вернуться в главное меню\n'
                                                     '<b>/help</b> - вернуться в команды',
                                                     parse_mode='html'
                           )

