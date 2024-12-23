import asyncio
from aiogram import Bot, Dispatcher
from app.scheduler import start_scheduler
from app.handlers import register_handlers
from apscheduler.schedulers.asyncio import AsyncIOScheduler


# Инициализация бота и диспетчера
bot = Bot(token='7962799405:AAGcDE7uCs01J37cMgO1BA6nIWpwW-86bag')
dp = Dispatcher()


# Главная асинхронная функция
async def main():
    print("Бот запущен...")
    start_scheduler()
    register_handlers(dp, bot)
    try:
        await dp.start_polling(bot)  # Запуск опроса Telegram
    finally:
        await bot.session.close()  # Закрываем сессию бота при завершении


# Запуск бота через asyncio
if __name__ == "__main__":
    asyncio.run(main())