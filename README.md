# 💱 CBR Currency Bot

Телеграм-бот для получения актуальных курсов валют с сайта **Центрального Банка РФ**.

## 📋 Возможности

- 🇺🇸 Курс Доллара (USD)
- 🇪🇺 Курс Евро (EUR)
- 🇨🇳 Курс Юаня (CNY)

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone git@github.com:ВАШ_ЛОГИН/cbr-currency-bot.git
cd cbr-currency-bot
```

### 2. Создание виртуального окружения
```bash
python -m venv venv
```

### 3. Активация окружения

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 5. Настройка переменных окружения
Создайте файл `.env` в корне проекта и добавьте:
```env
BOT_TOKEN=ваш_токен_бота
PROXY_URL=http://логин:пароль@адрес:порт
```

### 6. Запуск бота
```bash
python main.py
```

## 📂 Структура проекта
```text
cbr-currency-bot/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 🛠 Технологии

- **Python 3.10+**
- **aiogram 3.x** — фреймворк для Telegram-ботов
- **aiohttp** — асинхронные HTTP-запросы
- **python-dotenv** — загрузка переменных окружения

## 🤖 Команды бота

| Команда  | Описание                       |
|----------|--------------------------------|
| `/start` | Приветственное сообщение       |
| `/rates` | Получить курсы валют с ЦБ РФ    |

## 📡 Источник данных
Данные загружаются с официального API ЦБ РФ:
[https://www.cbr.ru/scripts/XML_daily.asp](https://www.cbr.ru/scripts/XML_daily.asp)

## ⚠️ Примечание
Для работы из стран, где сайт ЦБ заблокирован, предусмотрена поддержка прокси через переменную `PROXY_URL`.
