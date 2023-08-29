# разбираемся с aiogram
import logging
import asyncio
from aiogram import Bot, Dispatcher, types

# настраиваем логирование
logging.basicConfig(level='INFO')
# создаем объект бота
bot = Bot(token='6439271902:AAHWCTBiDahbVSj6nzRHn-RVMcrs42uZnT0')
# создаем диспетчера
dp = Dispatcher(bot)


# обработчик команды start
@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer('Hello')


async def main():
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
