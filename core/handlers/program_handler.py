from aiogram.types import CallbackQuery
from core.keyboards.back_button import back_in_main_menu, back_on_message_13_dec


async def view_program(callback: CallbackQuery):
    await callback.message.answer(text="Это программа мероприятия", reply_markup=back_in_main_menu)
    await callback.answer()


async def view_program_13_dec(callback: CallbackQuery):
    await callback.message.answer(text="Это программа мероприятия", reply_markup=back_on_message_13_dec)
    await callback.answer()