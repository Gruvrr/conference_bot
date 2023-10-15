from aiogram.types import Message


async def send_conference_tomorrow(message: Message):
    await message.answer(text="Завтра мероприятие")

