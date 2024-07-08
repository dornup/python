# разбираемся с aiogram
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
import requests
from bs4 import BeautifulSoup
from very_secret_info import token
from aiogram.filters.command import Command
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from lxml.html.soupparser import fromstring

# все, что происходит далее - чистой воды прикол ради прикола 
# не судите меня строго, зато я изучаю http запросы и методы

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.get('https://geocult.ru/natalnaya-karta-onlayn-raschet')
time.sleep(2)
name = driver.find_element(by = By.CSS_SELECTOR, value = 'input[name="fn"]')
name.send_keys('name')
day = driver.find_element(by = By.CSS_SELECTOR, value = 'select[name="fd"]')
day.send_keys('18')
month = driver.find_element(by = By.CSS_SELECTOR, value = 'select[name="fm"]')
month.send_keys('Мая') # родительный падеж
year = driver.find_element(by = By.CSS_SELECTOR, value = 'select[name="fy"]')
year.send_keys('2009')
hour = driver.find_element(by = By.CSS_SELECTOR, value = 'select[name="fh"]')
hour.send_keys('15')
minute = driver.find_element(by = By.CSS_SELECTOR, value = 'select[name="fmn"]')
minute.send_keys('27')
country = driver.find_element(value='country')
country.send_keys('Россия')
time.sleep(1)
state = driver.find_element(value='state')
state.send_keys('Новосибирская область')
time.sleep(2)
cityplan = driver.find_element(value='cityplan')
time.sleep(2)
cityplan.send_keys('Новосибирск')
button = driver.find_element(By.CLASS_NAME, 'natal_button')
button.click()
driver.switch_to.window(driver.window_handles[1])
natal = requests.get(driver.current_url)
spaces = BeautifulSoup(natal.text, 'html.parser')
search_space = fromstring(str(spaces))
link = search_space.xpath('//a[contains(@class, "fancybox")]/@href')[0]
img = requests.get(link)
if img.status_code == 200:
    with open("img.jpg", "wb") as file:
        file.write(img.content)
        print("Картинка успешно скачана")
else:
    print("Не удалось скачать картинку")


# pic = driver.find_element(By.CSS_SELECTOR, 'a.fancybox img')


# получение полей ввода
# natal = requests.get('https://geocult.ru/natalnaya-karta-onlayn-raschet')
# spaces = BeautifulSoup(natal.text, 'html.parser')   # пока не нужны
# name_s = spaces.select('input[name="fn"]')
# day_s = spaces.select('select[name="fd"]')
# month_s = spaces.select('select[name="fm"]')
# year_s = spaces.select('select[name="fy"]')
# hour_s = spaces.select('select[name="fh"]')
# min_s = spaces.select('select[name="fmn"]')
# country_s = spaces.select('select#country')
# state_s = spaces.select('select#state')
# input_city = spaces.select('input#city')


# настраиваем логирование
logging.basicConfig(level='INFO')
# создаем объект бота
bot = Bot(token=token)
# создаем диспетчера
dp = Dispatcher()


# обработчик команды start
@dp.message(Command('start'))  # будет работать только после команды start
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


# @dp.message_handler(commands=['dice'])
# async def bot_dice(message: types.Message):
#     await message.answer_dice(emoji='🎲')  # кидаем кубик) да, мне заняться нечем, и что?


# @dp.message_handler(commands=['die'])
# async def bot_die(message: types.Message):
#     await bot.send_dice(12345678, emoji='🎲')  # будет отправлять кубик на указанный ID


async def main():
    await dp.start_polling(bot)  # начинаем принимать новые сообщения


if __name__ == '__main__':
    asyncio.run(main())



# https://geocult.ru/natalnaya-karta-onlayn-raschet?fn=hhh&fd=11&fm=4&fy=1980&fh=12&fmn=0&c1=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F&ttz=20&tz=Europe%2FMoscow&tm=3&lt=55.7522&ln=37.6155&hs=P&sb=1
# https://geocult.ru/natalnaya-karta-onlayn-raschet?fn=hhh&fd=3&fm=5&fy=1973&fh=12&fmn=0&c1=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F&ttz=20&tz=Europe%2FMoscow&tm=3&lt=55.7522&ln=37.6155&hs=P&sb=1
# https://geocult.ru/natalnaya-karta-onlayn-raschet?fn=hhh&fd=3&fm=5&fy=1973&fh=12&fmn=0&c1=%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D1%81%D0%BA%2C+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F&ttz=20&tz=Asia%2FYakutsk&tm=9&lt=50.2796&ln=127.540&hs=P&sb=1