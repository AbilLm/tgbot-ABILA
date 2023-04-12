import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types



BOT_TOKEN = '6239478395:AAFLQoG_ipQ-wSp4UCDMQzFdi1WITzHjN8k'


bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать!")


@dp.message_handler(commands = ['help'])
async def send_help(message: types.Message):
    await message.reply("Как я могу вам помочь?")

@dp.message_handler(commands = ['myinfo'])
async def send_info(message: types.Message):
    await message.reply(f"Вы - {message.from_user.full_name} (ID: {message.from_user.id})")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)

