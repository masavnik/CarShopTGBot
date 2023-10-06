import telebot
from data import config
from button_bot import button_main_menu, button_response_info_shop, push_car_button, push_test_drive_button
from commands import response_to_commands_help, response_to_commands_low, response_to_commands_high,\
                     response_to_commands_custom

from mysql_bot import my_sql_bot
from request_link import vehicle_data_recording


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    command_start_text = message.text
    user_id = message.chat.id
    my_sql_bot.write_command_to_database(user_id, command_start_text)
    bot.send_message(message.chat.id,
                     f'Здравствуй <b>{message.chat.first_name}</b>\n'
                     f'Выберете действие\n'
                     f'<b>Введи /help если хочешь посмотреть команды</b>',
                     reply_markup=button_main_menu(),
                     parse_mode='html'
                     )


@bot.callback_query_handler(func=lambda message: True)
def add_button_auto(message):
    push_car_button(bot, message)
    push_test_drive_button(bot, message)
    button_response_info_shop(bot, message)


@bot.message_handler(commands=['help'])
def get_text_messages(message):
    command_help_text = message.text
    user_id = message.chat.id
    my_sql_bot.write_command_to_database(user_id, command_help_text)
    response_to_commands_help(bot, message)


@bot.message_handler(commands=['low'])
def get_commands_low(message):
    command_low_text = message.text
    user_id = message.chat.id
    my_sql_bot.write_command_to_database(user_id, command_low_text)
    response_to_commands_low(bot, message)


@bot.message_handler(commands=['high'])
def get_commands_high(message):
    command_high_text = message.text
    user_id = message.chat.id
    my_sql_bot.write_command_to_database(user_id, command_high_text)
    response_to_commands_high(bot, message)


@bot.message_handler(commands=['history'])
def get_text_messages(message):
    user_id = message.chat.id
    list_commands = my_sql_bot.output_commands_from_databases(user_id)
    bot.send_message(message.from_user.id, 'Ваша история запросов')
    bot.send_message(message.from_user.id, '\n'.join(list_commands))


@bot.message_handler(commands=['custom'])
def get_commands_custom(message):
    command_custom_text = message.text
    user_id = message.chat.id
    my_sql_bot.write_command_to_database(user_id, command_custom_text)
    bot.send_message(message.from_user.id,
                     'Введите цену ОТ и ДО через пробел\n'
                     '<b>Пример: 1200000 4200000</b>',
                     parse_mode='html'
                     )


@bot.message_handler(func=lambda message: True)
def response_message_user(message):
    response_to_commands_custom(bot, message)


if __name__ == '__main__':
    # vehicle_data_recording()
    bot.infinity_polling()
