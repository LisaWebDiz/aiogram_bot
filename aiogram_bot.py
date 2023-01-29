from config import tg_bot_token

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token = tg_bot_token)
dp = Dispatcher(bot)

HELP = """
/help - вывести список доступных команд
/add - добавить задачу в список
/show - напечатать все добавленные задачи"""

tasks = {
}

def add_todo (date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = [task]

@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
    await message.answer("Привет!")

@dp.message_handler(commands = ["add"])
async def add(message):
    command = list(message.text.split('\n'))
    if len(command) != 4:
        await message.answer("Задача введена некорректно")
    else:
        date = command[1]
        task = command[2]
        category = command[3]
        await message.answer(f'Задача {task} добавлена в категорию {category} на дату {date}')
        task = command[2]+ ' @ ' + command[3]
        add_todo (date, task)

@dp.message_handler(commands = ["show"])
async def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1]
    if date in tasks:
        await message.answer(date)
        for task in tasks[date]:
            await message.answer("* " + task)
    else:
        await message.answer("Задач на эту дату нет")

@dp.message_handler(commands = ["help"])
async def help(message):
    await message.answer(HELP)
