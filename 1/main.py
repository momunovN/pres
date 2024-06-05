from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token='7371328229:AAEpg5OF2i4CBjC3mB4UPsQnNlLu9uRAy8g')
dp = Dispatcher(bot)

# async def set_commands(bot: Bot):
#     commands = [
#         types.BotCommand(command='/start', description='Запустить'),
#         types.BotCommand(command='/info', description='Info'),
#         types.BotCommand(command='/Life', description='Жизнь'),
#     ]
#     await bot.set_my_commands(commands)

async def set_commands2(bot: Bot):
    commands2 = [
        types.BotCommand(command='/start', description='Запустить'),
        types.BotCommand(command='/info', description='Info'),
        # types.BotCommand(command='/Life', description='Жизнь'),
        # types.BotCommand(command='/love', description='Любовь'),
        # types.BotCommand(command='/friend', description='Дружба'),
        types.BotCommand(command='/iecho', description='Эхо')
    ]
    await bot.set_my_commands(commands2)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет, я эхо бот')



@dp.message_handler(commands=['info'])
async def help(message: types.Message):
    await message.reply('Тут есть цитаты Омара Хайяма.\n'
                        'Команды: /Life\n'
                        '/love\n'
                        '/friend')

@dp.message_handler(commands=['Life'])
async def about(message: types.Message):
    await message.reply('Сорваный цветок должен быть подарен,\n начатое стихотворение — дописано,\n'
                        ' а любимая женщина — счастлива,\n'
                        ' иначе и не стоило браться за то,\n'
                        ' что тебе не по силам.')

@dp.message_handler(commands=['love'])
async def love(message: types.Message):
    await message.reply('В любимом человеке нравятся даже недостатки, а в нелюбимом раздражают даже достоинства.')


@dp.message_handler(commands=['friend'])
async def friend(message: types.Message):
    await message.reply('Любовь может обойтись без взаимности, но дружба — никогда.')

@dp.message_handler(commands=['iecho'])
async def iecho(message: types.Message):
    await message.reply('Привееееееетттик.....')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# async def on_startup(dispatcher):
#     await set_commands(dispatcher.bot)

async def on_startup2(dispatcher2):
    await set_commands2(dispatcher2.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup2)
