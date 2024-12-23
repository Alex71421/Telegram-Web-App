import asyncio
from aiogram import Bot, Dispatcher, F

from app.handlers_temp import router

# Создание бота и обработчика сообщений
bot = Bot(token='7962799405:AAGcDE7uCs01J37cMgO1BA6nIWpwW-86bag')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
