import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Бот работает!"

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден!")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🤟 Telegram-канал", url="https://t.me/mmmmisl_m_channel")],
    [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/mmmmisl_m")],
    [InlineKeyboardButton(text="🚀 Threads", url="https://www.threads.com/@mmmmisl_m")],
    [InlineKeyboardButton(text="🎵 TikTok", url="https://www.tiktok.com/@mmmmisl_m")],
    [InlineKeyboardButton(text="🌍 Meera", url="https://meera.me/mmmmisl_m")],
])

@dp.message(Command("start"))
async def send_card(message: types.Message):
    text = "Привет! Ссылки на соцсети mmmmisl_m💥 можете найти ниже ⬇️"
    await message.answer(text=text, reply_markup=keyboard)

async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем бота в фоне
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    import threading
    threading.Thread(target=lambda: loop.run_until_complete(start_bot()), daemon=True).start()
    # Запускаем Flask
    app.run(host="0.0.0.0", port=10000)
