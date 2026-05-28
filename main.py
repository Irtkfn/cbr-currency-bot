import asyncio
import logging
import os
import xml.etree.ElementTree as ET

import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
PROXY_URL = os.getenv("PROXY_URL")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Настройка сессии с прокси, если он указан
session = AiohttpSession(proxy=PROXY_URL) if PROXY_URL else None
bot = Bot(token=API_TOKEN, session=session)
dp = Dispatcher()

async def get_rates():
    """Получает курсы валют с сайта ЦБ РФ."""
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    async with aiohttp.ClientSession() as http_session:
        try:
            async with http_session.get(url, timeout=15) as response:
                if response.status == 200:
                    data = await response.text()
                    root = ET.fromstring(data)

                    rates = {}
                    for valute in root.findall('Valute'):
                        char_code = valute.find('CharCode').text
                        value = valute.find('Value').text.replace(',', '.')
                        if char_code in ['USD', 'EUR', 'CNY']:
                            rates[char_code] = float(value)
                    return rates
        except Exception as e:
            logger.error(f"Ошибка при получении данных ЦБ: {e}")
        return None

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработка команды /start."""
    await message.answer("Привет! Напиши /rates, чтобы узнать курс валют ЦБ РФ.")

@dp.message(Command("rates"))
async def cmd_rates(message: types.Message):
    """Обработка команды /rates."""
    wait_msg = await message.answer("⏳ Запрашиваю данные с ЦБ РФ...")
    rates = await get_rates()

    if rates:
        text = (
            "💰 **Курс валют ЦБ РФ:**\n\n"
            f"🇺🇸 Доллар (USD): {rates.get('USD', 0):.2f} ₽\n"
            f"🇪🇺 Евро (EUR): {rates.get('EUR', 0):.2f} ₽\n"
            f"🇨🇳 Юань (CNY): {rates.get('CNY', 0):.2f} ₽"
        )
        await wait_msg.edit_text(text, parse_mode="Markdown")
    else:
        await wait_msg.edit_text("❌ Не удалось получить данные от ЦБ. Попробуйте позже.")

async def main():
    logger.info("Бот запущен...")
    try:
        me = await bot.get_me()
        logger.info(f"Подключен бот: @{me.username}")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")