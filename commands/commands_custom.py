from data import open_file_json


def response_to_commands_custom(token_bot, add_message):
    try:
        data_auto = open_file_json.open_file_json_auto()
        price_range = add_message.text.split()
        price_from = int(price_range[0].strip())
        price_to = int(price_range[1].strip())
        auto_filter = [i for i in data_auto if price_from <= int(i['PRICE'][:-7].replace(' ', '')) <= price_to]

        if not auto_filter:
            token_bot.send_message(add_message.from_user.id, 'Извините, машин в данном диапазоне цен нет')
        else:
            for i_auto in auto_filter:
                token_bot.send_photo(add_message.from_user.id,
                                     photo=i_auto['LINK'][0],
                                     caption=f"{i_auto['AUTO']}\n"
                                             f"{i_auto['RUN']}\n"
                                             f"{i_auto['ENGINE']}\n"
                                             f"{i_auto['YEAR_OF_ISSUE']}\n"
                                             f"{i_auto['FUEL']}\n"
                                             f"{i_auto['PRICE']}")

    except (ValueError, IndexError):
        token_bot.send_message(add_message.from_user.id,
                               'Пожалуйста, введите диапазон цен в соответствии с форматом')

