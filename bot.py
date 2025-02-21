from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os

TOKEN = os.getenv("7802726283:AAFtXUHWY2ckklGYGviovcCUoizTnts-e7Y")  # Читаем токен из Railway
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функция для обработки сообщений в группе
@dp.message_handler(content_types=types.ContentType.TEXT, chat_type=types.ChatType.SUPERGROUP)
async def group_message(message: types.Message):
    if message.text.lower() == "/start":
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button = KeyboardButton(text="SkillHUB", url="https://sites.google.com/view/skillhub-kh-reg/головна?authuser=0")
        keyboard.add(button)

        await message.reply("SkillHUB", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)