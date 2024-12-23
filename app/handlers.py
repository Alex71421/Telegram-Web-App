from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from datetime import datetime, timedelta
from app.scheduler import schedule_task, send_scheduled_message


def register_handlers(dp, bot):

    # Команда /start
    @dp.message(CommandStart())
    async def start_command(message: Message):
        await message.answer(
            "Привет! Отправь сообщение в формате: \n\n"
            "`текст сообщения | ЧЧ:ММ`\n\n"
            "Пример: `Напомни позвонить | 14:30`",
            parse_mode="Markdown")


    # Обработчик задания времени
    @dp.message()
    async def schedule_message(message: Message):
        try:
            # Парсим текст сообщения и время
            text, time_str = message.text.split("|")
            text = text.strip()
            time_str = time_str.strip()
            target_time = datetime.strptime(time_str, "%H:%M").time()

            # Рассчитываем время отправки
            now = datetime.now()
            send_time = datetime.combine(now.date(), target_time)
            if send_time <= now:
                send_time += timedelta(days=1)  # Если время уже прошло, выбираем завтрашний день

            # Добавляем задачу в планировщик
            schedule_task(
                chat_id=message.chat.id,
                text=text,
                send_time=send_time,
                bot=bot,
                send_func=send_scheduled_message
            )

            await message.answer(f"Напоминание установлено на {send_time.strftime('%H:%M')}!")
        except ValueError:
            await message.answer("Неправильный формат. Используйте `текст сообщения | ЧЧ:ММ`.")