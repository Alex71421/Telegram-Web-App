import asyncio
from aiogram import Bot, Dispatcher, F

from app.handlers_temp import router
from app.database.models_temp import async_main




async def main():
    print("Бот запущен...")
    await async_main()
    # Создание бота и обработчика сообщений
    bot = Bot(token='7962799405:AAGcDE7uCs01J37cMgO1BA6nIWpwW-86bag')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
