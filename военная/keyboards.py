from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
tech_types_keyboard = InlineKeyboardMarkup()
tech_types_keyboard.add(InlineKeyboardButton('Танки', callback_data='tanks'))
tech_types_keyboard.add(InlineKeyboardButton('Бронетехника', callback_data='armored_vehicles'))
tech_types_keyboard.add(InlineKeyboardButton('Артиллерия', callback_data='artillery'))
tech_types_keyboard.add(InlineKeyboardButton('Авиация', callback_data='aviation'))
tech_types_keyboard.add(InlineKeyboardButton('Военные порты', callback_data='military_ports'))
tech_types_keyboard.add(InlineKeyboardButton('Военные погоны', callback_data='military_ranks'))

back_keyboard = InlineKeyboardMarkup()
back_keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))

military_ports_info_keyboard = InlineKeyboardMarkup()
military_ports_info_keyboard.add(InlineKeyboardButton('Подробнее о военных портах',
                                                        url='https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B5%D0%BD%D0%BD%D0%BE-%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D1%84%D0%BB%D0%BE%D1%82_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8'))

military_ranks_info_keyboard = InlineKeyboardMarkup()
military_ranks_info_keyboard.add(InlineKeyboardButton('Подробнее о военных погонах', url='https://tass.ru/infographics/9851'))



def get_keyboard_1():

    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    btn1 = KeyboardButton('Посмотреть код')
    keyboard.add(btn1)
    return keyboard

