from data import open_file_json
import calendar
from telebot import types
from data import config
import pymysql


def button_main_menu():
    '''Функция добавляет кнопки главного меню'''
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='🚗Посмотреть автомобили🚗', callback_data='but1')
    button2 = types.InlineKeyboardButton(text='🖊Записаться на TEST DRIVE🖊', callback_data='but2')
    button3 = types.InlineKeyboardButton(text='😊Посмотреть информацию об автосалоне😊', callback_data='but3')
    button4 = types.InlineKeyboardButton(text='Наш сайт', url=config.url)
    buttons.add(button1, button2, button3, button4)
    return buttons


def push_car_button(token_bot, message):
    '''
    Функция отвечающая за кнопку ПОСМОТРЕТЬ АВТОМОБИЛИ
    1. Выводит список автомобилей и кнопку: НАЗАД В МЕНЮ
    2. При нажатии на автомобиль, выводит информацию автомобиля
    3. При нажатии на кнопку 'НАЗАД В МЕНЮ' возвращается в главное меню
    '''
    if 'but1' in message.data:
        data_auto = open_file_json.open_file_json_auto()
        button_auto_list = []
        list_auto_name = [i['AUTO'] for i in data_auto]
        markup_auto = types.InlineKeyboardMarkup(row_width=2)

        for i, y in enumerate(list_auto_name):
            button_auto_list.append(types.InlineKeyboardButton(text=f'{y}',
                                                               callback_data=f'auto{i}'))
        button_back = types.InlineKeyboardButton(text='НАЗАД В МЕНЮ', callback_data='back')
        markup_auto.add(*button_auto_list, button_back)
        token_bot.edit_message_text('Все автомобили в наличии\n'
                                    'Выберете автомобиль',
                                    message.message.chat.id,
                                    message.message.message_id,
                                    reply_markup=markup_auto)

    if message.data.startswith('auto'):
        of = open_file_json.open_file_json_auto()
        model_auto_button = int(message.data.replace('auto', ''))
        data_info_auto_list = []
        photo_auto = []
        for y, i in enumerate(of):
            if model_auto_button == y:
                data_info_auto_list.append(i['AUTO'])
                data_info_auto_list.append(i['RUN'])
                data_info_auto_list.append(i['ENGINE'])
                data_info_auto_list.append(i['YEAR_OF_ISSUE'])
                data_info_auto_list.append(i['FUEL'])
                data_info_auto_list.append(str(i['PRICE']))
                for t in i['LINK']:
                    photo_auto.append(types.InputMediaPhoto(t))

        token_bot.send_media_group(message.message.chat.id, photo_auto)
        token_bot.send_message(message.message.chat.id, text='\n'.join(data_info_auto_list))

    if message.data == 'back':
        token_bot.edit_message_text(chat_id=message.message.chat.id,
                                    message_id=message.message.id,
                                    text=f'Вы вернулись в главное меню\n'
                                    f'Выберете действие\n'
                                    f'<b>Нажми ➡️ /help если хочешь посмотреть команды</b>',
                                    reply_markup=button_main_menu(),
                                    parse_mode='html')


def push_test_drive_button(token_bot, message):
    '''
    Функция отвечающая за кнопку: ЗАПИСАТЬСЯ НА ТЕСТ ДРАЙВ
    1. Выводит месяц для записи
    2. Выводит дни для записи
    3. Выводит время для записи
    '''
    if 'but2' in message.data:
        markup_month = types.InlineKeyboardMarkup(row_width=2)
        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                  'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь',
                  ]

        buttons_month = [types.InlineKeyboardButton(text, callback_data=f'month_{i}')
                         for i, text in enumerate(months, 1)
                         ]
        markup_month.add(*buttons_month)
        token_bot.edit_message_text(chat_id=message.message.chat.id,
                                    message_id=message.message.id,
                                    text="Выберите месяц:",
                                    reply_markup=markup_month)

        return markup_month

    elif 'month_' in message.data:
        month = int(message.data.split("_")[1])
        cal = calendar.monthcalendar(2023, month)
        markup_day = types.InlineKeyboardMarkup(row_width=7)
        for week in cal:
            row = []
            for day in week:
                if day == 0:
                    row.append(types.InlineKeyboardButton(" ", callback_data='none'))
                else:
                    row.append(types.InlineKeyboardButton(str(day), callback_data=f'{str(day)} число'))
            markup_day.row(*row)

        token_bot.edit_message_text(chat_id=message.message.chat.id,
                                    message_id=message.message.id,
                                    text="Выберите день:",
                                    reply_markup=markup_day)

        return markup_day
    elif 'число' in message.data:
        markup_time = types.InlineKeyboardMarkup(row_width=4)
        time_but = []
        for i in range(10, 22):
            time_but.append(types.InlineKeyboardButton(f'{i}:00',
                                                       callback_data=f'время {str(i)}:00'))
        button_back = types.InlineKeyboardButton(text='НАЗАД В МЕНЮ', callback_data='back')
        markup_time.add(*time_but, button_back)
        token_bot.edit_message_text(chat_id=message.message.chat.id,
                                    message_id=message.message.id,
                                    text="Выберите время:",
                                    reply_markup=markup_time)
        return markup_time
    elif 'none' in message.data:
        token_bot.send_message(message.message.chat.id,
                               "Такого дня нет, выберете цифру на кнопках")
    elif 'время ' in message.data:
        token_bot.send_message(message.message.chat.id,
                               f"Вы выбрали {message.data}")


def button_response_info_shop(bot_token, message):
    '''
    Функция отвечающая за кнопку: ПОСМОТРЕТЬ ИНФОРМАЦИЮ ОБ АВТОСАЛОНЕ
    Выводит информацию об автосалоне
    '''
    if 'but3' in message.data:
        with open('data/info_shop.txt', 'r', encoding='utf-8') as file:
            read = file.read()
        bot_token.send_message(message.from_user.id, read)