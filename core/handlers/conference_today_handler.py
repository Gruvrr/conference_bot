from aiogram.types import CallbackQuery, Message
from core.keyboards import event_keyboard_13_dec
from core import settings


async def send_today_conference_callback(callback: CallbackQuery):
    await callback.message.answer(text=f"Сегодня мероприятие.\n"
                                       f"Ниже вы можете ознакомится в подробной программой и расписанием.",
                                  reply_markup=event_keyboard_13_dec.keyboard)
    await callback.answer()


async def send_today_conference_message(message: Message):
    user_id = int(message.from_user.id)
    admin_id = int(settings.get_settings.bots.admin_id)
    if user_id != admin_id:
        await message.answer(text=f"У вас нет прав использовать эту команду. ")
    else:
        await message.answer(text=f"Сегодня мероприятие.\n"
                                  f"Ниже вы можете ознакомится в подробной программой и расписанием.",
                             reply_markup=event_keyboard_13_dec.keyboard)
