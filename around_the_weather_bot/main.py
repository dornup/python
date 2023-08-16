# импортируем всякие нужные библиотеки
import os
import datetime
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='Token')
dispatcher = Dispatcher(bot)
