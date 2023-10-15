from aiogram.types import CallbackQuery
from core.keyboards import inline_list_questions

async def btn_fac_click(callback: CallbackQuery):
    await callback.message.answer(text="Выберите интересующий вас вопрос.",
                                  reply_markup=inline_list_questions.fac)
    await callback.answer()
