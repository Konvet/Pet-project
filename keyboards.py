#создание кнопок Inline
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import BotCommand

#Создание кнопок в главном меню
private_commands = [
    BotCommand(command="start", description="Начать"),
    BotCommand(command="help", description="Помощь"),
    BotCommand(command="questionnaire", description="Пройти опросник"),
    BotCommand(command="send_photo", description="Прислать фото")
]

#Создаю переменную, в которой у меня будет сама клавиуатура,
# в кот перечислены все кнопки
hello = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Да, хочу подкинуть', callback_data = 'information'),
    InlineKeyboardButton(text = 'Узнать о боте', callback_data= 'About bot')]
])

get_info = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Пройду опросник', callback_data= 'questionnaire'),
    InlineKeyboardButton (text = 'Пришлю фото', callback_data= 'send photo')]
])

conclusion = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Удалить фото', callback_data = 'delete')],
    [InlineKeyboardButton(text = 'Давай закончим уже', callback_data = 'end session'),
     InlineKeyboardButton(text = 'Следующее животное', callback_data = 'add info')]
])

conclusion2 = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Давай закончим уже', callback_data = 'end session'),
    InlineKeyboardButton(text = 'Следующее животное', callback_data = 'add info')],
    [InlineKeyboardButton(text = 'Хочу рассказать еще доп инфу', callback_data = 'story')]
])

conclusion3 = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Давай закончим уже', callback_data = 'end session'),
    InlineKeyboardButton(text = 'Следующее животное', callback_data = 'add info')]
])