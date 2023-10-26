import psycopg2
from aiogram.types import CallbackQuery, Message
from core.keyboards import event_keyboard_13_dec
from core import settings
from core.settings import db_settings
from aiogram import Bot


async def send_today_conference_callback(callback: CallbackQuery):
    await callback.message.answer(text=f"Сегодня мероприятие.\n"
                                       f"Ниже вы можете ознакомится в подробной программой и расписанием.",
                                  reply_markup=event_keyboard_13_dec.keyboard)
    await callback.answer()


async def send_today_conference_message(bot: Bot):
    admin_id = int(settings.get_settings.bots.admin_id)
    connection = psycopg2.connect(
        host=db_settings.host,
        user=db_settings.user,
        password=db_settings.password,
        database=db_settings.db_name
    )
    sent_count = 0
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT user_id FROM users")
            users = cursor.fetchall()

            for user in users:
                user_id = user[0]
                try:
                    await bot.send_message(user_id, text=f"Сегодня мероприятие.\n"
                                                                f"Ниже вы можете ознакомится в подробной программой и расписанием.",
                                                   reply_markup=event_keyboard_13_dec.keyboard)
                    sent_count += 1
                except Exception as e:
                    print(f"Failed to send message to user_id {user_id}. Error: {e}")

        await bot.send_message(admin_id, text=f"Уведомления успешно отправлены! Отправлено сообщений: {sent_count}")
    except Exception as _ex:
        print(["[INFO] Error exception ", _ex])
    finally:
        connection.close()
