from aiogram.types import CallbackQuery, Message
from core.keyboards import event_keyboard_13_dec


async def send_today_conference_callback(callback: CallbackQuery):
    await callback.message.answer(text=f"Сегодня мероприятие.\n"
                                       f"Ниже вы можете ознакомится в подробной программой и расписанием.",
                                  reply_markup=event_keyboard_13_dec.keyboard)
    await callback.answer()

async def send_today_conference_message(message: Message):
    await message.answer(text=f"Сегодня мероприятие.\n"
                              f"Ниже вы можете ознакомится в подробной программой и расписанием.",
                         reply_markup=event_keyboard_13_dec.keyboard)