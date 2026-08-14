import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask

# --- Flask для Render ---
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Бот работает!"

# --- Сам бот ---
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Кнопки
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🤟 Telegram-канал", url="https://t.me/mmmmisl_m_channel")],
    [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/mmmmisl_m?igsh=dm1pNm5xMGc5OTli&utm_source=qr")],
    [InlineKeyboardButton(text="🚀 Threads", url="https://www.threads.com/@mmmmisl_m?igshid=NTc4MTIwNjQ2YQ==")],
    [InlineKeyboardButton(text="🎵 TikTok (основной)", url="https://www.tiktok.com/@mmmmisl_m?_r=1&_t=ZT-97QyIjOZ4NZ")],
    [InlineKeyboardButton(text="🎵 TikTok 2.0", url="https://www.tiktok.com/@mmmmisl_m2.0?_r=1&_t=ZT-98G4mvgEu0T")],
    [InlineKeyboardButton(text="🌍 Meera", url="https://meera.me/mmmmisl_m")],
])

@dp.message(Command("start"))
async def send_card(message: types.Message):
    text = "Привет! Ссылки на соцсети mmmmisl_m💥 можете найти ниже ⬇️"
    await message.answer(text=text, reply_markup=keyboard)

async def start_bot():
    await dp.start_polling(bot)

# --- Запуск ---
if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: asyncio.run(start_bot())).start()
    app.run(host="0.0.0.0", port=10000)
