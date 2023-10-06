# telegrambot-carshop
# Оглавление
+ [Секретные данные](#Секретные_данные)
+ [Парсинг сайта](#Парсинг_сайта)
+ [Код для бота телеграм](#Код_для_бота_телеграм)
+ [База данных](#База_данных)

# Секретные данные <a name='Секретные_данные'></a> 

Все секретные данные хранятся в [`config.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/data/config.py)
* token - токен вашего бота, которые вы получаете с помощью бота BotFathe в телеграмме
* url - [ссылка для парсига](https://www.audi-perm.ru/)

###### Данные БД - база данных
* host = 'localhost'
* user - ваше имя в БД
* password = пароль для БД
* database = имя БД

# Парсинг сайта <a name='Парсинг_сайта'></a>

Для парсинга сайта используется [`request_link.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/request_link.py)
В коде происходить парсинг сайта с помощью ООП - объектно-орентированное программирование

###### Используемые библиотеки и данные
* import requests
* import json 
* from bs4 import BeautifulSoup
* from random import randint
* import data import config

###### Методы парсинга

* `requests_get` - подает запрос на сайт
* `link_cleaning` - чистит теги и возвращает список ссылок на изображения автомобилей
* `auto_cleaning` - создает список словарей с данными автомобилей (в данным словаре используется метод rondom с помощью которого мы
создаем примерные цены на автомобили так как на сайте нет цен)

* Функция `vehicle_data_recording` используется для записи всех данных с сайта в [JSON файл](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/data/parser.json), который мы будем использовать для вывода в телеграм боте

# Код для бота телеграм <a name='Код_для_бота_телеграм'></a>

Глаыный код телеграм бота находится в [`main.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/main.py)

Данный код обрабатывает все команды и запросы пользователя

1. /start
2. /help
3. /low
4. /high
5. /history
6. /custom
7. Кнопки при нажатии команды /start

### 1. /start

Данная команда используется при старте в боте и выводит: приветсвие пользователя, команду /help для помощи и кнопки(пункт 7)

![2023-04-24_22-16-53](https://user-images.githubusercontent.com/112847238/234094468-78cc3bc3-961b-44be-91f5-45de5e5ee1ab.png)

### 2. /help
Для обработки команды help используется [`commands_help.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/commands/commands_help.py)

Данная команда выводит команды под пунктами: 3, 4, 5, 6

![2023-04-24_22-22-47](https://user-images.githubusercontent.com/112847238/234095560-5e5ad598-7e51-4bec-befc-4c54a0f7d216.png)

### 3. /low

Для обработки команды low используется [`commands_low.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/commands/commands_low.py)

Данная команда выводит все автомобили от минимальной до максимальной цены и последнее сообщение для удобства: /start и /help

###### Первый автомобиль
![2023-04-24_22-32-08](https://user-images.githubusercontent.com/112847238/234097675-2e6241a0-669d-459f-bb28-28a3928025a2.png)

###### Последний автомобиль
![2023-04-24_22-32-39](https://user-images.githubusercontent.com/112847238/234097851-55429042-28ca-4719-876b-2567b2571693.png)

###### Последнее сообщение
![2023-04-24_22-33-13](https://user-images.githubusercontent.com/112847238/234098059-b2ff578c-d895-47f1-8638-e3456b89fa60.png)

### 4. /high

Для обработки команды low используется [`commands_high.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/commands/commands_high.py)

Данная команда выводит все автомобили от максимальной до минимальной цены и последнее сообщение для удобства: /start и /help

###### Первый автомобиль
![2023-04-24_22-42-05](https://user-images.githubusercontent.com/112847238/234099409-df7fbfb0-a202-4711-a8e1-8fcfb8ccc3ac.png)

###### Последний автомобиль
![2023-04-24_22-40-18](https://user-images.githubusercontent.com/112847238/234099424-7fcfdfa1-2530-4349-b602-dee0999cf43e.png)

###### Последнее сообщение
![2023-04-24_22-40-44](https://user-images.githubusercontent.com/112847238/234099434-7ec2a4a1-bf3b-4d60-b6ff-76907992ac76.png)

### 5. /history

Команда history выводит всю историю команд, который вводил пользователь

![2023-04-24_22-47-46](https://user-images.githubusercontent.com/112847238/234100619-9990052f-3f72-49a5-9209-9e789ce6b6e2.png)

Для вывода всех команд используется БД, в которой записываются и хранятся команды и id пользователя,

подрбнее читайте в пункте -> база данных

### 6. /custom

Для обработки команды custom используется взаимосвязаные декоратор `@bot.message_handler(commands=['custom'])` и [`commands_custom.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/commands/commands_custom.py)

Пользователю выводится сообщение: <b>Введите цену ОТ и ДО через пробел 'Пример: 1200000 4200000</b>.

Если пользователь ввел неправльные значение, то ему выводится сообщение : <b>Извините, машин в данном диапазоне цен нет</b>

![2023-04-24_23-01-06](https://user-images.githubusercontent.com/112847238/234103499-5044cd88-5418-4264-aad7-e7106a08972c.png)

![2023-04-24_23-02-58](https://user-images.githubusercontent.com/112847238/234103762-98f054e2-fc02-46cb-82f7-717469dd8de9.png)

### 7. Кнопки при нажатии /start

Обработка кнопок находятся в [`button_bot.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/button_bot.py)

`button_main_menu()` - функция, которая выводит кнопки главного меню

`push_car_button()` - функция, которая выводит кнопки автомобилей

`push_test_drive_button()` - функция для записи на тест драйв

`button_response_info_shop()` - функция выводит информацию об автосалоне

Все функции обрабатываются с помощью декоратора: `@bot.callback_query_handler(func=lambda message: True)`

### Посмотреть автомобили

При нажатии на кнопку `Посмотреть автомобили` сообщение обновляется, поэтому меню исчезает и выводится список кнопок автомобилей и кнопка назад.

###### Нажали на кнопку: Посмотреть автомобили

![2023-04-24_23-10-07](https://user-images.githubusercontent.com/112847238/234105569-f338d8d7-65e7-4a38-ad45-6a8383ffdb69.png)

###### Нажимаем на автомобиль <b>BMW X6</b>

![2023-04-24_23-10-57](https://user-images.githubusercontent.com/112847238/234105760-7afe2b45-cdd4-407d-977b-678061e44c67.png)

Как видим, что бот выводит фотографии и всю информацию об автомобиле, которые мы забирали с сайта с помощью `request_link.py`

###### Нажимаем кнопку назад в меню

![2023-04-24_23-15-56](https://user-images.githubusercontent.com/112847238/234106602-ed59b2b0-4239-4fd1-8951-31d8ff92b343.png)

Обратите внимание, что теперь пользователь видит главное меню и обновленное сообщение

### Записаться на TEST DRIVE

Кнопка выводит месяц, день, время для записи на тест драйв. Каждое сообщение обновляется

###### При нажатии на кнопку Записаться на TEST DRIVE выводятся кнопки:

![2023-04-24_23-41-57](https://user-images.githubusercontent.com/112847238/234112950-2add5024-816a-4130-9952-aeed2c4d90d8.png)

###### При нажатии на кнопку: Апрель. Выбираем день

![2023-04-24_23-42-39](https://user-images.githubusercontent.com/112847238/234113266-788bbcc5-bbef-4623-ac0c-c63bc36ed67b.png)

###### Выбираем время

![2023-04-24_23-43-34](https://user-images.githubusercontent.com/112847238/234113348-062d12a4-afc2-4eb3-83a2-e1cb73b51682.png)

###### Выводится сообщение:

![2023-04-24_23-44-18](https://user-images.githubusercontent.com/112847238/234113652-aec20785-84ae-4416-a458-7190a60ff621.png)

###### Что будет если нажать на пустой день, который не существует

![2023-04-24_23-51-10](https://user-images.githubusercontent.com/112847238/234114153-c629d304-1688-4961-9969-24e3734b3d6a.png)

### Посмотреть информацию об автосалоне

Кнопка выводит информацию об автосалое. Информация хранится в [`info_shop.txt`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/data/info_shop.txt)

![2023-04-24_23-55-00](https://user-images.githubusercontent.com/112847238/234115078-c7731942-7d85-46c6-8690-42ab8ef9ba28.png)

# База данных <a name='База_данных'></a>

Код для базы данных в [mysql_bot.py](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/mysql_bot.py)

Подключение к базе данных происходит с помощью ООП. Все данные берем с [`config.py`](https://github.com/masavnik/TELEGRAM-BOT-AUTO/blob/master/data/config.py)

* host = 'localhost'
* user - ваше имя в БД
* password = пароль для БД
* database = имя БД

В ООП используется 2 метода:

`write_command_to_database(user_id, commands)` - записывет в БД ID пользователя телеграм и команду при нажатии

`user_id` - id пользователя в телеграм

`commands` - команда, которая нажал пользователь

`output_commands_from_databases(user_id)` - забирает команды с БД и выводит в телеграм бот. 

`user_id` - id пользователя в телеграм
