from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime

# Инициализация планировщика
scheduler = AsyncIOScheduler()

def schedule_task(chat_id: int, text: str, send_time: datetime, bot, send_func):
    """
    Планирует отправку сообщения.
    :param chat_id: ID чата, куда нужно отправить сообщение
    :param text: Текст сообщения
    :param send_time: Время, когда сообщение нужно отправить
    :param bot: Объект Telegram Bot
    :param send_func: Асинхронная функция отправки сообщения
    """
    scheduler.add_job(
        send_scheduled_message,
        trigger=DateTrigger(run_date=send_time),
        args=[chat_id, text, bot]
    )


# Асинхронная функция отправки сообщения
async def send_scheduled_message(chat_id: int, text: str, bot):
    """
    Отправляет сообщение в указанный чат.
    :param chat_id: ID чата
    :param text: Текст сообщения
    :param bot: Объект Telegram Bot
    """
    await bot.send_message(chat_id, f"Напоминание: {text}")


# Запуск планировщика
def start_scheduler():
    """
    Запускает планировщик.
    """
    scheduler.start()
