from aiogram.types import Message
from core import settings
import psycopg2
from core.settings import db_settings
from aiogram import Bot


async def send_conference_tomorrow(bot: Bot):
    connection = None
    admin_id = int(settings.get_settings.bots.admin_id)
    try:
        connection = psycopg2.connect(
            host=db_settings.host,
            user=db_settings.user,
            password=db_settings.password,
            database=db_settings.db_name
        )
        print(f"[INFO] connection good")
        with connection.cursor() as cursor:
            cursor.execute("""SELECT user_id FROM users""")
            users = cursor.fetchall()

            sent_count = 0
            for user in users:
                user_id = user[0]
                try:
                    await bot.send_message(user_id, "Завтра мероприятие")
                    sent_count += 1
                except Exception as e:
                    print(f"Failed to send message to user_id {user_id}. Error: {e}")

            await bot.send_message(admin_id, text=f"Уведомления успешно отправлены! Отправлено сообщений: {sent_count}")

    except Exception as _ex:
        print(["[INFO] Error exception ", _ex])
    finally:
        if connection:
            connection.close()
            print("[INFO] Postgresql connection close")


async def send_conference_tomorrow_manual(message: Message, bot: Bot):
    connection = None
    admin_id = int(settings.get_settings.bots.admin_id)
    try:
        connection = psycopg2.connect(
            host=db_settings.host,
            user=db_settings.user,
            password=db_settings.password,
            database=db_settings.db_name
        )
        print(f"[INFO] connection good")
        with connection.cursor() as cursor:
            cursor.execute("""SELECT user_id FROM users""")
            users = cursor.fetchall()

            sent_count = 0
            for user in users:
                user_id = user[0]
                try:
                    await bot.send_message(user_id, "Завтра мероприятие")
                    sent_count += 1
                except Exception as e:
                    print(f"Failed to send message to user_id {user_id}. Error: {e}")

            await bot.send_message(admin_id, text=f"Уведомления успешно отправлены! Отправлено сообщений: {sent_count}")

    except Exception as _ex:
        print(["[INFO] Error exception ", _ex])
    finally:
        if connection:
            connection.close()
            print("[INFO] Postgresql connection close")


