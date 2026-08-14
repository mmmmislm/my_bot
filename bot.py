import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# СЮДА ВСТАВЬ СВОЙ ТОКЕН
BOT_TOKEN = "8875709967:AAFuA1MvBOH5gfpHuedFuXLrZmrGuouVDQI"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ВСЕ ТВОИ СОЦСЕТИ В КНОПКАХ
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
    text = (
        "Привет! Ссылки на соцсети mmmmisl_m💥 можете найти ниже ⬇️"
    )
    await message.answer(
        text=text,
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())