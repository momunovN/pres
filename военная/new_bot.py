from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tech_info import tech_info
from keyboards import tech_types_keyboard, back_keyboard, get_keyboard_1

API_TOKEN = '7484897887:AAHMrZ_cz3uwQrWV0xeRJnMxf0AXqC1YP40'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Это бот о военной тематике\n '
                         'Вы можете узнать о Танках, Артиллерии, Авиации и т.д')
    await message.answer('Выберите тип военной техники:', reply_markup=tech_types_keyboard)
    await message.answer('Вы еще можете посмотреть код этого бота', reply_markup=get_keyboard_1())



@dp.message_handler(lambda message: message.text == 'Посмотреть код')
async def check_password(message: types.Message):
    await message.answer('Введите пароль:')
    await message.answer('', reply_markup=types.ReplyKeyboardRemove())

password = '26кадр'

@dp.message_handler()
async def check_password_input(message: types.Message):
    if message.text == password:
        await message.answer('Пароль верен! Вот содержимое:')
        # здесь вы можете отправить содержимое, которое хотите показать
        await message.answer('')
    else:
        await message.answer('Пароль не верен!')



@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('Бот для просмотра информации о военной технике РФ')


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await message.answer('Бот создан для просмотра информации о военной технике РФ')


@dp.callback_query_handler()
async def tech_info_callback(callback: types.CallbackQuery):
    if callback.data == 'back':
        await callback.message.edit_text('Выберите тип военной техники:')
        await callback.message.answer('Выберите тип военной техники:', reply_markup=tech_types_keyboard)
    else:
        tech_type = callback.data
        tech_data = tech_info[tech_type]
        text = f'{tech_data["name"]}\n{tech_data["description"]}\n{tech_data["characteristics"]}'
        await callback.message.edit_text(text, reply_markup=back_keyboard)
        if 'info_keyboard' in tech_data:
            await callback.message.answer('Подробнее:', reply_markup=tech_data['info_keyboard'])
        for tech in tech_data['techs']:
            await callback.message.answer_photo(tech['image'])
            await callback.message.answer(f'{tech["name"]}\n{tech["description"]}\n{tech["characteristics"]}')

        # Add inline buttons to view information about other types of military equipment
        inline_keyboard = InlineKeyboardMarkup()
        for key in tech_info:
            if key != tech_type:
                inline_keyboard.add(InlineKeyboardButton(tech_info[key]['name'], callback_data=key))
        await callback.message.answer('Выберите другой тип военной техники:', reply_markup=inline_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)