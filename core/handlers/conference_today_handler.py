from aiogram.types import Message


async def send_today_conference(message: Message):
    await message.answer(text="Сегодня мероприятие. Ниже вы можете ознакомится в подробной программой и расписанием.")

