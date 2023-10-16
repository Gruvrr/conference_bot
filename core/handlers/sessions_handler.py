from aiogram import Bot
from aiogram.types import CallbackQuery
from core.keyboards import keyboard_session, back_button


async def choice_session(callback: CallbackQuery):
    await callback.message.answer(text="Выберете интересующее вас время.", reply_markup=keyboard_session.keyboard_time)
    await callback.answer()


async def choice_time_10(callback: CallbackQuery):
    await callback.message.answer(text="Первая сессия начинается в 10 часов. Будут работать следующие залы.", reply_markup=keyboard_session.keyboard_10)
    await callback.answer()


async def choice_time_12(callback: CallbackQuery):
    await callback.message.answer(text="Вторая сессия начинается в 12 часов. Будут работать следующие залы.", reply_markup=keyboard_session.keyboard_12)
    await callback.answer()


async def choice_time_15(callback: CallbackQuery):
    await callback.message.answer(text="В 15 часов начнется пленарное заседание ", reply_markup=back_button.back_on_sessions_time)
    await callback.answer()


