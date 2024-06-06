from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import PreCheckoutQuery

from ai.ai_consult import get_sovet
from ai.ai_assistent import get_response
from ai.img_generation import generate_image


Api = '7257861984:AAHJxxLkh058Qmy2ExQpQFUWJo2GWNZ7uss'
bot = Bot(token= Api)
dp = Dispatcher(bot)


@dp.message_handler(commands= ['start'])
async def start(message: types.Message):
    await message.answer('Привет, я бот шедеврум от Яндекс. Я сгенерирую картинку по вашему запросу\n'
                         '\n'
                         'Введи /help ')

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Запустить'),
        types.BotCommand(command='/help', description='Помощь'),
        types.BotCommand(command='/sovet', description='Помощь'),
    ]
    await bot.set_my_commands(commands)

# @dp.pre_checkout_query_handler()
# async def pre_checkout(query: PreCheckoutQuery):
#     await query.answer(ok=True)

@dp.message_handler(commands='help')
async def analize_message(message: types.Message):
    await message.reply('Команды-\n'
                        '/sovet + text\n'
                        '/generate_image + text')



@dp.message_handler(commands='sovet')
async def analize_message(message: types.Message):
    user = message.get_args()
    response_text = await get_sovet(user)
    await message.answer(response_text)



@dp.message_handler(commands='generate_image')
async def handler_message(message: types.Message):
    user = message.get_args()
    response_text = await get_response(user)
    user_text = response_text
    await message.reply(f"Вот твой улучшенный промпт {user_text}")
    print(user_text)
    await message.reply('Ожидайте, идет генерация изображения ')

    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f"Уфы, ошибка: {e}")



async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)