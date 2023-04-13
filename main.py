import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import random

load_dotenv()
BOT_TOKEN = '6239478395:AAFLQoG_ipQ-wSp4UCDMQzFdi1WITzHjN8k'


bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать!")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    commands = [
        "/start - начать работу с ботом",
        "/help - показать список команд",
        "/myinfo - показать информацию о вас",
        "/picture - отправить случайную картинку"
    ]
    help_text = "\n".join(commands)
    await message.reply(help_text)



@dp.message_handler(commands=['myinfo'])
async def myinfo_command(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.reply(f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш username: @{username}")


async def cmd_picture(message: types.Message):
    img = ["images/img_1.png", "images/img_2.png", "images/img_3.png", "images/cat.webp"]
    photo = open(random.choice(img), "rb")
    await message.answer_photo(photo)
if __name__ == '__main__':
    executor.start_polling()
