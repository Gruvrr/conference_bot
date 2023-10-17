import psycopg2

from core.settings import db_settings
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import select_FAC


async def get_start(message: Message, bot: Bot):
    connection = None
    try:
        connection = psycopg2.connect(
            host=db_settings.host,
            user=db_settings.user,
            password=db_settings.password,
            database=db_settings.db_name
        )
        print(f"[INFO] connection good")
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users (user_id, username, first_name, last_name) VALUES (%s, %s, %s, %s)""",
                (message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
            )
            connection.commit()
            print(f"[INFO] Данные успешно добавлены")
        await bot.send_message(message.from_user.id, (f"Здравствуйте, {message.from_user.first_name}.\n"
                                                      f"Благодарим за регистрацию на мероприятие!\n\n"
                                                      f"Ниже вы можете ознакомиться с программой мероприятия "
                                                      f"или посмотреть ответы на часто задаваемые вопросы."),
                                                      reply_markup=select_FAC)

    except Exception as _ex:
        print(["[INFO] Error exeption ", _ex])
    finally:
        if connection:
            connection.close()
            print("[INFO] Postgresql connection close")

