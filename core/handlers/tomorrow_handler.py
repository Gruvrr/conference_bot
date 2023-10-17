from aiogram.types import Message
from core import settings


async def send_conference_tomorrow(message: Message):

    if int(message.from_user.id) != int(settings.get_settings.bots.admin_id):
        await message.answer(text="У вас нет прав использовать эту команду")
    else:
        await message.answer(text="Завтра мероприятие")

