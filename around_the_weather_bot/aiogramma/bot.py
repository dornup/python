# разбираемся с aiogram
import logging
import asyncio
from aiogram import Bot, Dispatcher, types

# настраиваем логирование
logging.basicConfig(level='INFO')
# создаем объект бота
bot = Bot(token='Token')
# создаем диспетчера
dp = Dispatcher(bot)


# обработчик команды start
@dp.message_handler(commands=['start'])  # будет работать только после команды start
async def bot_start(message: types.Message):
    await message.answer('Hello')  # обычное сообщение


# @dp.message_handler(commands=['test'])
# async def bot_test(message: types.Message):
#     await message.reply('test passed')  # ответ
#
#
# @dp.message_handler(commands=['test2'])
# async def bot_test2(message: types.Message):
#     await message.reply('second test passed')


@dp.message_handler(commands=['dice'])
async def bot_dice(message: types.Message):
    await message.answer_dice(emoji='🎲')  # кидаем кубик) да, мне заняться нечем, и что?


@dp.message_handler(commands=['die'])
async def bot_die(message: types.Message):
    await bot.send_dice(12345678, emoji='🎲')  # будет отправлять кубик на указанный ID


async def main():
    await dp.start_polling()  # начинаем принимать новые сообщения


if __name__ == '__main__':
    asyncio.run(main())
